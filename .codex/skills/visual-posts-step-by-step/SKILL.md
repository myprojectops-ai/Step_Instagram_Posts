---
name: visual-posts-step-by-step
description: Create or edit step-by-step Instagram tutorial carousels in Visual_posts. Use for tutorial, how-to, paso a paso, carousel walkthrough, cover, step slide, closing CTA. Brand v2 system (Roboto + Playfair Italic, scheme/mode aware).
---

# Step-By-Step Posts (brand v2)

Use this skill for tutorial/how-to carousels: cover → PASO 0X slides → closing CTA.

## Required References

Read these before creating or editing slides:

1. `.codex/skills/visual-posts-core/SKILL.md`
2. `Brand/brand-spec.md`
3. `PostTypes/step-by-step/README.md`
4. `PostTypes/step-by-step/Skills/instagram-post-design.md`
5. `PostTypes/step-by-step/Skills/instagram-cover-design.md`
6. `PostTypes/step-by-step/Skills/instagram-step-slide-design.md`
7. `PostTypes/step-by-step/Skills/instagram-dark-mode.md` (only if user chose DARK mode)

## Workflow

1. Confirm type + color (AMARILLO/ROJO/AZUL) + mode (LIGHT/DARK).
2. **Open `Brand/Templates/Tutorial/{COLOR}/{STYLE}/{MODE}/`** and view at least 2 reference PNGs.
3. Review at least 2 images in `PostTypes/step-by-step/Inspiracion/`.
4. Review all PNGs in `PostTypes/step-by-step/Favoritos_Claude_Generated/`.
5. List `Logos/` and check whether required brands already exist.
6. Gather missing context (slides count, source material, emphasis word, screenshots).
7. Propose the full carousel breakdown in text and wait for approval.
8. Generate any missing brand logos via `mcp__higgsfield__generate_image`. Save to `Logos/` after user review.
9. Create `PostTypes/step-by-step/Outputs/$(date +%Y-%m-%d)_{topic-slug}/`. **Folder MUST start with `YYYY-MM-DD_` prefix.**
10. Write HTML files using scaffolds from the per-type skills + canonical `@font-face` block from `Brand/brand-spec.md`.
11. Render with `render.sh`.
12. Inspect every PNG (Visual QA).
13. Present the carousel and offer precise iterations.
14. Ask which images are favorites; copy selected PNGs to `Favoritos_Claude_Generated/` with `cp` (never `mv`).
15. **Auto-prune:** run `python Brand/prune_outputs.py step-by-step` to keep only the 5 most-recent dated folders. See CLAUDE.md §3.6.

Do not write production HTML before the user approves the breakdown.

## Visual Rules (brand v2)

- **Background per mode:** LIGHT `#efedec` (flat) or LIGHT gradient variants; DARK `#11191b` or DARK gradient variants. Match the chosen template subfolder.
- **`@lucianomusellaa` placement:** on the COVER (top center) and the CLOSING slide (top center). Interior step slides do NOT show the handle.
- **Fonts:** Roboto (Regular/Medium/Bold/Black) for body and headlines; **Playfair Display Italic** for exactly 1 emphasis word per headline.
- **Emphasis word color:** scheme highlight color (`#ffb050` AMARILLO / `#e60000` ROJO / `#0056a6` AZUL).
- **Cover headline:** 1 word in Playfair Italic scheme color. Optional solid pill ("en X pasos") below.
- **Step slide eyebrow:** `TUTORIAL · PASO 0X` (zero-padded 2-digit) in scheme highlight color, ALL CAPS, letter-spacing 2px.
- **Step slide headline:** 1 word in Playfair Italic scheme color (same pattern as cover, shorter overall).
- **No page dots / carousel indicators** -- Instagram handles pagination natively.
- **No solid pill on step slides** (cover only).
- **Closing slide:** mascot/icon + lowercase big text + thin divider + ONE-WORD CTA pill in ALL CAPS + caption. No `Desliza`, no eyebrow.
- **All slides use the same scheme + same mode** -- no half-and-half carousels.
- **Terminal mockups** for code/CLI content; **orgchart cards** for delegation tutorials; real or recreated screenshots for UI tutorials.

## Naming

- Cover variations: `cover_v{n}_{descriptor}.html`
- Step slides: `paso_{n}_{descriptor}.html`
- Closing slide: `cierre_cta.html`
- Rendered PNGs sit beside their HTML.

## Image generation

Step-by-step uses Higgsfield MCP **only for missing brand logos**. All other slide visuals (terminal mockups, orgcharts, illustrations) are HTML+CSS+inline SVG. See `Brand/brand-spec.md §4` for prompt anatomy when generating a logo via `mcp__higgsfield__generate_image`.
