#!/usr/bin/env python3
"""PROTOTYPE -- throwaway. Isolates the binary change from the template change.

Round 1 Codex = OLD binary (247581e40ee272fb, now deleted) + round-1 template -> example
fired on 6 of 10 findings, all 6 passing both audit tests.
Round 2 Codex = NEW binary (80f78947ad880e6e) + round-2 template -> 0 of 9.

Two variables moved between those runs. This builds the ROUND-1 template against the NEW
binary, so the only difference from round 2 is the template. If the example comes back, the
template change caused the loss. If it stays at zero, the binary did, and round 1's Codex
result is not reproducible on any instrument that still exists.

Paste 1 and paste 3 come from the live generator; only paste 2 is swapped for the saved
round-1 copy.
"""
import json
import pathlib
import subprocess
import sys

import tiktoken

V2 = pathlib.Path(r'C:\Users\User\Desktop\180dc-ai\tools\quality-reviewer\v2')
HERE = pathlib.Path(__file__).parent
OUT = HERE / 'bundles-v1'
OUT.mkdir(exist_ok=True)
ENC = tiktoken.get_encoding('cl100k_base')

V1_PASTE2 = pathlib.Path(
    r'C:\Users\User\AppData\Local\Temp\claude\C--Users-User-Desktop-180dc-ai'
    r'\92913c02-a456-4235-a95c-c27666371b31\scratchpad\CHAT-CONTEXT.v1.md')

KEY1, KEY2 = '0924-V1RECHECK', 'OMEGA-9V'
DRIVE = 'https://drive.google.com/drive/folders/EXAMPLE-V1-RECHECK'

NODE = r"""
const b = require(%s);
const s = b.sources();
const fs = require('fs');
const keys = {k1: %s, k2: %s};
const v1p2 = fs.readFileSync(%s, 'utf8').replace(/\r\n/g, '\n');
process.stdout.write(JSON.stringify({
  p1: b.fill(s.p1, keys, %s),
  p2: b.fill(v1p2, keys, %s),
  p3: b.fill(s.p3, keys, %s),
}));
""" % (json.dumps(str(V2 / 'build-bundle.js')), json.dumps(KEY1), json.dumps(KEY2),
       json.dumps(str(V1_PASTE2)), json.dumps(DRIVE), json.dumps(DRIVE), json.dumps(DRIVE))

src = json.loads(subprocess.run(['node', '-e', NODE], capture_output=True, text=True,
                                check=True).stdout)
P1, P2, P3T = src['p1'], src['p2'], src['p3']

DECK = (V2 / 'TEST-KIT' / 'PASTE-3-deck-A.md').read_text(encoding='utf-8')
GATE_BLOCK = P3T.split('MODE: short | deep | lead')[0]

ATTEMPT = ("My own read first: I think the weakest part is that we never say what the "
           "client should actually do on Monday morning. We describe the market well but "
           "the recommendation stays abstract, and I suspect our membership numbers are "
           "pulled from one source we never name.")
GO = '\nReview this deliverable now, in your specified format.\n'

p3 = GATE_BLOCK + DECK.rstrip('\n') + '\n\nYOUR OWN READ:\n' + ATTEMPT + '\n'

ARMS = {'v1-student-attempt-r%d' % i: [P1, P2, p3] for i in (1, 2, 3)}


def main():
    assert 'Strike out the invented' in P2, 'paste 2 is not the round-1 template'
    assert 'THE HABIT TO BUILD' not in P2, 'unexpected habit section in round-1 paste 2'
    man = {'keys': {'part1': KEY1, 'part2': KEY2}, 'template': 'round-1', 'arms': {}}
    for name, parts in ARMS.items():
        text = '\n\n'.join(parts) + GO
        (OUT / (name + '.txt')).write_text(text, encoding='utf-8')
        man['arms'][name] = {'chars': len(text), 'tokens': len(ENC.encode(text))}
    (HERE / 'manifest-v1.json').write_text(json.dumps(man, indent=2), encoding='utf-8')
    for n, v in man['arms'].items():
        print('%-24s %8d chars %8d tokens' % (n, v['chars'], v['tokens']))
    print('paste 2 is the ROUND-1 template (audit-test wording present)')
    return 0


if __name__ == '__main__':
    sys.exit(main())
