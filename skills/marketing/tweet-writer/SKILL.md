---
name: tweet-writer
description: "Write high-engagement tweets and X/Twitter threads, grounded in live research of what's currently working in the user's niche: researches viral examples via web search, then drafts hook variants, a single-tweet version, and a thread version with alternates to test. Use when the user says 'write a tweet about X', 'turn this into a thread', 'help me go viral', 'grow my X/Twitter account', 'my tweets get no engagement', or shares an idea/article to tweet — any X/Twitter content request. Produces a Tweet Package: 3 hook options, final single tweet, full thread, and posting notes."
---

# Tweet Writer

Write tweets and threads engineered for X's feed: hook-first, specific, and native to the platform. **Prime directive: the hook decides everything.** Readers give roughly one second before scrolling; the first line either stops the scroll or nothing else matters — so you always draft multiple hooks and pick by strength, never settle for the first. Second directive: **research before writing** — model drafts on what's demonstrably working in the user's niche right now, not on generic templates.

## When to use / when not to

- Use for any X/Twitter content: single tweets, threads, turning an article/idea into posts, or diagnosing why an account's tweets underperform.
- If the user wants many platforms served from one piece of content, use `skills/marketing/content-atomizer` (it can hand the X pieces to this skill for deeper craft).
- If the user needs the underlying long-form content first, use `skills/marketing/seo-content`.
- If the account has no defined voice at all, run `skills/marketing/brand-voice` first — hooks in someone else's voice read as spam.

## Intake

Ask in one batch, only what's missing:

1. **Topic and the core insight** — what's the one thing this tweet says?
2. **Niche and audience** — who follows (or should follow) this account?
3. **Goal** — replies/engagement, followers, or clicks/conversions? (Changes the CTA and format.)
4. **Ammunition** — real numbers, results, or stories to use. Specifics are the currency; press for at least one.

Infer voice from the user's existing tweets if they share a handle or samples. If enough is known, state assumptions and proceed — don't stall.

## Workflow

### 1. Research the niche (do not skip)

Before drafting, use web search to find what's currently working:

- `"[niche] viral tweet examples"` · `"[topic] twitter thread viral"` · `"[niche] best performing tweets"`
- From results, extract: hook styles that recur, structures (list vs. story vs. contrarian), the specificity level winners use, and CTA patterns.

Summarize findings in 3–5 bullets — this brief steers every drafting choice. If web search is unavailable, say so and fall back to the hook taxonomy in `references/tweet-hooks.md`, labeling the approach as template-based rather than researched.

### 2. Choose format by goal and material

| If… | Format |
|---|---|
| One sharp insight, goal = engagement | Single tweet (listicle, contrarian take, before/after, or fill-in-the-blank) |
| Multi-step framework, story arc, or article source | Thread (5–10 tweets) |
| Goal = replies specifically | Question or fill-in-the-blank single tweet |
| Goal = clicks/conversions | Thread with CTA closer; link in the reply, never the main tweet |

### 3. Draft 3 hooks (always)

Generate three genuinely different hooks — different *types*, not rewordings. Pull from these families (full taxonomy with examples: `references/tweet-hooks.md`):

- **Specific result**: "I [result] in [timeframe]. Here's how:" — strongest when real numbers exist
- **Contrarian/pattern interrupt**: "Everyone says [X]. They're wrong." / "Stop doing [common practice]."
- **Curiosity gap**: "The one thing [group] gets wrong about [topic]:"
- **Story**: "[Time] ago I was [bad state]. Today [good state]."
- **List promise**: "[N] [things] that [benefit]:"
- **Extreme**: "The best/worst/fastest [X] I've ever [Y]" — superlative, then overdeliver

Hook rules: lead with the payoff, not context; concrete number > adjective ("12,847 followers in 63 days" beats "grew fast"); first 7 words must carry the whole promise. Recommend one hook with a one-line reason; the user picks.

### 4. Write the body

**Single tweet** — aim ≤110 characters when the idea allows (heuristic: shorter scans faster and quotes better); apply a frame: PAS (problem → agitate → solution), BAB (before → after → bridge), or bare list. One idea only.

**Thread** — 5–10 tweets:

1. **Hook tweet** — the chosen hook + thread signal ("🧵" or a colon ending)
2. **Context tweet** — why this matters, deepen the curiosity
3. **Body tweets (one idea each)** — ≤250 chars per tweet; number them (2/, 3/ …); every tweet must earn the next click — end tweets on mini-cliffhangers or completed punches, never mid-mush
4. **Summary tweet** — compress the takeaways
5. **CTA closer** — exactly one ask: a question (drives replies), "follow for more [specific topic]", or a link — and links go in a reply under the thread, not in tweet 1

Persuasion levers to apply throughout: specificity (real numbers), social proof (real counts/names), curiosity gaps, relatability ("when you finally…"), tasteful contrarianism. All numbers and results must come from the user or the research — never fabricate metrics, follower counts, or outcomes.

### 5. Package and deliver

Run the quality bar, then deliver the Tweet Package. Include posting notes: platform-mechanics heuristics, clearly labeled as such — early engagement matters (be available to reply in the first hour); replies and bookmarks appear to outweigh likes; external links in the main tweet correlate with suppressed reach (put them in a reply); asking for likes/RTs reads as spam and underperforms. Don't promise algorithmic outcomes — these are patterns, not guarantees.

## Required output format

```
# Tweet Package — [topic]

## Research brief
- [3–5 bullets: patterns found in the niche, or "web search unavailable — template-based"]

## Hook options
1. [Type] "…" (n chars)
2. [Type] "…" (n chars)
3. [Type] "…" (n chars)
Recommended: #_ — [one-line reason]

## Single tweet
"…" (n chars)

## Thread
1/ "…" (n chars)
2/ "…" (n chars)
...
[Link-in-reply text, if goal = clicks: "…"]

## Alternates to test
- [1–2 alternate hook tweets or a variant angle]

## Posting notes
- CTA: [the one ask] · Link placement: [none | in reply]
- [Heuristics that apply: reply-window availability, no engagement-begging, etc.]
```

## Quality bar

Count, don't eyeball:

- [ ] 3 hook options of genuinely different types, each with char count
- [ ] Single tweet ≤280 chars (target ≤110); every thread tweet ≤250 chars
- [ ] First 7 words of the chosen hook carry the promise — read them alone and check
- [ ] At least one concrete specific (number, timeframe, named thing) in the hook or body — or explicitly flagged that the user provided none
- [ ] All numbers/results real (from user or cited research); nothing invented
- [ ] Exactly one CTA, in the closer only; no "like and RT" begging anywhere
- [ ] No external link in the main tweet — link text staged for a reply
- [ ] One idea per tweet; no filler tweets ("let me explain…" alone is not a tweet)
- [ ] Voice matches the user's samples — a follower should believe they wrote it

## Integration

- `skills/marketing/brand-voice` — supplies the voice; run first for new/undefined accounts.
- `skills/marketing/content-atomizer` — feeds this skill article-derived ideas for X; sends back the finished tweets into its distribution pack.
- `skills/marketing/seo-content` — published articles are prime thread source material; the thread's link-in-reply points back to the article.
- `skills/marketing/direct-response-copy` — deepens conversion-focused CTAs when a tweet/thread sells directly.

## References

- `references/tweet-hooks.md` — the full 8-framework hook taxonomy (Extreme, AIDA, PAS, BAB, and more) with structures and examples. Read it at Step 3 when drafting hooks, or whenever the three drafts feel same-y and you need a different attack angle.
