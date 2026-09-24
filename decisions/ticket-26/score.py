#!/usr/bin/env python3
"""PROTOTYPE -- throwaway. Ticket 26's scorer.

Mechanical checks only. Three of the things this ticket cares about -- whether the register
actually reads as plain English, whether the worked example passes the two audit tests, and
whether The problem and Why it matters have collapsed -- are judgement and are read by hand.
What is here is what a string can settle, so the hand-read starts from facts.

The collapse proxy is explicitly a PROXY and is labelled as one in the output: the prompt's
own test is "would this passage still be true with no client, no board and no decision in
it", and the nearest mechanical stand-in is whether such a noun appears at all. A passage
can name the board and still be a restatement. It cannot pass the real test without one.
"""
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).parent
RUNS = HERE / 'runs'
DECK = pathlib.Path(r'C:\Users\User\Desktop\180dc-ai\tools\quality-reviewer\v2'
                    r'\TEST-KIT\PASTE-3-deck-A.md').read_text(encoding='utf-8')
# The deck is hard-wrapped; a quote in a review is one line. Compare on collapsed
# whitespace, or every quote reads as fabricated -- a scorer bug, not a finding.
DECK = ' '.join(DECK.split())

NEW_FIELDS = ['The problem:', 'Why it matters:', 'Do this:', 'Answer first:']
OLD_FIELDS = ['Where:', 'Quote:', 'Why it costs the client:', 'What to do:']
EXAMPLE = 'Aim for a line like:'
READER_NOUNS = ['board', 'client', 'trustee', 'funder', 'coordinator', 'decision',
                'audience', 'reader', 'member']


def sentences(s):
    return [x for x in re.split(r'(?<=[.!?])\s+', s.strip()) if x]


def words(s):
    return len(s.split())


def findings_block(text):
    m = re.search(r'^WHAT TO FIX, IN ORDER\s*$(.*?)^(?:WHAT THIS REVIEW COULD NOT JUDGE|'
                  r'THE HABIT TO BUILD|QUESTIONS WORTH ASKING)', text,
                  re.S | re.M)
    return m.group(1) if m else ''


def split_findings(block):
    parts = re.split(r'^\s*(\d+)\.\s+', block, flags=re.M)
    out = []
    for i in range(1, len(parts) - 1, 2):
        out.append(parts[i + 1])
    return out


def field(f, name):
    """Text of one labelled field, up to the next labelled field or blank-line break."""
    labels = NEW_FIELDS + OLD_FIELDS + [EXAMPLE]
    others = [re.escape(x) for x in labels if x != name]
    m = re.search(re.escape(name) + r'\s*(.*?)(?=' + '|'.join(others) + r'|\Z)', f, re.S)
    return ' '.join(m.group(1).split()) if m else None


def score_student(name, text):
    r = {'arm': name, 'mode': 'student'}
    r['produced_review'] = text.lstrip().startswith('REVIEW OF:')
    r['habit_section_present'] = 'THE HABIT TO BUILD' in text
    blk = findings_block(text)
    fs = split_findings(blk)
    r['n_findings'] = len(fs)
    r['old_fields_leaked'] = sorted({x for x in OLD_FIELDS if x in blk})
    per = []
    for f in fs:
        title = f.split('\n', 1)[0]
        why = field(f, 'Why it matters:')
        prob = field(f, 'The problem:')
        ex = field(f, EXAMPLE)
        d = {
            'title': title.strip(),
            'title_words': words(re.sub(r'\[.*?\]', '', title)),
            'has_all_fields': all(x in f for x in NEW_FIELDS),
            'missing_fields': [x for x in NEW_FIELDS if x not in f],
            'problem_sentences': len(sentences(prob)) if prob else None,
            'problem_words': words(prob) if prob else None,
            'why_sentences': len(sentences(why)) if why else None,
            'why_words': words(why) if why else None,
            'why_names_a_reader': bool(why) and any(
                n in why.lower() for n in READER_NOUNS),
            'has_example': ex is not None,
            'example_disclaimer': bool(ex) and 'shape' in ex.lower(),
            'wrote_none': bool(ex) and ex.strip().lower().startswith('none'),
            'severity': (re.search(r'\[(High impact|Moderate|Minor)\]', f) or [None, None])[1]
            if re.search(r'\[(High impact|Moderate|Minor)\]', f) else None,
        }
        per.append(d)
    r['findings'] = per
    r['severities'] = [d['severity'] for d in per]
    quotes = re.findall(r'"([^"]{25,})"', blk)
    r['quotes_checked'] = len(quotes)
    r['quotes_not_in_deck'] = [q[:60] for q in quotes if ' '.join(q.split()) not in DECK]
    return r


def score_lead(name, text):
    r = {'arm': name, 'mode': 'lead'}
    r['produced_review'] = text.lstrip().startswith('REVIEW OF:')
    r['habit_section_present'] = 'THE HABIT TO BUILD' in text
    blk = findings_block(text)
    r['n_findings'] = len(split_findings(blk))
    r['dense_fields_present'] = sorted({x for x in OLD_FIELDS if x in blk})
    r['new_fields_bled_in'] = sorted({x for x in NEW_FIELDS + [EXAMPLE]
                                      if x in blk and x != 'Answer first:'})
    r['answer_first_present'] = 'Answer first:' in blk
    whys = re.findall(r'Why it costs the client:\s*(.*?)(?=\n\s*What to do:|\Z)', blk, re.S)
    r['why_words'] = [words(' '.join(w.split())) for w in whys]
    quotes = re.findall(r'"([^"]{25,})"', blk)
    r['quotes_checked'] = len(quotes)
    r['quotes_not_in_deck'] = [q[:60] for q in quotes if ' '.join(q.split()) not in DECK]
    r['severities'] = re.findall(r'\[(High impact|Moderate|Minor)\]', blk)
    return r


def main():
    out = []
    for p in sorted(RUNS.glob('haiku--*.md')) + sorted(RUNS.glob('codex--*.md')):
        text = p.read_text(encoding='utf-8')
        name = p.stem
        out.append(score_lead(name, text) if 'lead' in name else score_student(name, text))
    (HERE / 'scores.json').write_text(json.dumps(out, indent=2), encoding='utf-8')

    print('=== STUDENT ARMS: does the register hold ===')
    for r in [x for x in out if x['mode'] == 'student']:
        print('\n%s  review=%s  findings=%d  habit_section=%s  old_fields_leaked=%s'
              % (r['arm'], r['produced_review'], r['n_findings'],
                 r['habit_section_present'], r['old_fields_leaked'] or 'none'))
        print('  quotes %d checked, %d not in deck' %
              (r['quotes_checked'], len(r['quotes_not_in_deck'])))
        for i, d in enumerate(r['findings'], 1):
            print('  %d. [%s] %dw title | problem %ss/%sw | why %ss/%sw names-reader=%s'
                  ' | example=%s disclaimer=%s'
                  % (i, d['severity'], d['title_words'], d['problem_sentences'],
                     d['problem_words'], d['why_sentences'], d['why_words'],
                     d['why_names_a_reader'], d['has_example'], d['example_disclaimer']))
            if d['missing_fields']:
                print('     MISSING: %s' % d['missing_fields'])
            if d['wrote_none']:
                print('     WROTE "none" INSTEAD OF OMITTING')
            print('     title: %s' % d['title'][:100])

    print('\n=== LEAD ARMS: no-bleed control ===')
    for r in [x for x in out if x['mode'] == 'lead']:
        print('\n%s  review=%s  findings=%d  habit_section=%s'
              % (r['arm'], r['produced_review'], r['n_findings'],
                 r['habit_section_present']))
        print('  dense fields present: %s' % (r['dense_fields_present'] or 'NONE'))
        print('  NEW FIELDS BLED IN:   %s' % (r['new_fields_bled_in'] or 'none'))
        print('  why-it-costs word counts: %s' % r['why_words'])
        print('  severities: %s | quotes %d checked, %d not in deck'
              % (r['severities'], r['quotes_checked'], len(r['quotes_not_in_deck'])))

    print('\nNOTE: "names-reader" is a PROXY for the collapse test, not the test. '
          'The real check is read by hand.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
