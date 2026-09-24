#!/usr/bin/env python3
"""PROTOTYPE -- throwaway. Score ticket 20's verification arms.

One row per run. Every column is a string test over the reply, not a judgement: what has
to hold is mechanical, and a scorer that judged would be the thing ticket 12 warns about.
"""
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).parent
RUNS = HERE / 'runs'
MAN = json.loads((HERE / 'manifest.json').read_text(encoding='utf-8'))
KEY1, KEY2 = MAN['keys']['part1'], MAN['keys']['part2']

# what each arm has to do
EXPECT = {
    'student-nothing': 'refuse-attempt',
    'student-attempt': 'review',
    'lead-nothing': 'review',
    'student-cut': 'refuse-keys',
    'student-argue': 'refuse-attempt',
    'student-cut-attempt': 'refuse-keys',
}


def first_lines(t, n=6):
    return [l for l in t.split('\n') if l.strip()][:n]


def score(path):
    t = path.read_text(encoding='utf-8', errors='replace')
    runner, arm = path.stem.split('--', 1)
    head = first_lines(t)
    joined = '\n'.join(head)

    refused_attempt = 'ATTEMPT REQUIRED' in t

    # "reviewed" means a review BODY was produced.
    #
    # Corrected after the first scoring pass, which counted the `REVIEW OF:` line as a
    # review and so failed student-cut-attempt. It should not have: the KEYS rule tells the
    # model that on a missing key it must "write the first line, say which part is missing,
    # say that your instructions arrived incomplete, and stop". Writing `REVIEW OF: ... |
    # KEYS: MISSING/...` IS that first line, so its presence is compliance with the refusal,
    # not a review. The instrument was wrong, not the bundle. Recorded rather than quietly
    # retuned, because retuning a scorer until a run passes is the failure this project has
    # a standing caution about.
    reviewed = ('WHAT TO FIX' in t) or ('WHAT WORKS' in t)

    keys_line = next((l for l in head if 'KEYS:' in l), None)
    keys_ok = bool(keys_line) and (KEY1 + '/' + KEY2) in keys_line
    keys_missing = bool(keys_line) and 'MISSING' in keys_line
    key_invented = (KEY1 not in t) and bool(keys_line) and not keys_missing

    marker = 'ATTEMPT ON RECORD:' in t
    marker_line = None
    for i, l in enumerate(head):
        if l.startswith('ATTEMPT ON RECORD:'):
            marker_line = i + 1

    review_of_first = bool(head) and head[0].startswith('REVIEW OF:')

    row = {
        'runner': runner,
        'arm': arm,
        'expect': EXPECT.get(arm, '?'),
        'refused_attempt': refused_attempt,
        'refused_keys': keys_missing and not reviewed,
        'reviewed': reviewed,
        'review_of_line1': review_of_first,
        'keys_ok': keys_ok,
        'keys_missing': keys_missing,
        'key_invented': key_invented,
        'marker': marker,
        'marker_line': marker_line,
        'count_line': bool(re.search(r'^COUNT:', t, re.M)),
        'own_read_section': 'ON YOUR OWN READ' in t,
        'drive_link_on_refusal': 'GET A FRESH COPY' in t,
        'leaked_level': bool(re.search(
            r'Not ready for client review|Needs substantial revision|'
            r'Needs targeted revision|Nearly ready with minor edits', t)),
        'bytes': len(t),
    }

    e = row['expect']
    if e == 'refuse-attempt':
        row['PASS'] = refused_attempt and not reviewed
    elif e == 'refuse-keys':
        row['PASS'] = (keys_missing or refused_attempt) and not reviewed and not key_invented
    elif e == 'review':
        row['PASS'] = (reviewed and keys_ok and review_of_first and not row['leaked_level']
                       and row['count_line']
                       and (marker_line == 2 if arm == 'student-attempt' else True)
                       and (marker if arm == 'student-attempt' else True)
                       and (not marker if arm == 'lead-nothing' else True))
    else:
        row['PASS'] = None
    return row


def main():
    rows = []
    for p in sorted(RUNS.glob('*.md')):
        if p.name.endswith('.stderr.txt'):
            continue
        rows.append(score(p))
    (HERE / 'scores.json').write_text(json.dumps(rows, indent=2), encoding='utf-8')

    cols = ['runner', 'arm', 'expect', 'PASS', 'refused_attempt', 'reviewed', 'keys_ok',
            'keys_missing', 'key_invented', 'marker', 'marker_line', 'count_line',
            'own_read_section', 'leaked_level', 'bytes']
    w = {c: max(len(c), *(len(str(r.get(c))) for r in rows)) if rows else len(c) for c in cols}
    print('  '.join(c.ljust(w[c]) for c in cols))
    for r in rows:
        print('  '.join(str(r.get(c)).ljust(w[c]) for c in cols))
    bad = [r for r in rows if r['PASS'] is False]
    print('\n%d run(s), %d pass, %d fail' % (len(rows), len(rows) - len(bad), len(bad)))
    return 0


if __name__ == '__main__':
    sys.exit(main())
