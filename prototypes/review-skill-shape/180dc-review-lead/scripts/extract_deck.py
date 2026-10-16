# PROTOTYPE. Extract the text of each slide or page into deck.json.
#   python extract_deck.py <deck.pptx|deck.pdf|deck.docx> [-o deck.json]
# Standard library only for pptx/docx, so it runs whatever the sandbox has installed.
# PDF needs pypdf or the pdftotext tool; without either it says so and exits 2.
import json, re, subprocess, sys, zipfile
import xml.etree.ElementTree as ET

A = '{http://schemas.openxmlformats.org/drawingml/2006/main}t'
W = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'


def clean(s):
    return re.sub(r'\s+', ' ', s or '').strip()


def pptx(path):
    z = zipfile.ZipFile(path)
    names = [n for n in z.namelist() if re.fullmatch(r'ppt/slides/slide\d+\.xml', n)]
    names.sort(key=lambda n: int(re.search(r'(\d+)', n.rsplit('/', 1)[1]).group(1)))
    slides = []
    for i, n in enumerate(names, 1):
        root = ET.fromstring(z.read(n))
        # one entry per paragraph, so titles, bullets and cells stay separate items
        paras = []
        for p in root.iter('{http://schemas.openxmlformats.org/drawingml/2006/main}p'):
            t = clean(''.join(x.text or '' for x in p.iter(A)))
            if t:
                paras.append(t)
        slides.append({'n': i, 'items': paras})
    return slides


def docx(path):
    root = ET.fromstring(zipfile.ZipFile(path).read('word/document.xml'))
    paras = [clean(''.join(t.text or '' for t in p.iter(W + 't'))) for p in root.iter(W + 'p')]
    return [{'n': 1, 'items': [p for p in paras if p]}]


def pdf(path):
    try:
        from pypdf import PdfReader
        pages = [pg.extract_text() or '' for pg in PdfReader(path).pages]
    except ImportError:
        try:
            out = subprocess.run(['pdftotext', '-layout', path, '-'], capture_output=True,
                                 text=True, check=True).stdout
        except (OSError, subprocess.CalledProcessError):
            print('EXTRACT: could not run (no PDF reader here). Read the attachment directly.')
            sys.exit(2)
        pages = out.split('\f')
    return [{'n': i, 'items': [clean(l) for l in p.splitlines() if clean(l)]}
            for i, p in enumerate(pages, 1) if i <= len(pages)]


def main():
    args = sys.argv[1:]
    out = 'deck.json'
    if '-o' in args:
        out = args[args.index('-o') + 1]
    src = args[0]
    kind = src.lower().rsplit('.', 1)[-1]
    slides = {'pptx': pptx, 'docx': docx, 'pdf': pdf}[kind](src)
    unreadable = [s['n'] for s in slides if len(' '.join(s['items'])) < 20]
    json.dump({'file': src, 'slides': slides, 'unreadable': unreadable}, open(out, 'w'),
              ensure_ascii=False, indent=1)
    print(f'EXTRACT: {len(slides)} slides/pages to {out}. '
          f'Little or no text on: {", ".join(map(str, unreadable)) or "none"} '
          f'(images or charts: read those slides from the images).')


if __name__ == '__main__':
    main()
