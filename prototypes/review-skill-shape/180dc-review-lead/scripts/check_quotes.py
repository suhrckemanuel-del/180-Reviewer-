# PROTOTYPE. Check every quote in review.md against the slide it cites.
#   python check_quotes.py deck.json review.md
# A quote is "..." followed by (slide N) or (page N). Whitespace collapses and curly quotes
# count as straight ones; every other character must match. Exit 0 when all pass, 1 otherwise.
import json, re, sys

QUOTE = re.compile(r'["“](.+?)["”]\s*\((?:slide|page|p\.)\s*(\d+)\)', re.I)


def norm(s):
    s = s.translate(str.maketrans({'‘': "'", '’': "'", '“': '"', '”': '"'}))
    return re.sub(r'\s+', ' ', s).strip()


def main():
    deck = json.load(open(sys.argv[1], encoding='utf-8'))
    review = open(sys.argv[2], encoding='utf-8').read()
    # each item checked on its own: a quote may not join two bullets or two cells
    slides = {s['n']: [norm(i) for i in s['items']] for s in deck['slides']}
    quotes = QUOTE.findall(review)
    bad = []
    for q, n in quotes:
        q, n = norm(q), int(n)
        if any(q in item for item in slides.get(n, [])):
            continue
        elsewhere = [m for m, items in slides.items() if any(q in i for i in items)]
        where = f'found on slide {", ".join(map(str, elsewhere))} instead' if elsewhere \
            else 'not found anywhere in the deck text'
        bad.append(f'  MISSING (slide {n}): "{q[:70]}" -> {where}')
    ok = len(quotes) - len(bad)
    if not quotes:
        print('Quotes not machine-checked: no quotes found in review.md.')
        sys.exit(1)
    print(f'**Quotes checked by script: {ok} of {len(quotes)} found on the cited slide.**')
    if bad:
        print('\n'.join(bad))
        sys.exit(1)


if __name__ == '__main__':
    main()
