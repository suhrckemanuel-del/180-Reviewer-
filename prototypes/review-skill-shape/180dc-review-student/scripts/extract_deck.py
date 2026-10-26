# PROTOTYPE. Extract the text of each slide or page into deck.json.
#   python extract_deck.py <deck.pptx|deck.pdf|deck.docx> [-o deck.json]
# Standard library only for pptx/docx, so it runs whatever the sandbox has installed.
# PDF needs pypdf or the pdftotext tool; without either it says so and exits 2.
import json, re, subprocess, sys, zipfile
import xml.etree.ElementTree as ET

A = '{http://schemas.openxmlformats.org/drawingml/2006/main}t'
W = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
P = '{http://schemas.openxmlformats.org/presentationml/2006/main}'
R = '{http://schemas.openxmlformats.org/officeDocument/2006/relationships}'
D = '{http://schemas.openxmlformats.org/drawingml/2006/main}'


def clean(s):
    # some PDF readers return an emoji as two halves; rejoin them, or drop a lone half, so the JSON can be written
    s = (s or '').encode('utf-16', 'surrogatepass').decode('utf-16', 'replace')
    return re.sub(r'\s+', ' ', s).strip()


def pptx(path):
    z = zipfile.ZipFile(path)
    # slides in presentation order, hidden ones left out, so numbers match what the lead sees
    rels = ET.fromstring(z.read('ppt/_rels/presentation.xml.rels'))
    target = {r.get('Id'): 'ppt/' + r.get('Target').lstrip('/').removeprefix('ppt/') for r in rels}
    pres = ET.fromstring(z.read('ppt/presentation.xml'))
    names = [target[s.get(R + 'id')] for s in pres.iter(P + 'sldId')]
    slides = []
    for n in names:
        root = ET.fromstring(z.read(n))
        if root.get('show') == '0':
            continue
        i = len(slides) + 1
        # one entry per paragraph, so titles, bullets and cells stay separate items
        paras, sizes = [], []
        for p in root.iter('{http://schemas.openxmlformats.org/drawingml/2006/main}p'):
            t = clean(''.join(x.text or '' for x in p.iter(A)))
            if t:
                paras.append(t)
                sz = [int(r.get('sz')) for r in p.iter(D + 'rPr') if r.get('sz')]
                sizes.append(max(sz) if sz else 0)
        slide = {'n': i, 'items': paras}
        # file order often puts small labels before the title, so name the title when the
        # slide says which it is, and otherwise the one paragraph set larger than the rest
        # (usually the title, sometimes a number callout)
        ph = [clean(''.join(x.text or '' for x in sp.iter(A))) for sp in root.iter(P + 'sp')
              if (f := sp.find('.//' + P + 'ph')) is not None and f.get('type') in ('title', 'ctrTitle')]
        big = [t for t, s in zip(paras, sizes) if s and s == max(sizes)]
        if ph and ph[0]:
            slide['title'] = ph[0]
        elif len(big) == 1:
            slide['largest_text'] = big[0]
        slides.append(slide)
    return slides


def docx(path):
    root = ET.fromstring(zipfile.ZipFile(path).read('word/document.xml'))
    paras = [clean(''.join(t.text or '' for t in p.iter(W + 't'))) for p in root.iter(W + 'p')]
    return [{'n': 1, 'items': [p for p in paras if p]}]


def pdf_largest(page):
    # the text set in the page's largest font: usually the title, sometimes a number or divider
    chunks = []
    def visit(text, cm, tm, font, size):
        if text.strip():
            chunks.append((round(abs(size * tm[3] * cm[3]), 1), text.strip()))
    try:
        page.extract_text(visitor_text=visit)
    except Exception:
        return None
    if not chunks:
        return None
    top = max(s for s, _ in chunks)
    return clean(' '.join(t for s, t in chunks if s == top).replace('ﬁ', 'fi').replace('ﬂ', 'fl'))


def pdf(path):
    try:
        from pypdf import PdfReader
        reader = PdfReader(path)
        pages = [pg.extract_text() or '' for pg in reader.pages]
        largest = [pdf_largest(pg) for pg in reader.pages]
        slides = [{'n': i, 'items': [clean(l) for l in p.splitlines() if clean(l)]}
                  for i, p in enumerate(pages, 1)]
        for s, big in zip(slides, largest):
            if big:
                s['largest_text'] = big
        return slides
    except ImportError:
        try:
            out = subprocess.run(['pdftotext', '-layout', path, '-'], capture_output=True,
                                 text=True, check=True).stdout
        except (OSError, subprocess.CalledProcessError):
            print('EXTRACT: could not run (no PDF reader here). Read the attachment directly.')
            sys.exit(2)
        pages = out.rstrip('\f').split('\f')  # pdftotext ends every page with \f
    return [{'n': i, 'items': [clean(l) for l in p.splitlines() if clean(l)]}
            for i, p in enumerate(pages, 1)]


def main():
    args = sys.argv[1:]
    out = 'deck.json'
    if '-o' in args:
        out = args[args.index('-o') + 1]
    src = args[0]
    kind = src.lower().rsplit('.', 1)[-1]
    slides = {'pptx': pptx, 'docx': docx, 'pdf': pdf}[kind](src)
    unreadable = [s['n'] for s in slides if len(' '.join(s['items'])) < 20]
    json.dump({'file': src, 'kind': kind, 'slides': slides, 'unreadable': unreadable},
              open(out, 'w', encoding='utf-8'),
              ensure_ascii=False, indent=1)
    print(f'EXTRACT: {len(slides)} slides/pages to {out}. '
          f'Little or no text on: {", ".join(map(str, unreadable)) or "none"} '
          f'(images or charts: read those slides from the images).')


if __name__ == '__main__':
    main()
