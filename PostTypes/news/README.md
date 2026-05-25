# News posts -- AI noticias (brand v2)

> **Skills:** see [`Skills/news-post-design.md`](Skills/news-post-design.md) for the full visual system and the Higgsfield prompt structure per slide. The brand visual system lives in [`Brand/brand-spec.md`](../../Brand/brand-spec.md).

## What this type is for

Posts about AI announcements, model releases, breaking news, industry events. **4-slide carousel** generated 100% via Higgsfield single-step (one image per slide with all text + visuals baked into the prompt) under brand v2 (Roboto + Playfair Italic, scheme/mode-aware). Mode (LIGHT/DARK) and color scheme (AMARILLO/ROJO/AZUL) asked at the start of every post.

## Trigger phrases

- "post de noticia: {titular}"
- "carrusel de la noticia de {evento}"
- "hagamos un post sobre la noticia de {tema}"
- "esto salió hoy: {url}"

## Skills to load (in order)

1. [Brand/brand-spec.md](../../Brand/brand-spec.md) -- canonical palette, fonts, slide patterns
2. [Skills/news-post-design.md](Skills/news-post-design.md) -- 4-slide news visual system + prompt structures

Plus the global mandatory skill:
- [../../Skills/visual-qa.md](../../Skills/visual-qa.md) -- mandatory post-render verification

## Structure -- 4 recipes + 7-type library (updated 2026-05-25)

News is no longer a fixed 4-slide skeleton. There are **7 slide types** in a library and **4 recipes** that pick from it. Pick the recipe that best fits the news, rotating vs the last 2 posts so the feed stays visually fresh.

**The 7 slide types** (full visuals + Higgsfield prompt anatomy in [Skills/news-post-design.md §1.1, §3-6.7](Skills/news-post-design.md)):

Cover (always slide 1) · Body text · Stat card · Verdict · **Tweet card** · **Quote pull** · **Comparison split**

**The 4 recipes** (pick ONE per post, rotate vs last 2):

| Recipe | Slides | When |
|---|---|---|
| **A — Standard** | Cover → Body → Stat → Verdict | Factual news with a strong number (default) |
| **B — Reaction** (5) | Cover → Body → Tweet/Quote → Stat → Verdict | When a public voice matters (CEO statement, official tweet) |
| **C — Comparison** | Cover → Body → Comparison → Verdict | Strategy pivots, before/after, X vs competition |
| **D — Photo essay** (5) | Cover → Body → Quote Pull → Stat → Verdict | Narrative/human news where an editorial quote earns its place |

**Visual variants per info slide** (body / stat / verdict each have 2-3 layout variants — pick one different from the last post). Full catalog in [Skills/news-post-design.md §1.4 and per-slide variant subsections](Skills/news-post-design.md).

**Length limits:** 3 minimum (thinner feels weak), 6 maximum (loses punch). 4-5 is the sweet spot.

## Workflow when the user triggers a news post

1. **Confirm type + color + mode** (per root CLAUDE.md §1)
2. **Read** [Brand/brand-spec.md](../../Brand/brand-spec.md), then [Skills/news-post-design.md](Skills/news-post-design.md)
3. **Mandatory visual re-anchoring:** open `Brand/Templates/Noticias/{COLOR}/{MODE}/` and read at least 2 PNGs. Then [Inspiracion/](Inspiracion/) and [Favoritos_Claude_Generated/](Favoritos_Claude_Generated/).
4. **Understand the news:** what happened, who's involved, what's the data
5. **If only a title was given → WebSearch** for the full story. Extract: who, what, when, how, numbers, impact, source.
6. **Draft the outline** in a SINGLE message that includes:
   - **Recipe pick + reason** (e.g. "Receta B porque hay un tweet real de Zeb Evans"). Check the last 2 dated folders in `Outputs/` and rotate — don't repeat the same recipe two posts in a row.
   - **Per-slide breakdown** (content angle for each slide of the chosen recipe)
   - **Visual variant per info slide** (e.g. "body variante (b) split porque la foto es vertical"). Per [Skills/news-post-design.md §1.4](Skills/news-post-design.md), pick a different variant than the most recent post used.
   - **Cover headline** (single best option, no variants) in Colombian Spanish with Playfair Italic emphasis words marked. Per memory `feedback_pick_the_best_headline.md`: don't ask which headline is preferred — pick the best one.
   - Wait for user approval before generating.
7. **Create the dated output folder:**
   ```bash
   mkdir -p "PostTypes/news/Outputs/$(date +%Y-%m-%d)_{topic-slug}"
   ```
   The `YYYY-MM-DD_` prefix is mandatory -- enables auto-prune (see step 14).
8. **Generate each slide via Higgsfield MCP** -- one call per slide (4-5 calls depending on recipe). Model: `nano_banana_pro`, `aspect_ratio: "4:5"`, `resolution: "2k"`. Each prompt includes ALL text content + the mandatory line "The top-left corner MUST BE COMPLETELY EMPTY. No logo, no symbol, no mark." Cover prompt additionally includes the subject company's logo (centered in dark zone above headline + thin divider line — see `feedback_news_cover_company_logo.md`). See [Skills/news-post-design.md §9](Skills/news-post-design.md) for the per-slide prompt structure.
9. **Download + resize each result** from native ~1856×2304 to 1080×1350 via PIL LANCZOS. Save as `slide{N}_{descriptor}.png` in the dated folder. Delete the raw download.
10. **Mandatory Visual QA** ([../../Skills/visual-qa.md](../../Skills/visual-qa.md)) -- open every PNG. Verify Spanish spelling (no `MENOS MENOS` duplications, no `Verifed` missing letters, no styling-instruction leakage like `Roboto Medium Italic, ALL CAPS: LA APUESTA`), all numerical stats, italic emphasis on right words, semaphore dot order (green/red/orange), empty top-left corner, **cover logo present and identifiable**. **If any error → regenerate that slide with a refined Higgsfield prompt. Do NOT patch via HTML or PIL.**
11. **Draft the short caption** (1-3 lines) → save as `caption.txt`
12. **Present the complete carousel** + caption to the user
13. **Ask which slides are favorites** → `cp` to [Favoritos_Claude_Generated/](Favoritos_Claude_Generated/) with `{topic-slug}_{slide_name}.png` naming
14. **Run auto-prune (MANDATORY):**
    ```bash
    python Brand/prune_outputs.py news
    ```
    Keeps the 5 most-recent dated folders, deletes older ones. Favorites already saved in step 13 survive (they live in a separate folder). Historical pre-migration folders without a date prefix are never touched. See root CLAUDE.md §3.6.

## Brand-wide rules that apply

From [CLAUDE.md](../../CLAUDE.md):
- Always ask the user to confirm type + color + mode (§1)
- Mandatory visual re-anchoring (§1.5)
- After every post, ask which images are favorites (§1.6)
- Colombian Spanish, `tú` form -- never voseo
- **No `@lucianomusellaa` handle AND no Alta Studio logo on news.** Top-left corner is intentionally empty (editorial magazine look). Every Higgsfield prompt must include the mandatory empty-corner instruction.
- **No SWIPE pill on cover, no page dots** -- IG handles pagination
- Image generation 100% via Higgsfield MCP (`nano_banana_pro` at `resolution: "2k"`)
- Tweet ethics ([Skills/news-post-design.md §8](Skills/news-post-design.md)) -- never fabricate quotes attributed to real people
- Auto-prune to keep last 5 posts per type (§3.6)

## Folder layout

```
PostTypes/news/
├── README.md                          ← this file
├── Skills/
│   └── news-post-design.md            ← visual system + per-slide Higgsfield prompts + tweet ethics
├── Inspiracion/                       ← external visual references (carousel patterns)
├── Favoritos_Claude_Generated/        ← past slides the user marked as favorites (NEVER pruned)
└── Outputs/                           ← rendered news carousels, auto-pruned to last 5 dated folders
    ├── 2026-05-24_opus-4-7/           ← NEW format: YYYY-MM-DD_topic-slug
    │   ├── slide1_cover.png
    │   ├── slide2_body.png
    │   ├── slide3_stat.png
    │   ├── slide4_verdict.png
    │   └── caption.txt
    └── allbirds-pivote-ia/            ← LEGACY (pre-migration, no date prefix → exempt from prune)
        └── ...
```

## Naming convention

- **Folder:** `YYYY-MM-DD_{topic-slug}/` where the date is the creation date and the slug is kebab-case, ≤4 words. Examples: `2026-05-24_opus-4-7`, `2026-05-24_anthropic-religiosos`, `2026-05-25_perplexity-billion`.
- **Slide files:** `slide{N}_{descriptor}.png` (e.g. `slide1_cover.png`, `slide2_body.png`, `slide3_stat.png`, `slide4_verdict.png`).
- **Caption:** `caption.txt` in the same folder.
- Never reuse a folder for a different news item.
- Folders without a `YYYY-MM-DD_` prefix are treated as historical archive and exempt from auto-prune.
