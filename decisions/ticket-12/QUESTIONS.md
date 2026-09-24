# Ticket 12 — three questions for Manuel

Written 2026-09-20, after the first version of these questions was too compressed to argue with.
This version leads with **the moment it happens to somebody**, then what each option does to that
person, then where the cost lands. The decision is at the bottom of each one.

Background if you want it: [ticket 12's resolution](../issues/12-decide-the-bundles-truncation-self-check.md)
and [the measurements](../proto-12-selfcheck/RESULTS.md). You do not need either to answer these.

**What was built, in one paragraph.** When a student pastes the reviewer into a free chat window,
part of it can silently go missing — and ticket 04 measured that the review still comes back looking
perfect. The fix is two short code strings hidden in the bundle, one near the start and one at the
very end. The reviewer has to print both on the first line of every review. The student's cover
sheet tells them what that line should say. If it does not match, something went missing. It worked
on every run: 34 reviews across two different AI models, and not once did a model make up a code it
did not have.

Three things are left to decide.

---

## Q1: When the check fires, does the reviewer stop, or warn and carry on anyway? `[big]`

### The scene

Sunday evening. A student in the pilot has a client deck due Monday. No paid plan, so they open a
free chat window, paste the setup as one long message, paste their deck, type their own read of it,
and ask for the review.

**Everything arrived. Nothing was cut.** But the reviewer's first line comes back as

```
REVIEW OF: final recommendation deck | MODE: deep | KEYS: SIGMA-7K/MISSING
```

and it stops, saying its instructions arrived incomplete. It is simply wrong — it was holding both
codes and failed to copy one back.

**That is a false alarm, and it is the thing you asked me to write down.** In 14 complete runs
across two models it did not happen once. But 14 is not many runs. The honest statement is *"we did
not see it, and we cannot yet rule out it happening to something like one student in five."* If the
pilot is 20 students doing two reviews each, that range spans "never happens" to "happens eight
times".

### What each option does to that student

- **A — Stop.** No review. They see the refusal, start a new chat, and paste everything again.
  About two minutes on a laptop. Considerably worse on a phone. If it happens twice, most people
  stop trying.
- **B — Warn and review anyway.** A warning line at the top, then a full review underneath. If the
  alarm was false, the review is perfectly good and the warning was noise. If the alarm was real,
  they get a review that ticket 04 showed will *look* complete while being built on a third of the
  reviewer's instructions — and they may read past the warning.

**Worth knowing: the student's own check works either way.** Comparing that first line against
their cover sheet catches the problem under both options. The difference is only whether the
reviewer stops them, or leaves it to them to notice.

### Where the cost actually lands

- **Under A, the cost falls on students whose setup was fine.** Wasted time, and some of them give
  up. For 180DC that is not a degraded outcome, it is a total loss — the realistic alternative to
  this tool is no substantive review at all, so a student who walks away gets nothing.
- **Under B, the cost falls on students whose setup really was cut.** They act on a review that is
  quietly wrong, and some of that goes to a real client board.

### What we know, and how well

- False alarms seen: **0 in 14 complete runs**, two models. Upper end of what that rules out:
  **about one student in five**. Thin, and I am not dressing it up.
- Refusal, when the setup genuinely was cut: **9 of 9**, both models, no review produced.
- The parallel attempt-gate ticket measured the same fork from the other side and found
  **a check that reports a problem gets ignored; a check that withholds the product holds.**

### The decision

**I'd pick A — stop.** A false alarm costs one re-paste. A missed cut costs a confident review built
on a third of its instructions, going to a client.

**The best case against me:** the false-alarm number is genuinely weak, and the students most likely
to hit it are the ones on the smallest free windows — the ones already most likely to give up. A
refusal is the only option that can lose a student entirely, and losing them means they get no
review at all, which is the exact thing this whole project exists to prevent.

**If you're not sure:** say *"just pick"* and I take A. Or say *"soften it"* and I ship A with the
refusal message spelling out that this is usually a one-paste fix, not a broken tool.

---

## Q2: Should the hidden code also say which version of the reviewer produced the review? `[medium]`

### The scene

It is November. A team lead opens a review a student ran back in September and pasted into a
document. The reviewer's instructions were changed in October.

**The lead has no way to tell which version produced what they are reading.** Nothing in the chat
output says. That is a real gap — it is half of the distribution ticket, still open.

The code line is already on every single review, in a place a lead reads. So it can carry the
version for free.

### What each option looks like on the page

- **A — Make the code readable as a version.** First line reads
  `KEYS: 0919-SIGMA7K/DELTA-3Q`. The lead sees `0919` and knows it is the September bundle.
- **B — Keep it meaningless.** First line reads `KEYS: SIGMA-7K/DELTA-3Q`. Tells you nothing about
  version; something separate has to be built later to solve it.

### Where the cost actually lands

- **Under B**, on leads reading records months later, and on anyone trying to compare how the pilot
  went before and after a change to the reviewer. It does not hurt a student at all.
- **Under A**, the risk is subtler and it lands on every student. The whole check rests on the model
  *copying* a code rather than *guessing* one. A code that looks like a date is exactly the kind of
  thing a model reconstructs from context — it can see today's date. If it writes `0920` where the
  bundle said `0919`, a student gets a false alarm for no reason. Worse, if a model can plausibly
  guess the shape of the code, it could produce a convincing-looking code when the bundle really was
  cut, and the check passes when it should fail.

### What we know, and how well

- **Zero codes invented in 34 runs.** This is the strongest number in the whole ticket, and it is
  what makes the check trustworthy.
- **It was measured on meaningless codes only.** The version-readable variant has never been run.

### The decision

**I'd pick A — make it readable as a version, but keep a random chunk in it** (`0919-SIGMA7K`, not
`v2026-09-19`), and **run the variant before it ships**.

**The best case against me:** the zero-invented-codes result is the single thing holding this check
up, and it was measured on meaningless strings. Making the code guessable trades the strongest
property we have for a convenience that only affects leads reading old records — and there are
other, duller ways to stamp a version.

**If you're not sure:** say *"test it first"* and nothing ships until the readable version has been
run against a cut bundle. That is the cautious answer and it costs about twenty minutes.

---

## Q3: Should the reviewer's method be repeated in the second paste, so a broken session still gives a partial review? `[medium]`

### The scene

A student working on their phone, free account, a conversation that has gone on a while. Chat
windows drop the **oldest** message first when they run out of room — the parallel ticket measured
this. The oldest message is the first paste, which holds how the reviewer actually thinks.

So the method is gone, and the student does not know it.

### What each option does to that student

- **A — Do not repeat it.** The check fires, the reviewer stops, and the student has to start a new
  chat and paste roughly 42,000 characters again. On a phone.
- **B — Repeat it in the second paste.** The reviewer still has its method, and produces a review —
  shorter and less disciplined than a full one, but real.

### Where the cost actually lands

- **Under A**, on students on the smallest windows — the ones the pilot most needs to hear from, and
  the ones for whom re-pasting is worst.
- **Under B**, on every student, all the time: repeating the method costs **1,377 tokens, about a
  sixth of everything they paste.**

**And there is a trap in B worth naming.** Making the bundle a sixth bigger makes the window fill up
sooner, which makes the eviction it is protecting against **more likely**. You would be paying, on
every run, to soften a failure you are simultaneously making more common.

### What we know, and how well

- Before this check existed, losing the first paste was **invisible** — a perfect-looking review
  built on nothing. That is what repetition was originally for.
- Now, losing the first paste is a **refusal**, measured on both models.
- So repetition no longer buys *safety*. It buys *a degraded review instead of an honest stop*.

### The decision

**I'd pick A — do not repeat it.** The reason for repeating it was to stop a silent failure, and the
silent failure is gone. Paying a sixth of the bundle to make the remaining failure less annoying,
while making that failure more likely, is the wrong trade.

**The best case against me:** the students this hits are exactly the ones who cannot easily recover —
a phone, a small window, a deadline. For someone who realistically gets one attempt, a worse review
beats no review, and "start again" is advice that only works for people with a laptop and time.

**If you're not sure:** say *"park it"*. The pilot can ship without it, and we add it only if
refusals turn out to be common in practice — at which point we will have a real number instead of
this argument.

---

## If you only want to answer one

**Q1.** Q2 has a safe fallback I can take without you (test the variant first), and Q3 can be parked
until the pilot produces a number. Q1 decides what the pilot's students actually experience when
something goes wrong, and it cannot be deferred.
