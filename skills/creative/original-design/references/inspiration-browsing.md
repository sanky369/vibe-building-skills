# Gathering Visual Inspiration from the Web

## Contents
- When to use this
- Choosing your browsing method (by host agent)
- Method A: Claude Code + Claude in Chrome
- Method B: Codex + Computer Use
- Method C: Web search fallback (any agent)
- Where to look (platforms)
- What to search for
- What to capture

## When to use this

Two moments in the Original Design flow:
- **Phase 1.5** — references for the core metaphor + mood, *before* defining vocabulary.
- **Phase 6** — inspiration from *unrelated* domains, to keep the world fresh.

Goal each time: collect **8–15 references**, then extract the *patterns* (color temperature, lighting, composition, shape language, texture, typography), not just pretty pictures. Always summarize the patterns back to the user.

## Choosing your browsing method (by host agent)

Pick the first available option, in this order:

```
Is this Claude Code with the Chrome extension connected?  → Method A (Claude in Chrome)
Is this Codex with the Computer Use plugin installed?      → Method B (Codex Computer Use)
Otherwise (no visual browser available)                    → Method C (web search fallback)
```

A real, pixel-level look at moodboards (Methods A/B) is strongly preferred for design work because most inspiration lives in images, not text. Use Method C when no visual browser is available — it still surfaces named styles, palettes, and source URLs you can reason about and hand to the user.

If you're unsure whether a visual browser is connected, ask the user once ("Do you have Claude in Chrome / Codex Computer Use available?") rather than guessing.

## Method A: Claude Code + Claude in Chrome

Claude Code drives a real Chrome (or Edge) window through the **Claude in Chrome** extension. It opens tabs, shares your logged-in state, navigates, reads the DOM, and screenshots — so you can actually *see* moodboards.

Requirements (per official docs):
- Chrome or Edge + the **Claude in Chrome** extension (v1.0.36+)
- Claude Code v2.0.73+ on a direct Anthropic plan (Pro/Max/Team/Enterprise)

Enable it:
- Launch with `claude --chrome`, or run `/chrome` inside a session to connect / check status / reconnect.
- Run `/mcp` → `claude-in-chrome` to see the available browser tools.

Use it (natural-language instructions to the browser):
1. "Open cosmos.so and search for `<metaphor> <mood>` (e.g. *living library, warm, scholarly*). Scroll the results."
2. "Screenshot the grid so we can study the recurring colors and textures."
3. "Open the 3 strongest clusters/boards and capture them."
4. Repeat across the platforms listed below.

Notes: browser actions run in a visible window; when Claude hits a login wall or CAPTCHA it pauses for the user to handle it manually. Reference: code.claude.com/docs/en/chrome.

## Method B: Codex + Computer Use

Codex can see and operate the GUI (browser or desktop apps) via the **Computer Use** plugin on macOS or Windows.

Requirements (per official docs):
- Install the **Computer Use** plugin from Codex settings.
- macOS: grant Screen Recording + Accessibility permissions. Windows: keep the target app visible/foreground.
- Not available in EEA, UK, and Switzerland at launch.

Use it:
- Invoke by mentioning `@Computer` (or `@<AppName>`) in the prompt, or ask Codex to use computer use.
- Then drive a browser the same way as Method A: open cosmos.so / Pinterest, search the metaphor + mood, scroll, and screenshot strong boards.

Reference: developers.openai.com/codex/app/computer-use.

## Method C: Web search fallback (any agent)

When no visual browser is available, use the agent's web search/fetch (Codex CLI and Claude both ship first-party web search):

1. Search e.g. `"<metaphor> <mood> design inspiration site:cosmos.so"`, `"<metaphor> moodboard pinterest"`, `"<style> UI dribbble"`.
2. Fetch the top result pages and read titles, descriptions, tags, and any extractable palette/style notes.
3. Collect the **source URLs** and present them to the user as a clickable shortlist so they can open the visuals themselves.
4. Lean on *named* styles (e.g. "neo-brutalist", "claymorphism", "risograph", "blueprint/technical-drawing") to anchor the direction in words even without seeing every image.

Be honest about the limitation: you're reasoning from text + thumbnails, so confirm the visual direction with the user before locking it.

## Where to look (platforms)

| Platform | Best for |
|---|---|
| **cosmos.so** | Ad-free, human-curated visual clusters; AI-content filter; great for mood + texture |
| **Pinterest** | Broadest coverage; good for metaphor objects, color stories, niche aesthetics |
| **Savee** | Designer-curated, high signal for art direction |
| **Are.na** | Conceptual, cross-domain connections (ideal for Phase 6 unrelated domains) |
| **Dribbble / Behance** | Execution references for UI, motion, illustration systems |
| **Unsplash / museum & archive sites** | Phase 6 raw material from nature, architecture, manuscripts, space, machinery |

## What to search for

- **Phase 1.5:** `metaphor + mood` (e.g. "explorer's journal, vintage, hand-drawn"), plus the named DNA you're leaning toward.
- **Phase 6:** the *unrelated domain* itself ("brutalist architecture grids", "botanical illustration palettes", "NASA mission patch design", "vintage scientific diagrams", "industrial machinery blueprints").

## What to capture

For every reference set, record:
- 8–15 references (screenshots or URLs)
- **Recurring patterns:** color temperature, lighting, composition, shape language, texture, typography
- **3–5 transferable "steals"** (Phase 6): the specific idea you'll borrow, not a wholesale copy

Feed these directly into Phase 2 (vocabulary) and Phase 3 (Design DNA).
