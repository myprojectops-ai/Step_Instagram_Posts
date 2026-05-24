---
name: visual-posts-news
description: Create or edit AI news Instagram carousels in Visual_posts. 4-slide carousel (cover / body / stat card / verdict) under brand v2 (Roboto + Playfair Italic, scheme/mode aware). Higgsfield MCP for photos.
---

# News Posts (brand v2)

Use this skill for AI news carousels. Current format is a **4-slide carousel** (cover / body / stat card / verdict).

**Workflow (updated 2026-05-23, simplified):** 100% Higgsfield, no overlays. Each slide is a single Higgsfield generation with all text + visuals + layout in the prompt. The only post-processing is a PIL resize to 1080×1350. **News slides have NO Alta Studio logo and NO `@lucianomusellaa` handle.** The top-left corner is intentionally empty -- editorial magazine look. Every prompt must include the mandatory line: "The top-left corner MUST BE COMPLETELY EMPTY. No logo, no symbol, no mark, no triangle." NO HTML overlay, NO render.sh, NO CSS, NO PIL paste.

## Required References

Read these before production work:

1. `.codex/skills/visual-posts-core/SKILL.md`
2. `Brand/brand-spec.md`
3. `PostTypes/news/README.md`
4. `PostTypes/news/Skills/news-post-design.md`

## Workflow

1. Confirm type + color (AMARILLO/ROJO/AZUL) + mode (LIGHT/DARK).
2. **Open `Brand/Templates/Noticias/{COLOR}/{MODE}/`** and view at least 2 reference PNGs.
3. Review `PostTypes/news/Inspiracion/` and every file in `PostTypes/news/Favoritos_Claude_Generated/`.
4. Understand and verify the news. Browse when the user gives only a headline, a current event, a URL, or anything likely to have changed.
5. Draft the 4-slide outline and wait for approval.
6. Propose ONE cover headline (single best option, no variants per `feedback_pick_the_best_headline.md`).
7. Research official tweets when a quote/tweet slide is needed.
8. Create `PostTypes/news/Outputs/$(date +%Y-%m-%d)_{topic-slug}/`. **Folder MUST start with `YYYY-MM-DD_` prefix.**
9. Generate each slide via `mcp__higgsfield__generate_image` with `model: nano_banana_pro`, `aspect_ratio: "4:5"`, `resolution: "2k"`. The prompt must include ALL text (headline, stats, bullets, eyebrows, subtitles) with explicit styling (Playfair Italic emphasis words in scheme highlight color, etc.) AND the mandatory line: "The top-left corner MUST BE COMPLETELY EMPTY. No logo, no symbol, no mark, no triangle."
10. Download + resize each result from native ~1856×2304 to 1080×1350 (PIL LANCZOS). Save as `slide{N}_{descriptor}.png` in the dated folder. Delete the raw download.
11. Inspect every PNG (Visual QA). Verify Spanish spelling, all numerical stats, italic emphasis on right words, semaphore dot order (green/red/orange), top-left corner empty (no invented logo). If a slide has any error, regenerate the Higgsfield step with a refined prompt — do NOT patch via HTML or PIL.
12. Save a 1-3 line caption as `caption.txt`.
13. Present the carousel + caption and ask for favorites.
14. **Auto-prune:** run `python Brand/prune_outputs.py news` to keep only the 5 most-recent dated folders. See CLAUDE.md §3.6.

## Slide Structure (4-slide default)

| # | Slide | Purpose |
|---|---|---|
| 1 | Cover | Full-bleed Higgsfield photo + gradient overlay + headline (Roboto Black ALL CAPS with Playfair Italic emphasis words) + subtitle |
| 2 | Body text + photo | Text top with stats inline (`%`, numbers in Playfair Italic highlight) + 16:9 photo zone bottom |
| 3 | Stat card | White card with huge Roboto Black number + `%` in Playfair Italic + comparison cards |
| 4 | Verdict | White card with synthesis headline + 3 semaphore bullets (green/orange/red dots) |

Use 3 slides (drop stat or verdict) for ultra-simple news, 5-6 for complex news (insert tweet/quote slide).

## Visual Rules (brand v2)

- Mode-driven background and text (LIGHT cream / DARK warm-dark).
- Scheme-driven highlight color on every emphasis word.
- **No `@lucianomusellaa` on news. No Alta Studio logo either.** Top-left corner is intentionally empty (editorial magazine look). Every prompt must include the mandatory "TOP-LEFT MUST BE EMPTY" instruction.
- **No page dots** on news slides (or any slides).
- **No SWIPE pill** on the cover (the templates don't use one; IG's affordance is enough).
- HTML owns all typography, logos, tweet cards, stats, and labels.
- Generated images must contain no text, logos, words, or watermarks.
- Headline and subtitle on the cover MUST be SEPARATE absolute-positioned elements (not nested -- Chrome clips nested children that extend past parent height).

## Image Ratios (Higgsfield)

- Cover photo: `--ar 4:5` → 1080×1350
- Body photo: `--ar 16:9` → 1080×608
- Avatar: `--ar 1:1` → 1080×1080

## Tweet Ethics

- Never fabricate a quote attributed to a real person or company.
- Official announcements require web verification and faithful reproduction.
- Invented reaction tweets must use invented handles/personas.
- If a real tweet cannot be verified, use an editorial quote/source card instead.

## Historical Outputs

Some older `PostTypes/news/Outputs/` folders use deprecated 5-slide format, Inter typography, gpt-image-1 photos, or watermark patterns. **Treat them as archive, not current spec.** Do not re-render.
