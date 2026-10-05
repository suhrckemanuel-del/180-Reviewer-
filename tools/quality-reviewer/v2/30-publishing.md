# Publish and verify a supervised candidate

The private GitHub repository is the recovery/download entry point. Read generated
START-HERE.md: students use STUDENT setup/input files, leads use LEAD setup/input files.
Local generation does not publish, prove consultant access or approve a pilot.

Sources: 04-prompt-templates.md, CHAT-CONTEXT.md, STUDENT-PATH.md, LEAD-PATH.md,
START-HERE.md and HTML-PATH.md. HTML uses dedicated audience templates and shared renderer,
stylesheet and client code. build-bundle.js is the only bundle writer.

    node tools/quality-reviewer/v2/build-bundle.js --sync-test-kit
    node tools/quality-reviewer/v2/build-bundle.js --check
    node tools/quality-reviewer/v2/build-bundle.js --release --note "Supervised candidate, owner acceptance pending"

Generation mints one key pair shared by both audiences, writes an immutable releases/<part-1>
directory and appends the register. Manifests name each audience's files, version and source
hashes. No client examples. Never overwrite an old release; change sources and mint another
pair. --check verifies every recorded file hash.

Download matching setup files from the PR branch or registered candidate directory.
Verify a recovered setup (keep its STUDENT- or LEAD- filename prefix):

    node tools/quality-reviewer/v2/build-bundle.js --verify-copy STUDENT-SETUP.txt --release <part-1>

Expect IDENTICAL. Confirm pair/version/audience against START-HERE and MANIFEST.
Only an intended consultant's actual access check establishes consultant download permission.
Record account capacity and pilot observations separately from software verification.

Optional HTML is local only; keep the candidate inside this Git checkout. Genuine inputs,
quotations, notes and screenshots stay ignored under _client-private. Inspect staged changes
and manifests before committing. Open a dedicated PR for owner review; no automatic merge or
deployment. A named human signs off before client use.

The historical hosted URL still served the old desk on 2026-10-06 despite the local kill switch
being on. It is excluded from this candidate. Authorized withdrawal deployment and live
verification remain open; see validation/SPLIT-EXPERIENCES-2026-10-06.md at repository root.
