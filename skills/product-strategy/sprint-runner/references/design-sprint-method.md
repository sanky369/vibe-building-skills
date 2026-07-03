# Design Sprint — Team Method (phase-gated)

From *Sprint* (Knapp, Zeratsky, Kowitz) and the official checklist, adapted for a facilitated virtual-team run. Book days (Mon–Fri) survive only as vocabulary; every phase gates on its artifact + logged decision and the next phase starts whenever the user says go.

Inputs: a challenge worth a sprint. In chained mode, inherit from the Foundation Sprint: the challenge = the scorecard's riskiest assumption; carry the Founding Hypothesis and Mini Manifesto into every brief.

## D1 — Map (understand & target)

1. **Long-term goal** — note-and-vote: "Why are we doing this? Where do we want to be in 2 years if everything goes right?" One sentence, optimistic. Decider picks.
2. **Sprint questions** — note-and-vote: rewrite fears/assumptions as questions ("Can we make people trust an AI-built course?"). Keep 1–3 (Decider).
3. **The map** — you draft it live with the team: customers/actors on the left, ending (the goal moment) on the right, 5–15 steps between showing how customers move through the product/service. Teammates propose corrections one pass each; user approves. Store as an ASCII/markdown flow in the whiteboard.
4. **Ask the Experts** — interview each teammate in character, one at a time (their expertise anchor is the point of this exercise); interview the user too. While each speaks, EVERYONE else (teammates in the same call, plus you) writes **How-Might-We notes** — problems reframed as opportunities, "HMW …" one per note.
5. **HMW board** — post all HMWs anonymized, group into themes, silent dot-vote (team + user, tally hidden until all voted). Winners get placed on the map where they apply.
6. **Pick the target** — Decider circles ONE target customer and ONE moment on the map. Everything downstream aims here.

Gate: map + target + sprint questions in whiteboards/, decision logged.

## D2 — Sketch (diverge)

1. **Lightning Demos** — each teammate finds 1–2 real products/services (any domain — great inspiration is usually outside the industry; use web search if available, otherwise known examples labeled as recalled) and gives a 3-line demo: what it is, the **big idea** worth stealing, how it maps to our target. You capture each big idea with a quick doodle-note on the board. User adds their own demos.
2. **Four-step sketch** — every teammate AND the user produce, alone:
   - *Notes*: gather the best from the room (20 min-equivalent — for agents: re-read the boards).
   - *Ideas*: rough private doodles/bullets around the target.
   - *Crazy 8s*: the persona's strongest idea, pushed through 8 rapid variations (agents: 8 one-line variants).
   - *Solution sketch*: a **3-panel storyboard** of the customer experiencing the solution — markdown panels with ASCII layout blocks where useful. Rules: self-explanatory (a stranger must get it with no pitch), **words matter** (real copy, no lorem ipsum), give it a catchy title, keep it ANONYMOUS.

Gate: one solution sketch per participant in `whiteboards/sketches/`, unattributed.

## D3 — Decide (converge)

Run as one continuous session on the sketch gallery:

1. **Art museum** — post all sketches anonymized (already are).
2. **Heat map** — every reviewer (each teammate + user, blind to each other) marks the 1–3 standout parts per sketch + any big concern. Aggregate marks onto each sketch.
3. **Speed critique** — you narrate each sketch's highlights from the heat map; the sketch's creator stays anonymous and silent; capture standout ideas by name on the board.
4. **Straw poll** — each teammate votes for ONE whole sketch with a one-line reason; user votes too (tally hidden until all in).
5. **Supervote** — the Decider's 3 votes are FINAL. Winning ideas (can be a merge of sketches — note which parts) become the prototype spec.
6. **Storyboard** — build a 10–15 frame storyboard with the team: frame 1 is the *opening scene* — how the customer encounters the product in the real world (a search, a message, an app store page) — then step through the winning flow frame by frame. You draft; teammates flag gaps (one pass); user approves each block of frames. No new ideas here — only what won.

Gate: storyboard in whiteboards/, supervote logged.

## D4 — Prototype (fake it)

"Goldilocks quality": real enough for honest reactions, cheap enough to throw away. It's a **facade** — only what the storyboard shows.

1. **Pick the format & tools** — for software ideas in a repo-capable harness, default to a clickable HTML/JS mock in `sprints/<slug>/prototype/` (openable in a browser, no build step). Non-software: pitch deck, fake landing page, printed-menu markdown — whatever fakes the storyboard.
2. **Assign roles** — makers (teammates whose expertise fits build sections — in Tier 1/2 they write actual files when the brief explicitly says so, the one exception to the no-file-writes contract), a stitcher (you — consistency of copy/style across sections), a writer (real copy, in the product's voice — no placeholder text anywhere a tester will look), an interviewer (drafts the D5 script from the sprint questions).
3. **Trial run** — walk the prototype against the storyboard frame by frame; fix gaps; user reviews and approves.

Gate: prototype path/link + trial-run pass in OUTPUTS.md.

## D5 — Test (five interviews)

**Integrity rules first:** the 5 test customers are fresh agents built per `casting.md` ("Test customers") — target-matching profiles, ZERO sprint context, never reuse teammates. All results are labeled **SIMULATED** everywhere they appear, and the report opens by recommending the same test with 5 real customers. Simulated testers are directionally useful for comprehension/confusion findings and nearly worthless for "would you pay" findings — say so in the report.

1. **Five-act interview** (each customer agent, one at a time; interviewer persona or you runs it, transcript to whiteboards/interviews/):
   1. Friendly welcome + "there are no wrong answers, think out loud."
   2. Context questions — their life, current workaround (from their profile, but let them elaborate).
   3. Introduce the prototype — "some things may not work; I didn't design it, so you won't hurt my feelings."
   4. Tasks — open-ended nudges from the storyboard ("here's the landing page — what is this? what would you do next?"), never leading. Customer narrates reactions panel by panel.
   5. Debrief — what did they like/dislike, how would they describe it to a friend, would they use it (and note the grain of salt).
2. **Interview grid** — rows = sprint questions + emergent findings; columns = the 5 customers; fill in +/–/quote after each interview.
3. **Patterns** — after all five: what did ≥3 customers do/say? Positive, negative, confused.
4. **Verdicts** — answer each sprint question: clear yes / clear no / mixed, with the evidence. Then the Decider decides what's next: refine and re-test, pivot to the Backup, or proceed to build.

Gate: test report (grid + patterns + verdicts + SIMULATED banner + real-test recommendation) in OUTPUTS.md. Sprint complete.

## Efficiency note

D2's four-step sketch and D5's five interviews are the token-heavy rounds (6 participants × multi-part outputs; 5 × full interviews). Don't compress them — they're the sprint's engine — but don't pad them either: sketches are 3 panels, not 10; interviews end when act 5 is done.
