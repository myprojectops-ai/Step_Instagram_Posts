---
name: visual-posts-informativos
description: Create or edit dense informative Instagram posts in Visual_posts. Use for AI tips, hacks, lists, cheatsheets, rankings, mind maps, tool lists, prompt lists, infographics, save-worthy reference posts. Brand v2 (Roboto + Playfair Italic, scheme/mode aware, Higgsfield MCP).
---

# Informativos Posts (brand v2)

Use this skill for dense, save-worthy AI infographics and short informative carousels.

## Required References

Read these before production work:

1. `.codex/skills/visual-posts-core/SKILL.md`
2. `Brand/brand-spec.md`
3. `PostTypes/informativos/README.md`
4. `PostTypes/informativos/Skills/informativo-post-design.md`
5. `Skills/informativo-visual-iteration.md` -- for PIL/scipy alignment on organic compositions

## Workflow

1. Confirm type + color (AMARILLO/ROJO/AZUL) + mode (LIGHT/DARK).
2. Review `PostTypes/informativos/Inspiracion/` and every file in `PostTypes/informativos/Favoritos_Claude_Generated/`. (Note: `Brand/Templates/` does not currently include informativo templates -- rely on inspiration folder + brand-spec.)
3. Choose one layout pattern A-G (see Layout Patterns below).
4. Check `Logos/` and `Assets/Personas/` for required assets. Generate missing ones via Higgsfield if needed.
5. Propose title, layout, items/sections, and caption. Wait for approval before generating the composition image.
6. Generate **one** composition via `mcp__higgsfield__generate_image` and save it as `composition.png` in the post output folder. Use the prompt template for the chosen layout from `PostTypes/informativos/Skills/informativo-post-design.md §4`.
7. Present the composition for approval. Only regenerate if rejected.
8. For organic compositions (mind maps, blob layouts): run scipy connected-component analysis to find exact text positions (`Skills/informativo-visual-iteration.md §0`). For grid layouts (numbered list, grid cards, tier list, cheatsheet, comparison): compute positions deterministically from the prompt structure.
9. Overlay text with PIL (organic compositions) or HTML+CSS (grid compositions). Use Roboto + Playfair Italic from `Brand/Fonts/`.
10. Run the self-iteration loop (`Skills/informativo-visual-iteration.md §2`) -- max 5 attempts to align text correctly before presenting.
11. Inspect every final PNG (Visual QA).
12. Save caption as `caption.txt`.
13. Present output and ask for favorites.
14. **Auto-prune:** run `python Brand/prune_outputs.py informativos` to keep only the 5 most-recent dated folders. See CLAUDE.md §3.6.

**Folder naming note:** all informativo output folders MUST be named `YYYY-MM-DD_{topic-slug}/`. The date prefix enables auto-prune. Replace step 4's mkdir command with `mkdir -p "PostTypes/informativos/Outputs/$(date +%Y-%m-%d)_{topic-slug}"`.

## Layout Patterns

- **A:** Numbered list (vertical cards)
- **B:** Grid cards (3×3 / 2×3 / 2×2)
- **C:** Tier list / Pyramid
- **D:** Mind map / Radial diagram
- **E:** Sectioned cheatsheet (dense grid)
- **F:** Single feature / Hero card
- **G:** Comparison / Before-After

Per-layout prompt templates live in `PostTypes/informativos/Skills/informativo-post-design.md §4`.

## Composition Rules (Higgsfield)

- Composition uses mode-appropriate background (cream LIGHT / warm-dark DARK).
- Composition contains empty zones for text overlay.
- Composition contains **no text, letters, numbers, typography, or watermarks** -- always end the prompt with "no text anywhere".
- Generate **one** composition only unless the user rejects it.
- Aspect ratio: always `--ar 4:5`.
- Use a stable `--seed` if this is part of a multi-slide carousel.
- Category colors are allowed for differentiation (tier list, multi-tool lists), max **5 distinct colors per slide**.

## Text Overlay Rules

- Use Roboto + Playfair Italic fonts from `Brand/Fonts/`. Do not use `Assets/Fonts/Inter` (legacy).
- For HTML overlays: `@font-face` block with relative paths from the output HTML's location (typically `../../../../Brand/Fonts/...`).
- For PIL overlays: `ImageFont.truetype("Brand/Fonts/Roboto/static/Roboto-Bold.ttf", size)` etc.
- Do not use stale `C:/Visual_posts` paths -- workspace is `C:/Trabajo_AI/Visual_posts`.
- For organic blobs/cards, find exact text zones with connected-component analysis rather than guessing coordinates.
- Verify all text is readable at reduced size and stays inside its visual zone.
- Highlight color on emphasis words MUST match the chosen scheme (`#ffb050` AMARILLO / `#e60000` ROJO / `#0056a6` AZUL).
- Numbers in titles are almost always italicized with Playfair Italic in the scheme color.

## Content Rules

- Make the post specific and useful; avoid generic filler.
- Use a number in the title when natural ("9 reglas", "Top 7", "5 hacks").
- Minimum body text size is 16 px.
- **No Alta Studio watermark** on informativos (that's news-only).
- Use `@lucianomusellaa` at the bottom (informativos use the handle, unlike news).
- **No page dots** on slides.
- Colombian Spanish only (`tú` form, no voseo).
