#!/usr/bin/env python3
"""PROTOTYPE -- throwaway. Ticket 26's register run.

Measures whether a model can hold the rewritten finding register that the owner approved
on 2026-09-20, and whether lead mode stays untouched by it.

Arms:
  student-attempt r1..r3  deep mode, a real attempt given -> REVIEW in the new shape
  lead-nothing    r1..r2  lead mode                       -> REVIEW in the OLD dense shape

Three student repeats because the thing being measured is a *register*, and one sample of a
register says nothing. Lead is the no-bleed control: the owner ruled the new shape binds on
short and deep only, so lead output must come back looking like 2026-09-20's.

Bundles are generated from the shipped sources through build-bundle.js, not hand-assembled.
Same deck, same attempt text and the same key discipline as ticket 20, so the only thing
that differs between this run and that one is the template.
"""
import json
import pathlib
import subprocess
import sys

import tiktoken

V2 = pathlib.Path(r'C:\Users\User\Desktop\180dc-ai\tools\quality-reviewer\v2')
HERE = pathlib.Path(__file__).parent
OUT = HERE / 'bundles'
OUT.mkdir(exist_ok=True)
ENC = tiktoken.get_encoding('cl100k_base')

KEY1, KEY2 = '0924-WITHDRAW', 'OMEGA-9X'
DRIVE = 'https://drive.google.com/drive/folders/EXAMPLE-REGISTER-RUN'

NODE = r"""
const b = require(%s);
const s = b.sources();
const keys = {k1: %s, k2: %s};
process.stdout.write(JSON.stringify({
  p1: b.fill(s.p1, keys, %s),
  p2: b.fill(s.p2, keys, %s),
  p3: b.fill(s.p3, keys, %s),
}));
""" % (json.dumps(str(V2 / 'build-bundle.js')), json.dumps(KEY1), json.dumps(KEY2),
       json.dumps(DRIVE), json.dumps(DRIVE), json.dumps(DRIVE))

src = json.loads(subprocess.run(['node', '-e', NODE], capture_output=True, text=True,
                                check=True).stdout)
P1, P2, P3T = src['p1'], src['p2'], src['p3']

DECK = (V2 / 'TEST-KIT' / 'PASTE-3-deck-A.md').read_text(encoding='utf-8')
GATE_BLOCK = P3T.split('MODE: short | deep | lead')[0]


def paste3(mode, attempt_in_template=None):
    body = DECK
    if mode != 'deep':
        body = body.replace('MODE: deep', 'MODE: ' + mode, 1)
    out = GATE_BLOCK + body
    if attempt_in_template:
        out = out.rstrip('\n') + '\n\nYOUR OWN READ:\n' + attempt_in_template + '\n'
    return out


# Byte-identical to ticket 20's attempt, so the two runs are comparable.
ATTEMPT = ("My own read first: I think the weakest part is that we never say what the "
           "client should actually do on Monday morning. We describe the market well but "
           "the recommendation stays abstract, and I suspect our membership numbers are "
           "pulled from one source we never name.")

GO = '\nReview this deliverable now, in your specified format.\n'

ARMS = {
    'student-attempt-r1': [P1, P2, paste3('deep', ATTEMPT)],
    'student-attempt-r2': [P1, P2, paste3('deep', ATTEMPT)],
    'student-attempt-r3': [P1, P2, paste3('deep', ATTEMPT)],
    'lead-nothing-r1':    [P1, P2, paste3('lead')],
    'lead-nothing-r2':    [P1, P2, paste3('lead')],
}


def main():
    man = {'keys': {'part1': KEY1, 'part2': KEY2}, 'arms': {}}
    for name, parts in ARMS.items():
        text = '\n\n'.join(parts) + GO
        (OUT / (name + '.txt')).write_text(text, encoding='utf-8')
        man['arms'][name] = {
            'chars': len(text),
            'tokens': len(ENC.encode(text)),
            'has_key1': KEY1 in text,
            'has_key2': KEY2 in text,
            'has_new_template': 'Aim for a line like' in text,
            'has_lead_template': 'Why it costs the client' in text,
            'habit_section_gone': 'THE HABIT TO BUILD' not in text,
        }
    (HERE / 'manifest.json').write_text(json.dumps(man, indent=2), encoding='utf-8')
    print('%-20s %8s %8s  %s' % ('arm', 'chars', 'tokens', 'k1 k2 new lead nohabit'))
    for n, v in man['arms'].items():
        print('%-20s %8d %8d  %-3s %-3s %-4s %-5s %s' % (
            n, v['chars'], v['tokens'], v['has_key1'], v['has_key2'],
            v['has_new_template'], v['has_lead_template'], v['habit_section_gone']))
    return 0


if __name__ == '__main__':
    sys.exit(main())
