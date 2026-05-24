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

## The 4-slide default structure

| # | Slide type | Purpose |
|---|---|---|
| 1 | **Cover** | Full-bleed editorial photo + gradient + headline (Roboto Black ALL CAPS with Playfair Italic emphasis words) + subtitle |
| 2 | **Body** | Text top with stats inline (numbers in Playfair Italic highlight) + 16:9 concept photo zone bottom |
| 3 | **Stat card** | White/light card on dark bg with huge Roboto Black number + `%` in Playfair Italic + comparison cards |
| 4 | **Verdict** | White/light card with synthesis headline + 3 semaphore bullets (green/orange/red dots) + BOTTOM LINE closer |

Flexibility: 3 slides (drop stat or verdict) for ultra-simple news; 5-6 for complex news.

## Workflow when the user triggers a news post

1. **Confirm type + color + mode** (per root CLAUDE.md §1)
2. **Read** [Brand/brand-spec.md](../../Brand/brand-spec.md), then [Skills/news-post-design.md](Skills/news-post-design.md)
3. **Mandatory visual re-anchoring:** open `Brand/Templates/Noticias/{COLOR}/{MODE}/` and read at least 2 PNGs. Then [Inspiracion/](Inspiracion/) and [Favoritos_Claude_Generated/](Favoritos_Claude_Generated/).
4. **Understand the news:** what happened, who's involved, what's the data
5. **If only a title was given → WebSearch** for the full story. Extract: who, what, when, how, numbers, impact, source.
6. **Draft the 4-slide outline** -- propose breakdown for each slide angle. Wait for user approval.
7. **Propose the cover headline (single best option, no variants)** in Colombian Spanish with Playfair Italic emphasis words marked. Wait for approval. Per memory `feedback_pick_the_best_headline.md`: don't ask which headline is preferred -- pick the best one.
8. **Create the dated output folder:**
   ```bash
   mkdir -p "PostTypes/news/Outputs/$(date +%Y-%m-%d)_{topic-slug}"
   ```
   The `YYYY-MM-DD_` prefix is mandatory -- enables auto-prune (see step 14).
9. **Generate each of the 4 slides via Higgsfield MCP** -- one call per slide. Model: `nano_banana_pro`, `aspect_ratio: "4:5"`, `resolution: "2k"`. Each prompt includes ALL text content + the mandatory line "The top-left corner MUST BE COMPLETELY EMPTY. No logo, no symbol, no mark." See [Skills/news-post-design.md §9](Skills/news-post-design.md) for the per-slide prompt structure.
10. **Download + resize each result** from native ~1856×2304 to 1080×1350 via PIL LANCZOS. Save as `slide{N}_{descriptor}.png` in the dated folder. Delete the raw download.
11. **Mandatory Visual QA** ([../../Skills/visual-qa.md](../../Skills/visual-qa.md)) -- open every PNG. Verify Spanish spelling (no `MENOS MENOS` duplications, no `Verifed` missing letters), all numerical stats, italic emphasis on right words, semaphore dot order (green/red/orange), empty top-left corner. **If any error → regenerate that slide with a refined Higgsfield prompt. Do NOT patch via HTML or PIL.**
12. **Draft the short caption** (1-3 lines) → save as `caption.txt`
13. **Present the complete carousel** + caption to the user
14. **Ask which slides are favorites** → `cp` to [Favoritos_Claude_Generated/](Favoritos_Claude_Generated/) with `{topic-slug}_{slide_name}.png` naming
15. **Run auto-prune (MANDATORY):**
    ```bash
    python Brand/prune_outputs.py news
    ```
    Keeps the 5 most-recent dated folders, deletes older ones. Favorites already saved in step 14 survive (they live in a separate folder). Historical pre-migration folders without a date prefix are never touched. See root CLAUDE.md §3.6.

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
