"""Check that every number in a piece of slide text is one the data produced.

Usage: python check_numbers.py numbers.json "<text>" ["<more text>" ...]
Prints one line per number found: the keys it matches in numbers.json, or MISSING.
Exit code 1 if any number is MISSING. Stdlib only.

A number matches a value when the value, rounded to the number's own decimals, equals it.
"19%" matches 19.04 (percent units) or 0.1904 (a fraction). "1 in 14" matches a rate of 7.1%.
Keys starting with "given_" are numbers the consultant stated; they match and say so.
Dates ("1 Jul", "2025", "Q3", "H1") are skipped. Words like "doubled" or "a third" can't be
checked by value: they're listed as CHECK BY EYE.
"""
import json, re, sys

MONTH = r"(?:jan|feb|mar|apr|may|jun|jul|aug|sep|sept|oct|nov|dec)[a-z]*\.?"
DATES = [
    rf"\b\d{{1,2}}(?:st|nd|rd|th)?\s+{MONTH}(?:\s+\d{{4}})?",
    rf"\b{MONTH}\s+\d{{1,2}}(?:st|nd|rd|th)?\b(?:,?\s+\d{{4}})?",
    r"\b\d{1,2}[/.-]\d{1,2}(?:[/.-]\d{2,4})?\b",
    r"\b[QH][1-4]\b",
    r"\b(?:19|20)\d{2}/\d{2}\b",  # seasons and school years: 2022/23
    r"\b(?:19|20)\d{2}(?:[–-](?:19|20)?\d{2})?\b(?!\s*%)",
]
WORDS = r"\b(half|halved|halving|third|quarter|doubl(?:e|es|ed|ing)|twice|tripl(?:e|es|ed|ing)|majority|most)\b"
NUM = re.compile(
    r"(?<![\w.])(?P<cur>[€$£])?(?P<num>\d{1,3}(?:,\d{3})+(?:\.\d+)?|\d+(?:\.\d+)?)"
    r"(?P<unit>\s?%|\s?percent\b|\s?pp\b|\s?(?:x|×)(?![a-z])|\s+times\b)?",
    re.I)
ONE_IN = re.compile(r"\b1\s+in\s+(\d+)\b", re.I)


def leaves(obj, path=""):
    """Every number in numbers.json with its key (list items as key[i])."""
    if isinstance(obj, bool):
        return
    if isinstance(obj, (int, float)):
        yield path, float(obj)
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            yield from leaves(v, f"{path}[{i}]")
    elif isinstance(obj, dict):
        for k, v in obj.items():
            yield from leaves(v, f"{path}.{k}" if path else k)


def numbers_in(text):
    """[(shown, value, decimals, kind)] for each number in text; kind is pct, one_in, times or plain."""
    t = text
    for d in DATES:
        t = re.sub(d, " ", t, flags=re.I)
    found = []
    for m in ONE_IN.finditer(t):
        found.append((m.group(0), float(m.group(1)), 0, "one_in"))
    t = ONE_IN.sub(" ", t)
    for m in NUM.finditer(t):
        raw = m.group("num")
        val = float(raw.replace(",", ""))
        dec = len(raw.split(".")[1]) if "." in raw else 0
        unit = (m.group("unit") or "").strip().lower()
        kind = "pct" if unit in ("%", "percent", "pp") else "times" if unit in ("x", "×", "times") else "plain"
        found.append((m.group(0).strip(), val, dec, kind))
    words = [w.group(0) for w in re.finditer(WORDS, text, re.I)]
    return found, words


def matches(value, dec, kind, pool):
    hits = []
    for key, v in pool:
        cands = [v]
        if kind == "pct" and 0 <= v <= 1:
            cands.append(v * 100)
        if kind == "one_in":
            cands = [100 / v if v > 1 else 1 / v] if v > 0 else []
            dec = 0
        if any(round(c, dec) == value for c in cands):
            hits.append(key)
    return hits


def check(numbers, texts):
    """Lines of report, and whether everything matched."""
    pool = list(leaves(numbers))
    lines, ok = [], True
    for text in texts:
        found, words = numbers_in(text)
        for shown, value, dec, kind in found:
            hits = matches(value, dec, kind, pool)
            given = [h for h in hits if h.split("[")[0].startswith("given_")]
            if not hits:
                ok = False
                lines.append(f"  {shown:<10} MISSING: not in numbers.json at this rounding")
            elif given and len(given) == len(hits):
                lines.append(f"  {shown:<10} given by you ({given[0]})")
            else:
                hits.sort(key=lambda h: "[" in h)  # summary figures before single list items
                more = f" +{len(hits) - 4} more" if len(hits) > 4 else ""
                lines.append(f"  {shown:<10} = {', '.join(hits[:4])}{more}")
        for w in words:
            lines.append(f"  {w!r:<10} CHECK BY EYE: compute the ratio it claims and compare")
    return lines, ok


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    nums = json.load(open(sys.argv[1], encoding="utf-8"))
    lines, ok = check(nums, sys.argv[2:])
    print("\n".join(lines) if lines else "  no numbers found")
    print("ALL NUMBERS MATCH" if ok else "SOME NUMBERS ARE MISSING: fix the text or compute them")
    sys.exit(0 if ok else 1)
