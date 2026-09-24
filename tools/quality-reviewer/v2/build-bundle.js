#!/usr/bin/env node
/* build-bundle.js -- the only thing allowed to produce a pasteable reviewer bundle.
 *
 * Ticket 20 Group F item 3, from ticket 09. It exists because two hand-maintained
 * derivatives went stale undetected: TEST-KIT/PASTE-SETUP-combined.md sat three months
 * carrying a superseded prompt, and paste 2 drifted from paste 1 independently. One
 * generator, one check, no hand-edited derivatives.
 *
 *   node build-bundle.js --release                    mint a key pair and write a release
 *   node build-bundle.js --check                      fail on any drift (joins check-docs.js)
 *   node build-bundle.js --sync-test-kit              regenerate the TEST-KIT pastes
 *   node build-bundle.js --verify-drive <file> --release <key1>
 *
 * Sources are hand-edited; everything under releases/ and TEST-KIT/PASTE-* is generated.
 * Fix a source and rebuild; never edit a generated file.
 */
'use strict';
const fs = require('fs');
const path = require('path');
const crypto = require('crypto');

const V = __dirname;
const REL = path.join(V, 'releases');

/* ===================================================================== SWITCHES
 * THE AUDIENCE SWITCH. This is the one place the attempt gate's audience is set.
 *
 * 'students'  -- students type a read before the review; team leads go straight through.
 *                This is the default and it is the chapter's ruling of 2026-09-20.
 * 'everyone'  -- nobody is exempt.
 *
 * Flipping this is a one-line edit followed by --release. Both copies of the gate (the
 * system prompt and the team input template) are generated from it, so they cannot
 * disagree. It is NOT a free switch: ticket 21's "refused 16 of 16" was measured on an
 * unconditional gate, and the branched gate had to be re-measured separately. A flip is
 * a different prompt again and needs its own run before it ships. See 29-handover.md 5.5.
 */
const ATTEMPT_GATE_AUDIENCE = 'students';

/* The Google Drive folder the refusal message points a student at. One fixed folder,
 * "anyone with the link -- viewer", and the link must never change: it is baked into
 * bundles already in people's hands. Set it once, here. --release refuses while it is
 * null, because a release that cannot tell a student where to get a fresh copy is a dead
 * end at the one moment the tool has already failed them. */
const DRIVE_FOLDER_URL = null;

/* The prompt version these sources are. The single source of truth: --check asserts that
 * paste 2's record stamp and every generated artifact agree with it. */
const PROMPT_VERSION = 'frozen-2026-09-19';
/* ============================================================================ */

const GATE_AUDIENCE = {
  students:
    'WHO IT APPLIES TO: MODE short and MODE deep. It does NOT apply to MODE lead.\n' +
    'Set by ATTEMPT_GATE_AUDIENCE in build-bundle.js. Default: students.',
  everyone:
    'WHO IT APPLIES TO: every mode, including MODE lead. Nobody is exempt.\n' +
    'Set by ATTEMPT_GATE_AUDIENCE in build-bundle.js. Default: students.',
};

const TEST_KEYS = { k1: '0000-TESTKIT', k2: 'TESTKIT-00' };
const TEST_DRIVE = '(test build -- no Drive folder; see 30-publishing.md)';

// ---- sources ---------------------------------------------------------------

/* Sources are CRLF in this repo. Everything generated here is LF, and every comparison
 * normalises first, so a checkout with different line endings cannot fail --check or
 * --verify-drive for a reason that has nothing to do with the bundle. */
function lf(s) { return s.split('\r\n').join('\n'); }
function read(f) { return lf(fs.readFileSync(path.join(V, f), 'utf8')); }

/* Pull one fenced block out of 04-prompt-templates.md by its section heading. The
 * headings and the fences are document furniture, not prompt text, so they are stripped
 * exactly as a person copying the block would strip them. */
function section(md, heading) {
  const i = md.indexOf(heading);
  if (i === -1) throw new Error('section not found: ' + heading);
  const open = md.indexOf('\n```\n', i);
  if (open === -1) throw new Error('no fence under: ' + heading);
  const start = open + 5;
  const close = md.indexOf('\n```', start);
  if (close === -1) throw new Error('unclosed fence under: ' + heading);
  return md.slice(start, close).replace(/\s+$/, '') + '\n';
}

function sources() {
  const tpl = read('04-prompt-templates.md');
  return {
    p1: section(tpl, '## A. System prompt'),
    p2: read('CHAT-CONTEXT.md'),
    p3: section(tpl, '## B. Team input template'),
  };
}

function fill(text, keys, drive) {
  const audience = GATE_AUDIENCE[ATTEMPT_GATE_AUDIENCE];
  if (!audience) throw new Error('ATTEMPT_GATE_AUDIENCE must be students or everyone');
  const out = text
    .split('<<GATE_AUDIENCE>>').join(audience)
    .split('<<BUNDLE_KEY_1>>').join(keys.k1)
    .split('<<BUNDLE_KEY_2>>').join(keys.k2)
    .split('<<DRIVE_FOLDER_URL>>').join(drive);
  const left = out.match(/<<[A-Z_]+>>/g);
  if (left) throw new Error('unsubstituted placeholders: ' + [...new Set(left)].join(', '));
  return out;
}

// ---- generated artifacts ---------------------------------------------------

function setupFile(src, keys, drive) {
  return [
    'REVIEWER SETUP -- paste this whole document as one message.',
    'Generated by build-bundle.js. Do not edit this file; edit its sources and rebuild.',
    'Release ' + keys.k1 + '/' + keys.k2 + ', prompt ' + PROMPT_VERSION + '.',
    '',
    '===== PART 1 OF 2: THE SYSTEM PROMPT =====',
    '',
    fill(src.p1, keys, drive),
    '',
    '===== PART 2 OF 2: THE CONTEXT PACK =====',
    '',
    fill(src.p2, keys, drive),
  ].join('\n');
}

function teamInput(src, keys, drive) { return fill(src.p3, keys, drive); }

function coverSheet(keys, drive) {
  // Ticket 09 item 4. Four items, in this order. Item 2's wording is load-bearing and is
  // Group D item 6 verbatim: "exactly this string", never "look for the word MISSING",
  // because models have written <missing>, "part 2 missing" and "part 2 not provided".
  return '# The AI Quality Reviewer -- start here\n' +
'\n' +
'Release **' + keys.k1 + '/' + keys.k2 + '**. One page. Read it before you paste anything.\n' +
'\n' +
'## 1. What to do\n' +
'\n' +
'Paste **REVIEWER-SETUP.txt** into a new chat as one message. Then paste your deliverable.\n' +
'Then type your own read of it: what you think its weakest part is, in your own words. Two\n' +
'or three sentences is enough, and nothing is grading it.\n' +
'\n' +
'## 2. Check the first line of what comes back\n' +
'\n' +
'**The first line of your review must read exactly `KEYS: ' + keys.k1 + '/' + keys.k2 + '`.\n' +
'Anything else means part of the setup did not arrive: start a new chat and paste it\n' +
'again.**\n' +
'\n' +
'It is a one-paste fix, not a broken tool. Chat windows silently drop part of a long paste\n' +
'when they run out of room, and nothing announces it. This line is how you see it.\n' +
'\n' +
'## 3. Where to get a fresh copy\n' +
'\n' +
drive + '\n' +
'\n' +
'## 4. What this does not do\n' +
'\n' +
'It does not approve anything and it does not give you a grade. There is no score, no\n' +
'readiness level and no overall verdict, on purpose: the same deliverable was given two\n' +
'different verdicts on identical input, so that half is not produced at all. You get the\n' +
'findings, each one quoted from your own work, and you make the call.\n' +
'\n' +
'A named human signs off on client work. That does not move.\n';
}

function manifest(src, files, keys) {
  const sha = s => crypto.createHash('sha256').update(s, 'utf8').digest('hex');
  const srcFiles = ['04-prompt-templates.md', 'CHAT-CONTEXT.md'];
  const m = {
    keys: { part1: keys.k1, part2: keys.k2 },
    generatedAt: new Date().toISOString(),
    promptVersion: PROMPT_VERSION,
    attemptGateAudience: ATTEMPT_GATE_AUDIENCE,
    sources: {},
    files: {},
  };
  for (const f of srcFiles) {
    const body = read(f);
    m.sources[f] = { bytes: Buffer.byteLength(body, 'utf8'), sha256: sha(body) };
  }
  for (const name of Object.keys(files)) {
    const body = files[name];
    m.files[name] = { bytes: Buffer.byteLength(body, 'utf8'), chars: body.length, sha256: sha(body) };
  }
  return m;
}

function buildRelease(keys, drive) {
  const src = sources();
  const files = {
    'REVIEWER-SETUP.txt': setupFile(src, keys, drive),
    'TEAM-INPUT-TEMPLATE.txt': teamInput(src, keys, drive),
    'COVER-SHEET.md': coverSheet(keys, drive),
  };
  files['MANIFEST.json'] = JSON.stringify(manifest(src, files, keys), null, 2) + '\n';
  return files;
}

// ---- keys ------------------------------------------------------------------

/* Part 1 is MMDD-XXXXXXX: a release date, a hyphen, a random chunk. The date prefix is a
 * convenience for a lead reading an old record and is NOT authoritative -- REGISTER.md
 * is. Anything that parses the prefix as a version rather than looking the key up is a
 * bug. Part 2 stays meaningless: it is an end-of-bundle canary and there is no reason to
 * make it readable. The readable part-1 variant was measured at 0 inventions and 0 date
 * drift over 11 runs (proto-12-selfcheck/RESULTS-B3.md). Ambiguous glyphs are out of the
 * alphabet because these are copied by hand and compared by eye. */
const ALPHABET = 'ABCDEFGHJKLMNPQRSTUVWXYZ23456789';
function chunk(n) {
  const b = crypto.randomBytes(n);
  let s = '';
  for (let i = 0; i < n; i++) s += ALPHABET[b[i] % ALPHABET.length];
  return s;
}
function mintKeys(now) {
  const d = now || new Date();
  const mmdd = String(d.getMonth() + 1).padStart(2, '0') + String(d.getDate()).padStart(2, '0');
  return { k1: mmdd + '-' + chunk(7), k2: chunk(5) + '-' + chunk(2) };
}

// ---- the register ----------------------------------------------------------

const REGISTER = path.join(REL, 'REGISTER.md');
const REGISTER_HEAD = '# Release register\n' +
'\n' +
'**This file is the authority on what a key means, not the date inside the key.** A review\n' +
'arrives stamped with a key pair on its first line; look it up here. Comparisons are always\n' +
'within a key, never across: a record stamped with a retired key is evidence about the\n' +
'version that produced it and about no other.\n' +
'\n' +
'Rows are appended by `build-bundle.js --release` and are never edited or deleted. A key\n' +
'that is not in this table means a hand-edited bundle or a mistyped key: quarantine the\n' +
'record, do not pool it.\n' +
'\n' +
'| key pair | released | prompt version | gate audience | what changed |\n' +
'|---|---|---|---|---|\n';

function appendRegister(keys, note) {
  fs.mkdirSync(REL, { recursive: true });
  if (!fs.existsSync(REGISTER)) fs.writeFileSync(REGISTER, REGISTER_HEAD, 'utf8');
  const row = '| `' + keys.k1 + '/' + keys.k2 + '` | ' + new Date().toISOString().slice(0, 10) +
    ' | ' + PROMPT_VERSION + ' | ' + ATTEMPT_GATE_AUDIENCE + ' | ' + (note || 'not stated') + ' |\n';
  fs.appendFileSync(REGISTER, row, 'utf8');
}

function registerKeys() {
  if (!fs.existsSync(REGISTER)) return [];
  return fs.readFileSync(REGISTER, 'utf8').split('\n')
    .map(function (l) { return l.match(/^\|\s*`([^`\/]+)\/([^`]+)`\s*\|/); })
    .filter(Boolean).map(function (m) { return { k1: m[1], k2: m[2] }; });
}

function releaseDirs() {
  if (!fs.existsSync(REL)) return [];
  return fs.readdirSync(REL).filter(function (d) {
    return fs.statSync(path.join(REL, d)).isDirectory() && d !== 'archive';
  });
}

// ---- commands --------------------------------------------------------------

function cmdRelease(note) {
  if (!DRIVE_FOLDER_URL) {
    console.error('REFUSED: DRIVE_FOLDER_URL is not set in build-bundle.js.\n' +
      '\n' +
      'The refusal the reviewer shows a student whose paste was cut names this folder and\n' +
      'tells them to paste again. A release without it hands a student a dead end at the\n' +
      'one moment the tool has already failed them. Create the folder (one fixed folder,\n' +
      '"anyone with the link -- viewer"), set the constant, and rerun. The link must never\n' +
      'change afterwards: it is baked into every bundle issued. 30-publishing.md section 3.');
    return 1;
  }
  const keys = mintKeys();
  if (releaseDirs().indexOf(keys.k1) !== -1 || registerKeys().some(function (k) { return k.k1 === keys.k1; })) {
    console.error('REFUSED: key ' + keys.k1 + ' already exists. Rerun to mint another.');
    return 1;
  }
  const files = buildRelease(keys, DRIVE_FOLDER_URL);
  const dir = path.join(REL, keys.k1);
  fs.mkdirSync(dir, { recursive: true });
  Object.keys(files).forEach(function (name) { fs.writeFileSync(path.join(dir, name), files[name], 'utf8'); });
  appendRegister(keys, note);
  console.log('released ' + keys.k1 + '/' + keys.k2 + '  ->  releases/' + keys.k1 + '/');
  Object.keys(files).forEach(function (name) {
    console.log('  ' + name + '  ' + files[name].length + ' chars');
  });
  console.log('\nNot published yet. 30-publishing.md sections 2 to 4. The publish is not finished\n' +
    'until --verify-drive prints IDENTICAL.');
  return 0;
}

function testKitFiles() {
  const src = sources();
  return {
    'TEST-KIT/PASTE-1-system-prompt.txt': fill(src.p1, TEST_KEYS, TEST_DRIVE),
    'TEST-KIT/PASTE-2A-chat-path.md': fill(src.p2, TEST_KEYS, TEST_DRIVE),
    'TEST-KIT/PASTE-3-team-input-template.txt': fill(src.p3, TEST_KEYS, TEST_DRIVE),
  };
}

function cmdSyncTestKit() {
  const out = testKitFiles();
  Object.keys(out).forEach(function (f) {
    fs.writeFileSync(path.join(V, f), out[f], 'utf8');
    console.log('wrote ' + f + '  ' + out[f].length + ' chars');
  });
  return 0;
}

function cmdCheck() {
  const fail = [];

  // 1. the TEST-KIT pastes are generated, not hand-maintained
  const want = testKitFiles();
  Object.keys(want).forEach(function (f) {
    const p = path.join(V, f);
    if (!fs.existsSync(p)) fail.push(f + ' is missing; run --sync-test-kit');
    else if (lf(fs.readFileSync(p, 'utf8')) !== want[f]) fail.push(f + ' differs from a fresh generate; run --sync-test-kit');
  });

  // 2. the stale hand-maintained combined build must be gone
  if (fs.existsSync(path.join(V, 'TEST-KIT/PASTE-SETUP-combined.md'))) {
    fail.push('TEST-KIT/PASTE-SETUP-combined.md exists. It was hand-maintained and three ' +
      'months stale; the release bundle replaces it. Delete it.');
  }

  // 3. paste 2's record stamp agrees with PROMPT_VERSION
  const m = read('CHAT-CONTEXT.md').match(/"promptVersion":\s*"([^"]+)"/);
  const stamp = m ? m[1] : null;
  if (stamp !== PROMPT_VERSION) {
    fail.push('CHAT-CONTEXT.md stamps promptVersion "' + stamp + '" but build-bundle.js says "' +
      PROMPT_VERSION + '". Every record a pilot produced would name the wrong prompt.');
  }

  // 4. every release agrees with the register, with itself, and with its sources
  const rk = registerKeys();
  const curSha = crypto.createHash('sha256').update(read('CHAT-CONTEXT.md'), 'utf8').digest('hex');
  releaseDirs().forEach(function (dir) {
    const d = path.join(REL, dir);
    let man;
    try { man = JSON.parse(fs.readFileSync(path.join(d, 'MANIFEST.json'), 'utf8')); }
    catch (e) { fail.push(dir + ': unreadable MANIFEST.json'); return; }
    const keys = { k1: man.keys.part1, k2: man.keys.part2 };
    const hits = rk.filter(function (k) { return k.k1 === keys.k1; });
    if (hits.length === 0) fail.push(dir + ': key not in REGISTER.md');
    if (hits.length > 1) fail.push(dir + ': key appears ' + hits.length + ' times in REGISTER.md');
    const coverP = path.join(d, 'COVER-SHEET.md');
    const setupP = path.join(d, 'REVIEWER-SETUP.txt');
    const cover = fs.existsSync(coverP) ? fs.readFileSync(coverP, 'utf8') : '';
    const setup = fs.existsSync(setupP) ? fs.readFileSync(setupP, 'utf8') : '';
    if (cover.indexOf(keys.k1 + '/' + keys.k2) === -1) {
      fail.push(dir + ': COVER-SHEET.md does not carry the key pair the release embeds');
    }
    if (setup.indexOf('BUNDLE KEY (part 1): ' + keys.k1) === -1 ||
        setup.indexOf('BUNDLE KEY (part 2): ' + keys.k2) === -1) {
      fail.push(dir + ': REVIEWER-SETUP.txt does not embed the key pair the cover sheet prints');
    }
    if (man.sources && man.sources['CHAT-CONTEXT.md'] && man.sources['CHAT-CONTEXT.md'].sha256 !== curSha) {
      fail.push(dir + ': the sources have changed since this release was cut. Cut a new ' +
        'release; never change a bundle under a key already in circulation.');
    }
  });

  if (fail.length) {
    console.error('build-bundle --check FAILED\n');
    fail.forEach(function (f) { console.error('  - ' + f); });
    return 1;
  }
  console.log('build-bundle --check OK  (' + releaseDirs().length + ' release(s), prompt ' +
    PROMPT_VERSION + ', gate audience ' + ATTEMPT_GATE_AUDIENCE + ')');
  return 0;
}

function cmdVerifyDrive(file, key) {
  const p = path.join(REL, String(key), 'REVIEWER-SETUP.txt');
  if (!fs.existsSync(p)) { console.error('no such release: ' + key); return 1; }
  const want = fs.readFileSync(p, 'utf8');
  const got = fs.readFileSync(file, 'utf8').replace(/\r\n/g, '\n');
  if (got === want) { console.log('IDENTICAL'); return 0; }
  // A Doc is where smart quotes and autocorrected dashes get in, so report the first
  // difference by character. The fix is always to re-paste, never to edit the Doc.
  const n = Math.min(got.length, want.length);
  let i = 0; while (i < n && got[i] === want[i]) i++;
  const line = want.slice(0, i).split('\n').length;
  const show = function (s) { return JSON.stringify(s.slice(Math.max(0, i - 40), i + 40)); };
  console.error('DIFFERENT at character ' + i + ' (line ' + line + ')');
  console.error('  generated: ' + show(want));
  console.error('  drive doc: ' + show(got));
  console.error('\nRe-paste the Doc from releases/' + key + '/REVIEWER-SETUP.txt. Never edit the Doc.');
  return 1;
}

function usage() {
  console.log([
    'build-bundle.js -- the only thing allowed to produce a pasteable reviewer bundle.',
    '',
    '  --release [--note "<what changed>"]   mint a key pair and write a release',
    '  --check                               fail on any drift (joins check-docs.js)',
    '  --sync-test-kit                       regenerate the TEST-KIT pastes',
    '  --verify-drive <file> --release <key> diff a Drive copy-out against a release',
    '',
    'Sources are hand-edited: 04-prompt-templates.md sections A and B, CHAT-CONTEXT.md.',
    'Everything under releases/ and TEST-KIT/PASTE-* is generated. Fix a source and',
    'rebuild; never edit a generated file.',
  ].join('\n'));
  return 0;
}

function main(argv) {
  const a = argv.slice(2);
  const has = function (f) { return a.indexOf(f) !== -1; };
  const val = function (f) { const i = a.indexOf(f); return i === -1 ? null : a[i + 1]; };
  if (has('--check')) return cmdCheck();
  if (has('--sync-test-kit')) return cmdSyncTestKit();
  if (has('--verify-drive')) return cmdVerifyDrive(val('--verify-drive'), val('--release'));
  if (has('--release')) return cmdRelease(val('--note'));
  return usage();
}

if (require.main === module) process.exit(main(process.argv));
module.exports = {
  sources: sources, fill: fill, buildRelease: buildRelease, mintKeys: mintKeys,
  testKitFiles: testKitFiles, cmdCheck: cmdCheck,
  PROMPT_VERSION: PROMPT_VERSION, ATTEMPT_GATE_AUDIENCE: ATTEMPT_GATE_AUDIENCE,
};
