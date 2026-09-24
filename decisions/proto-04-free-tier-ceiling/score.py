#!/usr/bin/env python3
"""
PROTOTYPE -- throwaway. Ticket 04.

Scores each run using only the reply and the deck, which is the whole point:
the question is whether a half-loaded bundle is detectable by someone holding
the output and nothing else.

Detectors, in the order a reader would hit them:

  BRANCH     which output shape came back. The chat path is only ever supposed
             to produce `prose`. Anything else means paste 2 did not land whole.
  SECTIONS   which of the format's named sections survived.
  QUOTES     every evidence quote checked verbatim against the deck. This is
             the gate the hosted product already enforces.
  READINESS  whether a readiness level reached the output. The chat path exists
             to never produce one; a JSON fallback produces one every time.
  REFUSED    whether the reply declines to review and says why.
"""
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).parent
KIT = pathlib.Path(r"C:\Users\User\Desktop\180dc-ai\tools\quality-reviewer\v2\TEST-KIT")

SECTIONS = [
    "REVIEW OF:", "BEFORE YOU USE THIS", "Confidence in this review:",
    "Weakest areas:", "Effort to close", "WHAT WORKS", "WHAT TO FIX, IN ORDER",
    "THE HABIT TO BUILD", "WHAT THIS REVIEW COULD NOT JUDGE",
    "QUESTIONS WORTH ASKING THE TEAM", "HOW TO CHECK THIS FEEDBACK",
    "=== PASTE-BACK RECORD ===",
]

# The 2C template is a fragment, not a document: it opens with <title> and
# <style>, so looking for a doctype finds nothing. These are its landmarks.
HTML_MARKS = ["<title>", "<style>", 'class="wrap"', 'id="stu"', "const REVIEW"]

Q = "\"\u201c\u201d\u2018\u2019'"


def norm(s):
    return re.sub(r"\s+", " ", s).strip().lower()


def deck_text():
    raw = (KIT / "PASTE-3-deck-A.md").read_text(encoding="utf-8")
    return raw.split("DELIVERABLE TEXT", 1)[-1]


def extract_quotes(out, html):
    """Only the quotes offered as evidence. The paste-back record is dropped
    first: it is JSON field values, not evidence, and scanning it was noise."""
    body = out.split("=== PASTE-BACK RECORD ===", 1)[0]
    if html:
        # the data object the model fills; the template's own CSS is not evidence
        obj = out.split("const REVIEW", 1)[-1].split("</script>", 1)[0]
        return [m.group(1) for m in
                re.finditer(r"\bquotes?\s*:\s*\[?\s*[" + Q + r"]([^" + Q + r"]{8,400})", obj)]
    qs = [m.group(1) for m in
          re.finditer(r"Quote:\s*[" + Q + r"]([^" + Q + r"]{8,400})", body)]
    if not qs:
        qs = [m.group(1) for m in
              re.finditer(r"[" + Q + r"]([^" + Q + r"]{25,400})[" + Q + r"]", body)]
    return qs


def score(path):
    out = pathlib.Path(path).read_text(encoding="utf-8", errors="replace")
    deck = norm(deck_text())

    html = sum(1 for m in HTML_MARKS if m in out) >= 4
    present = [s for s in SECTIONS if s.lower() in out.lower()]

    # Branch, most specific first. `prose` is the only sanctioned shape here.
    if "REVIEW OF:" in out and len(present) >= 8:
        branch = "prose"
    elif html:
        branch = "html"
    elif re.match(r"\s*[\{\[]", out) or re.search(r'"diagnosticMean"|"readiness\w*"', out):
        branch = "JSON-fallback"
    elif len(out) < 2000 and re.search(
            r"incomplete|truncated|cut off|provide the remainder|cannot .{0,40}without",
            out, re.I):
        branch = "REFUSED"
    else:
        branch = "ad-hoc"

    quotes = extract_quotes(out, html)
    verbatim = [q for q in quotes if norm(q) in deck]
    fabricated = [q for q in quotes if norm(q) not in deck]

    # A readiness level that reached the reader. The paste-back record's own
    # readinessCall is null by design, so a null value is not a leak.
    leak = re.search(r'"readiness\w*"\s*:\s*"([^"]+)"', out)

    fixblock = out.split("WHAT TO FIX", 1)[-1].split("THE HABIT TO BUILD", 1)[0]
    findings = len(re.findall(r"^\s*\d+[.)]\s+\S", fixblock, re.M))

    return {
        "arm": pathlib.Path(path).stem.split("--", 1)[1],
        "runner": pathlib.Path(path).stem.split("--")[0],
        "bytes": len(out),
        "branch": branch,
        "sections_present": len(present),
        "sections_total": len(SECTIONS),
        "sections_missing": [s for s in SECTIONS if s.lower() not in out.lower()],
        "findings": findings,
        "quotes": len(quotes),
        "verbatim": len(verbatim),
        "fabricated": len(fabricated),
        "fabricated_samples": fabricated[:3],
        "leaked_readiness": leak.group(1) if leak else None,
    }


def main():
    runs = sorted((HERE / "runs").glob("*.md"))
    if len(sys.argv) > 1:
        runs = [pathlib.Path(p) for p in sys.argv[1:]]
    rows = [score(p) for p in runs if p.stat().st_size > 0]
    (HERE / "scores.json").write_text(json.dumps(rows, indent=2), encoding="utf-8")

    hdr = (f"{'run':<26}{'branch':>15}{'sect':>7}{'quotes ok':>11}"
           f"{'FABRICATED':>12}{'readiness leak':>22}")
    print(hdr)
    print("-" * len(hdr))
    for r in rows:
        print(
            f"{r['runner'] + '/' + r['arm']:<26}{r['branch']:>15}"
            f"{str(r['sections_present']) + '/' + str(r['sections_total']):>7}"
            f"{str(r['verbatim']) + '/' + str(r['quotes']):>11}"
            f"{r['fabricated']:>12}"
            f"{(r['leaked_readiness'] or '-'):>22}"
        )
    print()
    for r in rows:
        if r["fabricated"]:
            print(f"!! {r['runner']}/{r['arm']}: {r['fabricated']} unmatched")
            for s in r["fabricated_samples"]:
                print(f"     {s[:100]}")


if __name__ == "__main__":
    main()
