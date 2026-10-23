# PROTOTYPE. Build the deck-walk page as a file, so slide pictures never pass through Claude.
#   python build_deck_walk.py review.json deck.json [deck.pdf|deck.pptx] [-o deck-walk.html] [--width 960] [--no-images]
# review.json is the REVIEW object Claude wrote (the same words as the chat review); deck.json comes from
# extract_deck.py. The deck file is optional: with it, each slide is rendered to a small JPEG and embedded.
# Rendering tries PyMuPDF, then pdftoppm; a .pptx goes through LibreOffice to PDF first. When none of that is
# available the page still works and shows each slide's text instead of its picture.
import base64, glob, json, os, re, shutil, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
TEMPLATE = os.path.join(HERE, '..', 'assets', 'deck-line.html')
MAX_LINES, MAX_CHARS = 10, 220          # slide text kept per slide, enough to recognise it in the viewer
BUDGET = 12 * 1024 * 1024               # keep the page well under the 16 MB an artifact allows


def fail(msg):
    print(f'BUILD: {msg}')
    sys.exit(2)


def pdf_pictures(pdf, width, quality):
    """Render every page to JPEG bytes. Returns (list of bytes, how) or (None, why not)."""
    try:
        import fitz  # PyMuPDF
        doc, out = fitz.open(pdf), []
        for page in doc:
            pix = page.get_pixmap(matrix=fitz.Matrix(width / page.rect.width, width / page.rect.width), alpha=False)
            try:
                out.append(pix.tobytes('jpeg', jpg_quality=quality))
            except (TypeError, ValueError):   # older PyMuPDF: no jpeg writer, go through Pillow
                from io import BytesIO
                from PIL import Image
                buf = BytesIO()
                Image.frombytes('RGB', (pix.width, pix.height), pix.samples).save(buf, 'JPEG', quality=quality)
                out.append(buf.getvalue())
        return out, 'PyMuPDF'
    except ImportError:
        pass
    if shutil.which('pdftoppm'):
        with tempfile.TemporaryDirectory() as tmp:
            subprocess.run(['pdftoppm', '-jpeg', '-jpegopt', f'quality={quality}', '-scale-to-x', str(width),
                            '-scale-to-y', '-1', pdf, os.path.join(tmp, 'p')], check=True, capture_output=True)
            files = sorted(glob.glob(os.path.join(tmp, 'p-*.jpg')), key=lambda f: int(re.findall(r'(\d+)\.jpg$', f)[0]))
            return [open(f, 'rb').read() for f in files], 'pdftoppm'
    return None, 'no PDF renderer here (PyMuPDF or pdftoppm)'


def pptx_to_pdf(pptx, tmp):
    office = shutil.which('soffice') or shutil.which('libreoffice')
    if not office:
        return None, 'no LibreOffice here to turn the .pptx into pages'
    try:
        subprocess.run([office, '--headless', '--convert-to', 'pdf', '--outdir', tmp, pptx],
                       check=True, capture_output=True, timeout=180)
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as e:
        return None, f'LibreOffice could not convert the deck ({type(e).__name__})'
    pdf = os.path.join(tmp, os.path.splitext(os.path.basename(pptx))[0] + '.pdf')
    return (pdf, 'LibreOffice') if os.path.exists(pdf) else (None, 'LibreOffice wrote no PDF')


def pictures(deck_file, n_slides, width):
    """Slide pictures as data URLs keyed by slide number, plus a one-line note on what happened."""
    kind = deck_file.lower().rsplit('.', 1)[-1]
    with tempfile.TemporaryDirectory() as tmp:
        pdf, via = deck_file, ''
        if kind == 'pptx':
            pdf, via = pptx_to_pdf(deck_file, tmp)
            if not pdf:
                return {}, via
            via += ' + '
        elif kind != 'pdf':
            return {}, f'cannot render .{kind} files'
        for quality in (70, 55, 40):               # step quality down until the pictures fit the budget
            jpgs, how = pdf_pictures(pdf, width, quality)
            if jpgs is None:
                return {}, how
            if len(jpgs) != n_slides:
                # numbers would not line up with the review (hidden slides, a different file): text only
                return {}, f'deck renders to {len(jpgs)} pages but deck.json has {n_slides} slides'
            if sum(len(j) for j in jpgs) * 4 / 3 < BUDGET:
                break
        else:
            return {}, 'slide pictures too large even at low quality'
    urls = {i: 'data:image/jpeg;base64,' + base64.b64encode(j).decode('ascii') for i, j in enumerate(jpgs, 1)}
    return urls, f'{len(urls)} pictures via {via}{how}, quality {quality}'


def check(review, n):
    """Warnings only: the page still builds, the lead should know what looks off."""
    warn = []
    for key in ('check', 'main', 'findings', 'works', 'couldntJudge', 'stamp'):
        if key not in review:
            warn.append(f'review.json has no "{key}"')
    for i, f in enumerate(review.get('findings', []), 1):
        bad = [s for s in f.get('slides', []) + [q.get('slide') for q in f.get('quotes', [])] if not 1 <= int(s) <= n]
        if bad:
            warn.append(f'finding {i} cites slide {bad[0]}, but the deck has {n}')
    return warn


def embed(obj):
    # JSON is valid JavaScript; only "</" could end the script tag early
    return json.dumps(obj, ensure_ascii=False).replace('</', '<\\/').replace('\u2028', '\\u2028').replace('\u2029', '\\u2029')


def main():
    args = sys.argv[1:]
    out, width, images = 'deck-walk.html', 960, True
    if '-o' in args:
        out = args.pop(args.index('-o') + 1); args.remove('-o')
    if '--width' in args:
        width = int(args.pop(args.index('--width') + 1)); args.remove('--width')
    if '--no-images' in args:
        images = False; args.remove('--no-images')
    if len(args) < 2:
        fail('usage: build_deck_walk.py review.json deck.json [deck.pdf|deck.pptx] [-o out.html]')
    review = json.load(open(args[0], encoding='utf-8'))
    deck = json.load(open(args[1], encoding='utf-8'))
    slides = deck.get('slides', [])
    n = len(slides)
    if not n:
        fail('deck.json has no slides')
    if not review.get('slides'):
        review['slides'] = n
    elif review['slides'] != n:
        print(f'BUILD: warning: review says {review["slides"]} slides, deck.json has {n}; using {n}')
        review['slides'] = n

    text = {s['n']: [l[:MAX_CHARS] for l in s['items'][:MAX_LINES]] for s in slides}
    pics, how = ({}, 'pictures turned off') if not images or len(args) < 3 else pictures(args[2], n, width)
    if images and len(args) < 3:
        how = 'no deck file given, so no pictures'

    page = open(TEMPLATE, encoding='utf-8').read()
    if '__REVIEW_JSON__' not in page or '__DECK_JSON__' not in page:
        fail(f'template {TEMPLATE} has no placeholders')
    page = page.replace('__REVIEW_JSON__', embed(review), 1).replace('__DECK_JSON__', embed({'text': text, 'images': pics}), 1)
    open(out, 'w', encoding='utf-8').write(page)

    for w in check(review, n):
        print(f'BUILD: warning: {w}')
    print(f'BUILD: wrote {out} ({os.path.getsize(out) / 1024 / 1024:.1f} MB, {n} slides). '
          f'Pictures: {how}. Slide text is in the page either way.')


if __name__ == '__main__':
    main()
