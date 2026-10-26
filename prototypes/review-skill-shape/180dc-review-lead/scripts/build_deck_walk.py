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


def passages(rects):
    """One box per quoted passage: pieces on the same line merge, and lines that follow each other merge into one
    block, so a two-line title reads as one annotation. Lines far apart (a different text box) stay separate."""
    lines = []
    for r in sorted(rects, key=lambda r: (r[1], r[0])):
        for ln in lines:                                  # same line: vertical overlap of more than half a line
            if min(ln[3], r[3]) - max(ln[1], r[1]) > 0.5 * min(ln[3] - ln[1], r[3] - r[1]):
                ln[:] = [min(ln[0], r[0]), min(ln[1], r[1]), max(ln[2], r[2]), max(ln[3], r[3])]
                break
        else:
            lines.append(list(r))
    blocks = []
    for ln in sorted(lines, key=lambda r: r[1]):
        b = blocks[-1] if blocks else None
        if b and ln[1] - b[3] < 0.6 * (ln[3] - ln[1]) and min(b[2], ln[2]) > max(b[0], ln[0]):
            b[:] = [min(b[0], ln[0]), b[1], max(b[2], ln[2]), max(b[3], ln[3])]
        else:
            blocks.append(ln)
    return blocks


def find(page, s):
    """Search the page for s as written, then with straight and curly quotes swapped: the quote check counts
    them as the same character, so a quote that passed it may use the other kind than the slide."""
    straight = s.translate(str.maketrans({'‘': "'", '’': "'", '“': '"', '”': '"'}))
    curly = re.sub(r'"([^"]*)"', '“\\1”', straight.replace("'", '’'))
    for v in dict.fromkeys([s, curly, straight]):
        hits = page.search_for(v)
        if hits:
            return hits
    return []


def quote_boxes(pdf, wanted):
    """Where each quote sits on its slide, as fractions of the page: {slide: {quote: [[x0, y0, x1, y1], ...]}},
    and the slides where a quote was found only in part. Needs PyMuPDF; without it the page shows the slides
    without highlight boxes."""
    try:
        import fitz
    except ImportError:
        return {}, []
    doc, out, partly = fitz.open(pdf), {}, []
    for n, quotes in wanted.items():
        page = doc[n - 1]
        w, h = page.rect.width, page.rect.height
        for q in quotes:
            words = q.split()
            # the whole quote first; a quote broken across lines or boxes is found by its two ends
            hits = find(page, ' '.join(words))
            if not hits and len(words) > 6:
                head, tail = find(page, ' '.join(words[:5])), find(page, ' '.join(words[-5:]))
                hits = head + tail
                if hits and not (head and tail):
                    partly.append(n)              # one end only: the box covers part of the quote
            if hits:
                out.setdefault(n, {})[q] = [[round(x0 / w, 4), round(y0 / h, 4), round(x1 / w, 4), round(y1 / h, 4)]
                                            for x0, y0, x1, y1 in passages([(r.x0, r.y0, r.x1, r.y1) for r in hits[:8]])]
    return out, partly


def pictures(deck_file, n_slides, width, wanted):
    """Slide pictures as data URLs keyed by slide number, where the quotes sit on them, and a one-line note."""
    kind = deck_file.lower().rsplit('.', 1)[-1]
    with tempfile.TemporaryDirectory() as tmp:
        pdf, via = deck_file, ''
        if kind == 'pptx':
            pdf, via = pptx_to_pdf(deck_file, tmp)
            if not pdf:
                return {}, {}, via
            via += ' + '
        elif kind != 'pdf':
            return {}, {}, f'cannot render .{kind} files'
        for quality in (70, 55, 40):               # step quality down until the pictures fit the budget
            jpgs, how = pdf_pictures(pdf, width, quality)
            if jpgs is None:
                return {}, {}, how
            if len(jpgs) != n_slides:
                # numbers would not line up with the review (hidden slides, a different file): text only
                return {}, {}, f'deck renders to {len(jpgs)} pages but deck.json has {n_slides} slides'
            if sum(len(j) for j in jpgs) * 4 / 3 < BUDGET:
                break
        else:
            return {}, {}, 'slide pictures too large even at low quality'
        boxes, partly = quote_boxes(pdf, wanted)
    urls = {i: 'data:image/jpeg;base64,' + base64.b64encode(j).decode('ascii') for i, j in enumerate(jpgs, 1)}
    found = sum(len(v) for v in boxes.values()) - len(partly)
    part = f', {len(partly)} only in part (slide {", ".join(map(str, sorted(set(partly))))})' if partly else ''
    return urls, boxes, f'{len(urls)} pictures via {via}{how}, quality {quality}; {found} of {sum(len(v) for v in wanted.values())} quotes located on their slide{part}'


def check(review, n):
    """Warnings only: the page still builds, the lead should know what looks off."""
    warn = []
    for key in ('check', 'main', 'findings', 'works', 'couldntJudge', 'stamp'):
        if key not in review:
            warn.append(f'review.json has no "{key}"')
    for i, f in enumerate(review.get('findings', []), 1):
        if not f.get('slides') and not f.get('quotes'):
            warn.append(f'finding {i} has no slide and no quote, so it has no place on the line')
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
    wanted = {}                                       # every quote the page shows, by the slide it sits on
    for f in review.get('findings', []):
        for q in f.get('quotes', []):
            wanted.setdefault(int(q['slide']), set()).add(q['text'])
    for w in review.get('works', []):
        wanted.setdefault(int(w['slide']), set()).add(w['quote'])
    wanted = {k: sorted(v) for k, v in wanted.items() if 1 <= k <= n}
    pics, boxes, how = ({}, {}, 'pictures turned off') if not images or len(args) < 3 else pictures(args[2], n, width, wanted)
    if images and len(args) < 3:
        how = 'no deck file given, so no pictures'

    page = open(TEMPLATE, encoding='utf-8').read()
    if '__REVIEW_JSON__' not in page or '__DECK_JSON__' not in page:
        fail(f'template {TEMPLATE} has no placeholders')
    page = page.replace('__REVIEW_JSON__', embed(review), 1).replace('__DECK_JSON__', embed({'text': text, 'images': pics, 'boxes': boxes}), 1)
    open(out, 'w', encoding='utf-8').write(page)

    for w in check(review, n):
        print(f'BUILD: warning: {w}')
    print(f'BUILD: wrote {out} ({os.path.getsize(out) / 1024 / 1024:.1f} MB, {n} slides). '
          f'Pictures: {how}. Slide text is in the page either way.')


if __name__ == '__main__':
    main()
