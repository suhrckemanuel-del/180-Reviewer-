# PROTOTYPE. Check every quote in review.md against the slide it cites.
#   python check_quotes.py deck.json review.md
# A quote is "..." followed by (slide N) or (page N). Whitespace collapses and curly quotes
# count as straight ones; every other character must match. Exit 0 when nothing is missing.
# PDFs lose their reading order, so on a PDF a quote also passes when it sits in the page's
# joined text, and a quote whose words are all on the page in another order is "check by eye".
# A quote cited as (slide N, image) was read from the picture; the script can't see it.
import json, re, sys

QUOTE = re.compile(r'["“](.+?)["”]\s*\((?:slide|page|p\.)\s*(\d+)(\s*,\s*image)?\)', re.I)


def norm(s):
    s = s.translate(str.maketrans({'‘': "'", '’': "'", '“': '"', '”': '"'}))
    return re.sub(r'\s+', ' ', s).strip()


def words(s):
    return re.findall(r'[0-9a-z]+', s.lower())


def main():
    deck = json.load(open(sys.argv[1], encoding='utf-8'))
    review = open(sys.argv[2], encoding='utf-8').read()
    is_pdf = deck.get('kind') == 'pdf' or deck['file'].lower().endswith('.pdf')
    # each item checked on its own: a quote may not join two bullets or two cells
    slides = {s['n']: [norm(i) for i in s['items']] for s in deck['slides']}
    pages = {n: ' '.join(items) for n, items in slides.items()}
    quotes = QUOTE.findall(review)
    if not quotes:
        print('Quotes not machine-checked: no quotes found in review.md.')
        sys.exit(1)
    ok, eye, image, bad = 0, [], [], []
    for q, n, from_image in quotes:
        q, n = norm(q), int(n)
        if from_image:
            image.append(n)
        elif any(q in item for item in slides.get(n, [])) or (is_pdf and q in pages.get(n, '')):
            ok += 1
        elif is_pdf and set(words(q)) <= set(words(pages.get(n, ''))):
            eye.append(n)
        else:
            elsewhere = [m for m, items in slides.items() if any(q in i for i in items)
                         or (is_pdf and q in pages[m])]
            where = f'found on slide {", ".join(map(str, elsewhere))} instead' if elsewhere \
                else 'not found anywhere in the deck text'
            bad.append(f'  MISSING (slide {n}): "{q[:70]}" -> {where}')
    line = f'**Quotes checked by script: {ok} of {len(quotes)} found on the cited slide.'
    notes = []
    if eye:
        notes.append(f'slide {", ".join(map(str, sorted(set(eye))))} (PDF layout split the text)')
    if image:
        notes.append(f'slide {", ".join(map(str, sorted(set(image))))} (read from the image)')
    if notes:
        line += ' Check by eye: ' + '; '.join(notes) + '.'
    print(line + '**')
    if bad:
        print('\n'.join(bad))
        sys.exit(1)


if __name__ == '__main__':
    main()
