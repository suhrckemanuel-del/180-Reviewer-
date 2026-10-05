# deck-to-paste.py -- turn a real deliverable into the block you paste into the reviewer.
#
#   python deck-to-paste.py <deck.pptx|deck.pdf|deck.docx> [-o out.md]
#
# Writes the DELIVERABLE TEXT block, slide-segmented, plus the extraction-notes block the
# reviewer needs. Prints the result to stdout if no -o is given.
#
# Local only. Text/JSON are working aids. Original pages remain authoritative.
# Selection preserves original page/slide numbers. Damaged text OR lost relationships
# require source-page inspection; the presence of words is not proof of faithful extraction.
# All file outputs must stay in the repository's ignored _client-private area.

import sys, os, re, argparse, json, hashlib, html, subprocess
from pathlib import Path

def clean(s):
    return re.sub(r'[ \t]+', ' ', (s or '').replace('\r', '').strip())

# ---------------------------------------------------------------- pptx

def from_pptx(path, include_notes=False):
    from pptx import Presentation
    from pptx.util import Emu
    prs = Presentation(path)
    slides, notes, chart_unreadable, unbound = [], [], [], []

    for i, slide in enumerate(prs.slides, 1):
        body, had_text, tables, pics = [], False, 0, 0

        # Reading order: top to bottom, then left to right. A deck read in shape order is
        # the "scrambled"/"interleaved" case, and it is avoidable here so we avoid it.
        def pos(sh):
            try:
                return (sh.top if sh.top is not None else Emu(0),
                        sh.left if sh.left is not None else Emu(0))
            except Exception:
                return (0, 0)

        for shape in sorted(slide.shapes, key=pos):
            # --- text
            if getattr(shape, 'has_text_frame', False) and shape.has_text_frame:
                t = clean(shape.text_frame.text)
                if t:
                    body.append(t)
                    had_text = True

            # --- tables, with the header row kept and each cell bound to its column
            if getattr(shape, 'has_table', False) and shape.has_table:
                rows = [[clean(c.text) for c in r.cells] for r in shape.table.rows]
                if not rows or not any(v for r in rows for v in r):
                    continue
                # A 1x1 "table" is a decorative text box, not data. Real decks are full of
                # them. Emitting them as tables mislabels prose as a data structure.
                if len(rows) == 1 and len(rows[0]) == 1:
                    body.append(rows[0][0])
                    had_text = True
                    continue
                tables += 1
                # Preserve all cells, including blanks. A populated row is not proof of a header.
                body.append('[Table, row/column order preserved; header status not inferred]')
                body.extend('  ' + ' | '.join(row) for row in rows)
                unbound.append(i)
                had_text = True

            # --- charts: recover categories and series values
            if getattr(shape, 'has_chart', False) and shape.has_chart:
                try:
                    ch = shape.chart
                    cats = [clean(str(c)) for c in ch.plots[0].categories]
                    title = ''
                    try:
                        if ch.has_title:
                            title = clean(ch.chart_title.text_frame.text)
                    except Exception:
                        pass
                    lines = []
                    for s in ch.series:
                        vals = list(s.values)
                        if not vals:
                            continue
                        # A chart can carry values with no category names at all: the labels
                        # live in separate text boxes on the slide. Dropping the values in that
                        # case is worse than useless, because it also writes a "values not
                        # recoverable" note, and that note suspends the comparator test on the
                        # one slide whose numbers the reader most needs interrogated.
                        if cats:
                            body_vals = '; '.join(f'{cats[j] if j < len(cats) else "unlabelled value " + str(j+1)}: {v if v is not None else "not supplied"}' for j, v in enumerate(vals))
                        else:
                            body_vals = ('values in chart order, labels are elsewhere on the '
                                         'slide: ' + ', '.join(str(v) for v in vals))
                        lines.append(f'  {clean(s.name) or "series"} -- ' + body_vals)
                    if lines:
                        body.append(f'[Chart{" " + title if title else ""}]')
                        body.extend(lines)
                        had_text = True
                    else:
                        chart_unreadable.append(i)
                except Exception:
                    chart_unreadable.append(i)

            if shape.shape_type is not None and 'PICTURE' in str(shape.shape_type):
                pics += 1

        try:
            n = slide.notes_slide.notes_text_frame.text if include_notes and slide.has_notes_slide else ''
            if clean(n):
                body.append('[Speaker notes] ' + clean(n))
        except Exception:
            pass

        slides.append((i, body))
        if pics:
            notes.append((i, 'images are not represented by text; inspect the original slide'))
        if not had_text:
            notes.append((i, 'image-only, no extractable text on this slide'))
    # A chart we could not read is lost TEXT: its values are not in the input at all, so the
    # comparator test must be suspended on that slide rather than reported as a missing
    # comparator. This is the note the gate keys on.
    for i in sorted(set(chart_unreadable)):
        notes.append((i, 'chart present but its values are not recoverable as text, '
                         'no values at all were extracted'))
    # Plain text cannot establish visual grouping, merged headings or table meaning.
    for i in sorted(set(unbound)):
        notes.append((i, 'table cells are preserved without inferring header roles; inspect merged cells, labels and visual grouping in the original'))
    return slides, sorted(notes), len(prs.slides), None

# ---------------------------------------------------------------- pdf / docx

def from_pdf(path):
    import fitz
    doc = fitz.open(path)
    slides, notes = [], []
    for i, page in enumerate(doc, 1):
        t = clean(page.get_text())
        slides.append((i, [t] if t else []))
        if not t:
            notes.append((i, 'no extractable text, image-only page'))
        else:
            notes.append((i, 'text extraction does not preserve colors, chart meaning or reliable table associations; inspect the original page'))
    count = len(doc)
    doc.close()
    return slides, notes, count, None

def from_docx(path):
    import docx
    d = docx.Document(path)
    # Preserve paragraph/table order. DOCX has no stable PDF page numbers here.
    from docx.table import Table
    from docx.text.paragraph import Paragraph
    body = []
    for child in d.element.body.iterchildren():
        if child.tag.endswith('}p'):
            text = clean(Paragraph(child, d).text)
            if text: body.append(text)
        elif child.tag.endswith('}tbl'):
            rows = [[clean(c.text) for c in row.cells] for row in Table(child, d).rows]
            if rows:
                body.append('[Table, row order preserved; header status not inferred]')
                body.extend(' | '.join(row) for row in rows)
    return [(1, body)], [(1, 'DOCX logical section, not a rendered page; images, pagination and layout are not assessed')], 1, None

# ---------------------------------------------------------------- output

def selected_pages(spec, count):
    if not spec or spec.lower() == 'all': return list(range(1, count + 1))
    chosen = set()
    for token in spec.split(','):
        m = re.fullmatch(r"(\d+)(?:-(\d+))?", token.strip())
        if not m: raise ValueError('Use page ranges such as 1-12,15,20-24')
        first, last = int(m[1]), int(m[2] or m[1])
        if first < 1 or last < first or last > count: raise ValueError('Selection is outside the source page range')
        chosen.update(range(first, last + 1))
    return sorted(chosen)


def private_output(filename):
    repo = Path(subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], cwd=Path(__file__).resolve().parent, text=True).strip())
    root = (repo / '_client-private').resolve()
    target = Path(filename).resolve()
    if not target.is_relative_to(root) or target == root:
        raise ValueError('Output must be inside the repository ignored _client-private area')
    subprocess.run(['git', '-c', 'safe.directory=' + repo.as_posix(), 'check-ignore', '--quiet', '--', str(target)], cwd=repo, check=True)
    target.parent.mkdir(parents=True, exist_ok=True)
    return target


def run(path, out, selection='all', include_notes=False, preview=None, evidence_json=None):
    # Check every requested destination before writing any client content.
    for destination in (out, preview, evidence_json):
        if destination: private_output(destination)
    ext = Path(path).suffix.lower()
    unit = 'Slide' if ext == '.pptx' else ('Page' if ext == '.pdf' else 'Section')
    fn = {'.pptx': from_pptx, '.pdf': from_pdf, '.docx': from_docx}.get(ext)
    if not fn: raise ValueError('Use .pptx, .pdf or .docx')
    slides, notes, count, _ = fn(path, include_notes) if ext == '.pptx' else fn(path)
    chosen = selected_pages(selection, count)
    slides = [(i, body) for i, body in slides if i in chosen]
    notes = [(i, msg) for i, msg in notes if i in chosen]
    excluded = [i for i in range(1, count + 1) if i not in chosen]
    lines = [f'DELIVERABLE TEXT (original {unit.lower()} numbers preserved):', '']
    for i, body in slides:
        lines += [f'**{unit} {i}**', *(body or ['(no extractable text)']), '']
    lines += ['## Extraction notes (not part of the deliverable)', '',
        f'- Source: {Path(path).name}, {count} {unit.lower()}s.',
        f'- Included: {fmt(chosen)}.', f'- Excluded: {fmt(excluded) or "none"}. Do not diagnose absent evidence from excluded material.',
        '- Original files are authoritative. Text is a working aid; inspect original pages before findings.',
        '- Speaker notes: ' + ('included when present.' if include_notes else 'excluded.')]
    lines += [f'- {unit} {i}: {msg}.' for i, msg in notes]
    text = '\n'.join(lines) + '\n'
    print('Local extraction only. Not anonymized: inspect names, logos, personal data and unpublished figures before any authorized sharing.', file=sys.stderr)
    if out:
        private_output(out).write_text(text, encoding='utf-8')
        print(f'Wrote selected content: {len(chosen)} of {count} {unit.lower()}s.')
    else: sys.stdout.write(text)
    if evidence_json:
        evidence = {'source': str(Path(path).resolve()), 'sha256': hashlib.sha256(Path(path).read_bytes()).hexdigest(),
            'pageCount': count, 'unit': unit.lower(), 'included': chosen, 'excluded': excluded,
            'pages': [{'pdf_page': i, 'text': '\n'.join(body)} for i, body in slides],
            'notes': [{'page': i, 'message': msg} for i, msg in notes]}
        private_output(evidence_json).write_text(json.dumps(evidence, ensure_ascii=False, indent=2), encoding='utf-8')
    if preview:
        target = private_output(preview)
        images = {}
        if ext == '.pdf':
            import fitz
            with fitz.open(path) as doc:
                for n in chosen:
                    filename = private_output(target.parent / (target.stem + '-pages') / f'page-{n:04}.png')
                    page = doc[n-1]
                    page.get_pixmap(matrix=fitz.Matrix(1.2, 1.2), alpha=False).save(filename)
                    images[n] = filename.relative_to(target.parent).as_posix()
        blocks = []
        for i, body in slides:
            image = f'<img src="{html.escape(images[i], quote=True)}" alt="Original PDF page {i}">' if i in images else '<p>Inspect the original document for images and layout.</p>'
            blocks.append(f'<section><h2>{unit} {i}</h2>{image}<pre>{html.escape(chr(10).join(body))}</pre></section>')
        content = '<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width"><title>Local intake preview</title><style>body{font:16px system-ui;max-width:1000px;margin:30px auto;padding:20px;color:#14180f}img{max-width:100%;border:1px solid #ddd}pre{white-space:pre-wrap;overflow-wrap:anywhere;background:#f3f8ec;padding:20px}section{border-top:2px solid #78b038;margin-top:30px}p{line-height:1.6}</style><h1>Selected content preview</h1><p>Review the original page alongside the exact selected text. No uploads. Not anonymized.</p>'
        content += '<p>Included: ' + fmt(chosen) + '. Excluded: ' + (fmt(excluded) or 'none') + '.</p>'
        content += ''.join(blocks) + '<h2>Exact paste payload</h2><pre>' + html.escape(text) + '</pre></html>'
        target.write_text(content, encoding='utf-8')
        print('Wrote local preview with original PDF page images where applicable.')


def fmt(xs):
    return ', '.join(str(x) for x in xs)

def plural(unit, xs):
    return unit if len(xs) == 1 else unit + 's'

if __name__ == '__main__':
    ap = argparse.ArgumentParser(description='Turn a deliverable into the block you paste '
                                             'into the reviewer, with extraction notes.')
    ap.add_argument('deck')
    ap.add_argument('-o', '--out', default=None)
    ap.add_argument('--pages', default='all', help='Original page/slide numbers: all or 1-12,15,20-24')
    ap.add_argument('--include-speaker-notes', action='store_true')
    ap.add_argument('--preview', help='Ignored local HTML preview path')
    ap.add_argument('--evidence-json', help='Ignored page-marked evidence JSON path')
    a = ap.parse_args()
    try:
        run(a.deck, a.out, a.pages, a.include_speaker_notes, a.preview, a.evidence_json)
    except (ValueError, subprocess.CalledProcessError) as error:
        ap.error(str(error))
