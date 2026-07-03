# Sprint Room Templates

Copy the skeletons below when scaffolding `sprints/<YYYY-MM-DD>-<slug>/`. Fill `<>` placeholders; delete unused sections. Whiteboards are created per exercise from the blocks in §4.

## 1. STATE.md

```markdown
# Sprint State
- Idea: <one sentence, user's wording (+ approved elaboration if any)>
- Type: foundation | design | chained (currently in: <foundation|design>)
- Tier: 1 live team | 2 stateless | 3 inline
- Phase: <F1|F2|F3|F4|D1|D2|D3|D4|D5> — next exercise: <name>
- Sprint room: <path>

## Roster — PROPOSED | APPROVED (dossiers in team/)
| Name | Role | Bias one-liner |
| ... | ... | ... |

## Session agents — valid this session only (expired on resume)
| Name | Agent handle |

## Resume protocol
Read DECISIONS.md + current phase whiteboards; respawn roster from team/*.md
(dossier + notebook, rehydration prompt in casting.md); continue at first
unticked CHECKLIST item. Agents do not survive sessions — files do.
```

## 2. CHECKLIST.md

Foundation variant (Design variant: same shape with D1–D5 exercises from the method file):

```markdown
# Checklist — gates are artifacts + decisions, never time
## Setup
- [ ] Intake complete (idea, sprint type, prior decisions)
- [ ] Sprint room scaffolded
- [ ] Roster proposed
- [ ] Roster APPROVED by Decider
- [ ] Cast spawned (tier: <>)
## F1 Basics
- [ ] Target customer — note-and-vote → decision logged
- [ ] Customer problem — note-and-vote → decision logged
- [ ] Your advantage — user-first + team challenge → decision logged
- [ ] Competitors + 800-lb gorilla — note-and-vote → decision logged
## F2 Differentiation
- [ ] Classic differentiators dot-voted
- [ ] Custom differentiators note-and-voted
- [ ] Two differentiators picked (Decider)
- [ ] 2x2: alone top-right, honestly
- [ ] 2–3 principles → Mini Manifesto in OUTPUTS.md
## F3 Approach
- [ ] Options generated + labeled (≤7, Decider)
- [ ] Magic Lenses plotted (4 classic + custom)
- [ ] Pattern review (contradictions named)
- [ ] Top Bet + Backup decided
## F4 Hypothesis
- [ ] Founding Hypothesis assembled
- [ ] Team attack round (weakest clause each)
- [ ] Prove-it scorecard + riskiest assumption
- [ ] First move decided → OUTPUTS.md complete
```

## 3. team/<name>.md (dossier + notebook)

```markdown
# <Name> — <Role>
- Expertise anchor: <1–2 sentences, concrete>
- Bias / agenda: <one sentence that creates friction>
- Voice: <2–3 adjectives + tic>

## Notebook (append after every exercise — this is what survives sessions)
### <exercise>: <their position in 1–3 lines, incl. votes + reasons>
```

## 4. Whiteboard blocks

One file per exercise: `whiteboards/<NN>-<exercise>.md`. Compose from:

**Note-and-vote board**
```markdown
# <Exercise> — note-and-vote
## Brief
<the prompt everyone got>
## Board (anonymized)
- **A.** <note>
- **B.** <note>
## Votes (revealed only after all votes in, incl. user's)
| Note | Dots | One-line rationales |
## Decider's call
- Chosen: <> | Reason: <> | Said no to: <>
## Provenance (write ONLY after the Decider's call)
| Note | Author |
```

**2x2 (portable notation — differentiation chart and every Magic Lens)**
```markdown
Y: <low label> ←→ <high label>
X: <low label> ←→ <high label>
WIN = top-right
| Quadrant | Who | Read |
| Top-right | <you?> | own it |
| Top-left / Bottom-right / Bottom-left | <competitors / options> | Loserville |
```
Test of a good differentiation chart: alone top-right AND deliverable. For lenses: same notation, plot all labeled options A–G.

**Solution sketch (D2)**
```markdown
# "<Catchy title>" (anonymous until after supervote)
## Panel 1 — <moment>
<what the customer sees/does; ASCII layout block if useful; REAL copy>
## Panel 2 — <moment>
## Panel 3 — <payoff>
```

**Storyboard (D3)**: numbered frames 1–15, frame 1 = real-world opening scene; each frame = one line of action + the screen/scene it happens on.

**HMW board (D1)**: anonymized `HMW <...>` list → themes → dot-vote table → winners placed on map.

## 5. DECISIONS.md

```markdown
| # | Phase | Decision | Decider's reason | Rejected alternatives |
```

## 6. OUTPUTS.md

```markdown
# Sprint Outputs — <idea>
## Founding Hypothesis (F4)
> If we help **<customer>** solve **<problem>** with **<approach>**, they will
> choose it over **<competitors>** because our solution is **<diff1> + <diff2>**.
## Mini Manifesto (F2)
Differentiators: <two> · Principles: 1) <> 2) <>
## Magic Lenses summary (F3)
| Option | Customer | Pragmatic | Growth | Money | <custom> | Pattern |
Top Bet: <> · Backup: <>
## Prove-it scorecard (F4)
| Prediction | Cheapest falsifying test | Risk H/M/L |
Riskiest assumption: <> · First move: <>
## Prototype (D4)
Path/link: <> · Trial run: pass/notes
## Test report (D5) — ⚠️ SIMULATED CUSTOMERS
Repeat with 5 real customers before trusting this. Simulated results are
directionally useful for comprehension/confusion, weak for willingness-to-pay.
### Interview grid
| Finding / sprint question | C1 | C2 | C3 | C4 | C5 |
### Patterns (≥3 of 5)
### Verdicts on sprint questions
| Question | yes/no/mixed | Evidence |
### Decider's next step
refine & re-test | pivot to Backup | proceed to build — <reason>
```

## 7. Interview script (D5, five acts)

```markdown
1. Welcome — put them at ease; "think out loud, no wrong answers."
2. Context — their situation, current workaround (let them elaborate beyond profile).
3. Introduce prototype — "some things may not work; I didn't design it."
4. Tasks — open-ended nudges from the storyboard; NEVER leading; they narrate.
5. Debrief — likes/dislikes, describe-to-a-friend, would-you-use (grain of salt).
```
