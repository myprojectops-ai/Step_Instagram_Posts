---
name: visual-posts-core
description: Core operating rules for this Visual_posts repository (brand v2). Use when Codex is creating, migrating, rendering, QAing, or editing Instagram post assets in this project, regardless of post type.
---

# Visual Posts Core (brand v2)

Use this skill for all work in `c:/Trabajo_AI/Visual_posts`. It defines the shared rules; post-type skills add the specific workflow.

> **Brand v2 migration completed 2026-05-22.** Roboto + Playfair Italic typography, three color schemes (AMARILLO/ROJO/AZUL), two modes (LIGHT/DARK), Higgsfield MCP as sole image generator. Historical outputs are immutable.

## Load Order

1. Read `AGENTS.md`.
2. Read `Brand/brand-spec.md` (canonical palette, fonts, slide patterns).
3. Read this skill.
4. Read the selected post-type skill in `.codex/skills/`.
5. Read the detailed original specs linked by that skill.

## Mandatory First Move

Before any production work, ask the user to confirm three things:

`Para arrancar necesito tres cosas: (a) Tipo de post: (1) step-by-step, (2) news, o (3) informativo. (b) Esquema de color: AMARILLO, ROJO, o AZUL. (c) Modo: LIGHT o DARK.`

## Global Rules

- Use Colombian Spanish with `tú`; never use voseo.
- Use 1080 × 1350 px output for final posts.
- Keep generated source and rendered PNGs in `PostTypes/{type}/Outputs/YYYY-MM-DD_{topic-slug}/`. **Folder name MUST start with `YYYY-MM-DD_` prefix** (today's date) so the auto-prune step works.
- Review `Brand/Templates/{Tutorial|Noticias}/{COLOR}/{MODE}/`, `Inspiracion/`, and `Favoritos_Claude_Generated/` before every new post.
- Ask which rendered images are favorites at the end and copy selected PNGs to the post type's `Favoritos_Claude_Generated/`.
- **Auto-prune to keep last 5 posts per type:** after favorites are saved, run `python Brand/prune_outputs.py {type}`. Keeps top 5 dated folders, deletes older. Favorites + historical pre-migration folders (no date prefix) are never touched. See CLAUDE.md §3.6.
- **Historical Outputs/ are immutable** -- never re-render posts from before 2026-05-22.
- **No page dots on slides** -- Instagram handles carousel pagination natively.

## Brand Visual System (v2)

- **Canvas:** 1080 × 1350 px (4:5 portrait)
- **Mode (LIGHT or DARK):** asked per post -- drives bg + text base
  - LIGHT bg: `#efedec` / `#e6ecee` / `#ffffff`; text `#0c1314` / `#11191b` / `#000000`
  - DARK bg: `#11191b` / `#0c1314` / `#000000` / `#00386e`; text `#ffffff` / `#e6ecee` / `#c9d7da`
- **Color scheme (AMARILLO/ROJO/AZUL):** asked per post -- drives highlight color
  - AMARILLO: primary `#ffb050`, solid `#ff9d00`, light `#ffc47f`
  - ROJO: primary `#e60000`, solid `#c30000`, light `#ff0000`
  - AZUL: primary `#0056a6`, solid `#00386e`, light `#c9d7da` (soft)
- **Fonts:** Roboto (400/500/700/900) + Playfair Display Italic (1-2 emphasis words per headline only)
- **`@font-face` block:** local TTFs from `Brand/Fonts/` -- no Google Fonts CDN. Canonical block lives in `Brand/brand-spec.md §2`.

## Tool Translation For Codex

- Use `view_image` to inspect local reference PNG/JPG/WebP files.
- Use the web tool for news verification and official tweets.
- Use `apply_patch` for manual file edits.
- Use `rg` and `rg --files` for search.
- Use `render.sh`; do not hand-write Chrome commands.

## Render

Render all HTML in a folder:

```bash
./render.sh PostTypes/{type}/Outputs/{topic-slug}
```

Render one file:

```bash
./render.sh PostTypes/{type}/Outputs/{topic-slug}/slide.html
```

If running from PowerShell, invoke through Git Bash if needed:

```powershell
bash render.sh PostTypes/{type}/Outputs/{topic-slug}
```

## Visual QA

After every render, inspect every PNG before presenting it.

Check:
- Final image is 1080 × 1350
- No white/black strips at edges
- Fonts loaded (Roboto + Playfair Italic, NOT system fallback)
- Logos/photos loaded
- Bottom elements are visible
- Text is readable and not clipped
- Handle/logo rules match the post type (handle on tutorials + informativos; Alta Studio logo on news; no handle on interior tutorial steps)
- Highlight color matches the chosen scheme on every emphasis word
- No page dots
- Spanish is Colombian (no voseo)

Read `Skills/visual-qa.md` and `Skills/slide-spacing.md` when implementing or debugging layout.

## Assets

- `Brand/Templates/` is the canonical visual ground truth -- always check first.
- `Brand/Fonts/` contains Roboto + PlayfairDisplay TTFs for HTML (@font-face) and PIL.
- `Logos/` is the first place to check for brand assets:
  - `Alta_Studio_logo.png` -- LIGHT mode
  - `Alta_Studio_logo_white.png` -- DARK mode
  - `Claude_AI_symbol.svg`, third-party brand logos
- `Assets/Personas/` stores real person photos.
- `Assets/Fonts/` (Inter) is LEGACY -- not used by v2 brand.
- Prefer relative paths from the generated HTML/script location.

## Image Generation -- Higgsfield MCP (sole image generator)

> **Codex image tool, gpt-image-1, and any other image generator are deprecated.** All images go through Higgsfield MCP.

Setup (one-time):
```
claude mcp add --transport http --scope user higgsfield https://mcp.higgsfield.ai/mcp
```
First tool invocation opens browser-based OAuth -- log in with the paid Higgsfield account.

Tools exposed:
- `mcp__higgsfield__generate_image` -- single image (Soul 2.0 / Nano Banana Pro / Flux 2 / etc.)
- `mcp__higgsfield__generate_video` -- video (not used in this project today)
- `mcp__higgsfield__balance` -- credits remaining

Use Higgsfield for: news cover photos (4:5), news body photos (16:9), informativo compositions (4:5), missing brand logos (1:1), missing person photos (4:5). Step-by-step posts use Higgsfield ONLY for missing logos -- all other tutorial content is HTML+CSS+SVG.

Prompt anatomy lives in `Brand/brand-spec.md §4`. Always include negative directive ("no text, no logos") + explicit aspect ratio + stable seed for carousel consistency.

## Original References

Use these for detailed constraints:

- `CLAUDE.md`
- `Brand/brand-spec.md`
- `Skills/visual-qa.md`
- `Skills/slide-spacing.md`
- `Skills/informativo-visual-iteration.md`
- `render.sh`
