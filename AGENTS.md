# Visual_posts -- Codex Operating Guide (brand v2)

This repository generates Instagram posts for `@lucianomusellaa`. It is operated from both Claude Code (via `CLAUDE.md`) and Codex CLI (via this file + `.codex/skills/`). Both agents follow the same brand visual system documented in [`Brand/brand-spec.md`](Brand/brand-spec.md).

> **Brand v2 migration completed 2026-05-22.** All references in this guide reflect the new brand system: Roboto + Playfair Display Italic typography, dual-mode palette with three color schemes (AMARILLO/ROJO/AZUL), and Higgsfield MCP as the sole image generator. Outputs created before the migration are historical and must not be re-rendered.

## Required Startup

For every new post request:

1. **Ask the user to confirm three things** before any production work:

   `Para arrancar necesito tres cosas: (a) Tipo de post: (1) step-by-step, (2) news, o (3) informativo. (b) Esquema de color: AMARILLO, ROJO, o AZUL. (c) Modo: LIGHT o DARK.`

2. **Read [Brand/brand-spec.md](Brand/brand-spec.md)** -- canonical palette, fonts, and slide patterns.

3. **Read the matching Codex skill:**
   - `.codex/skills/visual-posts-step-by-step/SKILL.md`
   - `.codex/skills/visual-posts-news/SKILL.md`
   - `.codex/skills/visual-posts-informativos/SKILL.md`

4. **Read `.codex/skills/visual-posts-core/SKILL.md`** for global visual QA, spacing, render, and asset rules.

5. **Re-anchor visually before generating anything:** open `Brand/Templates/{Tutorial|Noticias}/` matching the user's chosen color + mode, then inspect the selected post type's `Inspiracion/` and all current files in `Favoritos_Claude_Generated/`.

## Project Shape

- `CLAUDE.md`: master router for Claude Code.
- `AGENTS.md`: this file -- master router for Codex CLI.
- `Brand/`: canonical brand system (palette PDF, fonts, templates, brand-spec.md).
- `Skills/`: global rules (visual QA, spacing, informativo visual iteration).
- `PostTypes/{type}/Skills/`: per-type visual specs.
- `PostTypes/{type}/Inspiracion/`: external references to review before new work.
- `PostTypes/{type}/Favoritos_Claude_Generated/`: user-approved favorites to review before new work.
- `PostTypes/{type}/Outputs/{topic-slug}/`: generated HTML, PNGs, photos, captions.
- `Logos/`: shared brand assets (Alta Studio LIGHT + DARK variants, third-party logos).
- `Assets/Personas/`: real person photos.
- `Assets/Fonts/`: LEGACY (Inter) -- not used by v2 brand. Reference only.
- **Image generation: Higgsfield MCP only.** Register via `claude mcp add --transport http --scope user higgsfield https://mcp.higgsfield.ai/mcp`. OAuth on first tool invocation. Tools: `mcp__higgsfield__generate_image`, etc.
- `render.sh`: required HTML to PNG renderer.
- `.codex/skills/`: Codex-native skill wrappers for this project.

## Non-Negotiable Brand Rules

- Use Colombian Spanish with `tú`, never Argentinian voseo.
- Use `@lucianomusellaa` on tutorial covers + closings, and on informativos (at the bottom). **Do NOT use** `@lucianomusellaa` on news slides or interior tutorial step slides; news uses Alta Studio logo, interior steps go without handle.
- Canvas is always 1080 × 1350 px unless generating intermediate assets at a documented ratio (4:5 covers / 16:9 body photos / 1:1 avatars).
- **Visual identity per the new brand:**
  - Light mode bg: `#efedec` / `#e6ecee` / `#ffffff`
  - Dark mode bg: `#11191b` / `#0c1314` / `#000000` (plus navy `#00386e`/`#0056a6` for gradient accents)
  - Highlight per scheme: AMARILLO `#ffb050` / ROJO `#e60000` / AZUL `#0056a6`
  - Fonts: Roboto + Playfair Display Italic (only italic, for 1-2 emphasis words per headline)
- **No page dots / carousel indicators on slides** -- Instagram handles pagination natively.
- Do not use Codex image tool, gpt-image-1, or any other generator. Higgsfield MCP only.
- Before presenting output, visually inspect rendered PNGs. Do not describe a visual detail that has not been verified in the image.

## Codex Tool Translation

- Claude's "Read image" → Codex `view_image` for local PNG/JPG/WebP references.
- Claude's "WebSearch" → Codex web tool. News facts, current announcements, and real tweets must be verified online.
- Claude's "Bash" examples may need PowerShell or Git Bash adaptation in this Windows workspace.
- Prefer `rg` / `rg --files` for repo search.
- Use `apply_patch` for manual edits.
- Use `render.sh` for HTML renders; do not call Chrome manually unless explicitly debugging `render.sh`.
- Higgsfield MCP tools are surfaced through MCP -- invoke `mcp__higgsfield__generate_image` directly.

## Render And QA

Render with:

```bash
./render.sh PostTypes/{type}/Outputs/{topic-slug}
```

or single file:

```bash
./render.sh PostTypes/{type}/Outputs/{topic-slug}/slide.html
```

After every render, visually inspect every PNG before presenting it. Verify per [`Skills/visual-qa.md`](Skills/visual-qa.md):

- exact 1080 × 1350 output
- no clipped bottom elements
- no broken images/logos
- readable contrast for the chosen mode
- fonts loaded (Roboto + Playfair Italic, NOT system fallback)
- correct handle/logo rules per post type
- highlight color matches chosen scheme
- Colombian Spanish

## Post-Type Routing

### Step-By-Step

Use `.codex/skills/visual-posts-step-by-step/SKILL.md`.

### News

Use `.codex/skills/visual-posts-news/SKILL.md`. **4-slide carousel** (cover / body / stat card / verdict).

### Informativos

Use `.codex/skills/visual-posts-informativos/SKILL.md`. **7 layout patterns** with Higgsfield full composition + HTML/PIL text overlay.

## Known Migration Risks

- Historical outputs in `PostTypes/*/Outputs/` were generated under the previous brand (cream/coral/Inter) and reference fonts/colors no longer in the system. **Treat them as a read-only archive. Do not re-render.** If asked to update an old post, ask the user whether to create a new v2 version in a sibling folder.
- Some scripts in `.codex/` or legacy files may still reference `Codex image tool`, `gpt-image-1`, `Inter`, `cream #F5F2ED`, `coral #E85D3C`, etc. These are deprecated -- replace operationally with Higgsfield MCP + brand v2 tokens.
- `render.sh` assumes Git Bash style paths and Chrome at `/c/Program Files/Google/Chrome/Application/chrome.exe`.
- README/spec text may render with mojibake in PowerShell output. Do not "fix" accents blindly; preserve UTF-8 content when editing.
- Higgsfield MCP first invocation triggers OAuth in browser. On a fresh machine, the user must complete this once before image generation will work.

## Delivery Convention

At the end of a post run, ask:

`¿Cuáles imágenes de este post son tus favoritas? Las guardo en Favoritos_Claude_Generated para usarlas como referencia en posts futuros.`

Copy selected PNGs into the correct `Favoritos_Claude_Generated/` folder. Use `cp` (copy), never `mv` (move).
