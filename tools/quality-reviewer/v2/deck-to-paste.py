# deck-to-paste.py -- turn a real deliverable into the block you paste into the reviewer.
#
#   python deck-to-paste.py <deck.pptx|deck.pdf|deck.docx> [-o out.md]
#
# Writes the DELIVERABLE TEXT block, slide-segmented, plus the extraction-notes block the
# reviewer needs. Prints the result to stdout if no -o is given.
#
# WHY THE EXTRACTION NOTES MATTER, and why this is not a nicety.
# The reviewer's comparator test asks, for every figure the recommendation leans on, "compared
# to what". On damaged input it cannot always tell a missing comparator from one the extraction
# destroyed, so it reads the extraction notes and applies one mechanical test to their wording:
# did the note say TEXT was lost, or that the PLACE of text was lost? Only lost TEXT suspends
# the comparator, and only on the slides that note names. So the vocabulary below is not
# decoration. "not recoverable as text" and "flattened" route to opposite behaviours, and a
# deck pasted with no notes at all gives the gate nothing to read.
# See 04-prompt-templates.md section A, step 5, and 25-comparator-gate.md.
#
# WHAT THIS DOES BETTER THAN THE INTAKE SCRIPT (eval-cases-real/intake-work/extract-local.py):
#   - tables keep their header row and bind each value to its column label, instead of being
#     flattened to tab-joined rows. A table whose numbers lose their labels is the exact
#     "disconnected from its label" damage the gate treats as lost PLACE.
#   - charts are read. python-pptx exposes categories and series values, so figures that would
#     otherwise be reported as "no extractable values" come through as real numbers. Chart
#     values are the single most common known gap in this project's real cases, and they are
#     the numbers the comparator test most wants.
#   - the extraction-notes block is generated from what actually happened, in the gate's own
#     vocabulary, rather than written by hand afterwards.
#
# No client text is stored anywhere. It reads one file and writes one file.

import sys, os, re, argparse

def clean(s):
    return re.sub(r'[ \t]+', ' ', (s or '').replace('\r', '').strip())

# ---------------------------------------------------------------- pptx

def from_pptx(path):
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
                # Row 0 is a header only if it plausibly is one: more than one row, and most
                # of its cells filled. Single-row tables and tables whose top row is mostly
                # blank have no header, and binding values to a header that is not there
                # invents labels.
                head = rows[0]
                filled = sum(1 for v in head if v)
                has_header = len(rows) > 1 and filled >= max(2, int(0.6 * len(head)))
                if has_header:
                    body.append('[Table] ' + ' | '.join(head))
                    for r in rows[1:]:
                        pairs = [f'{head[j]}: {v}' if j < len(head) and head[j] else v
                                 for j, v in enumerate(r) if v]
                        if pairs:
                            body.append('  ' + '; '.join(pairs))
                else:
                    body.append('[Table, no header row]')
                    for r in rows:
                        vals = [v for v in r if v]
                        if vals:
                            body.append('  ' + ' | '.join(vals))
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
                        vals = [v for v in s.values if v is not None]
                        if not vals:
                            continue
                        # A chart can carry values with no category names at all: the labels
                        # live in separate text boxes on the slide. Dropping the values in that
                        # case is worse than useless, because it also writes a "values not
                        # recoverable" note, and that note suspends the comparator test on the
                        # one slide whose numbers the reader most needs interrogated.
                        if cats:
                            body_vals = '; '.join(f'{cats[j]}: {v}' for j, v in enumerate(vals)
                                                  if j < len(cats))
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
            n = slide.notes_slide.notes_text_frame.text if slide.has_notes_slide else ''
            if clean(n):
                body.append('[Speaker notes] ' + clean(n))
        except Exception:
            pass

        slides.append((i, body))
        if not had_text:
            notes.append((i, 'image-only, no extractable text on this slide'))
    # A chart we could not read is lost TEXT: its values are not in the input at all, so the
    # comparator test must be suspended on that slide rather than reported as a missing
    # comparator. This is the note the gate keys on.
    for i in sorted(set(chart_unreadable)):
        notes.append((i, 'chart present but its values are not recoverable as text, '
                         'no values at all were extracted'))
    # A table with no header row loses which column each value came from. The values are all
    # present, so this is lost PLACE, not lost TEXT: it must NOT suspend the comparator test.
    for i in sorted(set(unbound)):
        notes.append((i, 'a table here has no header row, so its values are kept as extracted '
                         'and are disconnected from their labels'))
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
    return slides, notes, len(doc), None

def from_docx(path):
    import docx
    d = docx.Document(path)
    body = [clean(p.text) for p in d.paragraphs if clean(p.text)]
    for tb in d.tables:
        rows = [[clean(c.text) for c in r.cells] for r in tb.rows]
        if rows:
            head, rest = rows[0], rows[1:]
            body.append('[Table] ' + ' | '.join(head))
            for r in rest:
                body.append('  ' + '; '.join(
                    f'{head[j]}: {v}' if j < len(head) and head[j] else v
                    for j, v in enumerate(r)))
    return [(1, body)], [], 1, None

# ---------------------------------------------------------------- output

def run(path, out):
    ext = os.path.splitext(path)[1].lower()
    unit = 'Slide' if ext == '.pptx' else ('Page' if ext == '.pdf' else 'Section')
    fn = {'.pptx': from_pptx, '.pdf': from_pdf, '.docx': from_docx}.get(ext)
    if not fn:
        sys.exit(f'unsupported file type {ext}. Use .pptx, .pdf or .docx.')

    slides, notes, count, _ = fn(path)

    # chart-recovery notes, derived from what the body actually contains
    charted = [i for i, b in slides if any(x.startswith('[Chart') for x in b)]
    tabled  = [i for i, b in slides if any(x.startswith('[Table') for x in b)]

    lines = [f'DELIVERABLE TEXT (one block per {unit.lower()}, with numbers):', '']
    for i, body in slides:
        lines.append(f'**{unit} {i}**')
        lines.extend(body if body else ['(no extractable text)'])
        lines.append('')

    lines += ['## Extraction notes (not part of the deliverable)', '',
              f'- Source: {os.path.basename(path)}, {count} {unit.lower()}s, read with '
              f'deck-to-paste.py.']
    if tabled:
        lines.append(f'- {plural(unit, tabled)} {fmt(tabled)}: tables kept as extracted, with '
                     'each value bound to its column label.')
    if charted:
        lines.append(f'- {plural(unit, charted)} {fmt(charted)}: chart values were read from '
                     'the chart data and are bound to their categories.')
    for i, msg in notes:
        lines.append(f'- {unit} {i}: {msg}.')
    if not notes:
        lines.append('- No slide lost text in extraction.')
    lines += ['',
              '<!-- The wording above is load-bearing. The reviewer reads these notes to tell a',
              '     figure whose comparator is genuinely missing from one whose comparator the',
              '     extraction destroyed. Only lost TEXT suspends its comparator test. Do not',
              '     reword these lines. -->']

    text = '\n'.join(lines) + '\n'
    # This tool extracts. It does NOT anonymise, and the extraction carries client names,
    # figures and quotes verbatim. 12-real-deck-intake.md section C is the policy.
    warn = [
        '',
        '  NOT ANONYMISED. This output carries the client name and its numbers verbatim.',
        '  Before pasting it into any AI service: replace the client name throughout, and',
        '  turn off model training on that service. Most consumer free tiers train on what',
        '  you paste unless you say otherwise, and the deliverable belongs to the client.',
        '',
    ]
    print(chr(10).join(warn), file=sys.stderr)
    if out:
        open(out, 'w', encoding='utf-8', newline='\n').write(text)
        print(f'wrote {out}  ({count} {unit.lower()}s, {len(tabled)} with tables, '
              f'{len(charted)} with charts, {len(notes)} flagged)')
    else:
        sys.stdout.write(text)

def fmt(xs):
    return ', '.join(str(x) for x in xs)

def plural(unit, xs):
    return unit if len(xs) == 1 else unit + 's'

if __name__ == '__main__':
    ap = argparse.ArgumentParser(description='Turn a deliverable into the block you paste '
                                             'into the reviewer, with extraction notes.')
    ap.add_argument('deck')
    ap.add_argument('-o', '--out', default=None)
    a = ap.parse_args()
    run(a.deck, a.out)
