# Informativos posts â€” hacks, tips, listas, infografÃ­as

> **Skills are READY.** The design system is defined in [`Skills/informativo-post-design.md`](Skills/informativo-post-design.md). Read it before generating any informativo.

## What this type is for

Standalone informative posts: AI hacks, prompts Ãºtiles, tips sueltos, listas de herramientas, "did you know" content, mini-cheatsheets, tier lists, infographics. The viewer doesn't need to "do" the steps â€” they're consuming **reference content worth saving**.

Differences vs the other types:

| | Step-by-step | News | **Informativo** |
|---|---|---|---|
| Goal | Teach a process | Report a fact | **Deliver save-worthy reference info** |
| Format | Carousel (6â€“8 slides) | Single image | **Single image or short carousel (1â€“4)** |
| Density | Low â€” 1 focal point | Low â€” photo + headline | **HIGH â€” many items, icons, cards** |
| Background | Cream + grid | Dark photo | **Codex image tool composition** (cream-based) |
| Labels | "PASO X" | "AI NEWS" badge | **Numbered items, section headers** |

## Trigger phrases

- "post informativo de {tema}"
- "post de hacks de {tema}"
- "post de tips para {tema}"
- "post tipo lista sobre {tema}"
- "5 prompts para {tema}" / "10 herramientas de {tema}"
- "infografÃ­a de {tema}"
- "tier list de {tema}"
- "cheatsheet de {tema}"

## Skills to load

1. **[`Skills/informativo-post-design.md`](Skills/informativo-post-design.md)** â€” the complete visual system (layouts, palette, scaffolds, workflow)
2. **[`../../Skills/visual-qa.md`](../../Skills/visual-qa.md)** â€” mandatory post-render verification (global skill)

Also read the brand-wide rules in the root [`CLAUDE.md`](../../CLAUDE.md) â€” they apply to all post types.

## Workflow summary

1. Confirm post type with the user (CLAUDE.md section 1)
2. Load this README â†’ load the skill file â†’ load visual-qa
3. **Mandatory visual re-anchoring** â€” review `Inspiracion/` AND `Favoritos_Claude_Generated/` (CLAUDE.md section 1.5)
4. Understand the topic and choose a layout pattern (Aâ€“G in the skill)
5. Check `Logos/` and `Assets/` for needed brand assets
6. Propose content breakdown â†’ wait for user approval
7. Draft caption (no approval needed)
8. **Generate ONE visual composition with Codex image tool** â€” the full visual (background, layout structure, icons, logos, decorative elements â€” NO text). Present to user for approval.
9. **Generate HTML text overlay** â€” use approved composition as `background-image`, position all text to align with the visual structure
10. Render via `./render.sh` â†’ Visual QA (inspect every PNG)
11. Present rendered image(s) + caption to user
12. Ask for favorites â†’ save to `Favoritos_Claude_Generated/`

## Layout patterns available

| Pattern | Name | Best for |
|---|---|---|
| A | Numbered list | "Top N...", tip lists, tool rankings |
| B | Grid cards | Tips with explanations, rule sets |
| C | Tier list / Pyramid | Rankings, hierarchies, capability layers |
| D | Mind map / Radial | Central concept with spokes |
| E | Sectioned cheatsheet | Reference cards, multi-section guides |
| F | Single feature / Hero card | One killer prompt, one hack, high impact |
| G | Comparison / Before-After | X vs Y, con/sin IA |

## Folder layout

```
PostTypes/informativos/
â”œâ”€â”€ README.md                        â† this file
â”œâ”€â”€ Skills/
â”‚   â””â”€â”€ informativo-post-design.md   â† the visual system
â”œâ”€â”€ Inspiracion/                     â† user-provided reference images
â”‚   â””â”€â”€ Inspo_01.png ... Inspo_13.png
â”œâ”€â”€ Favoritos_Claude_Generated/      â† past slides the user marked as favorites
â””â”€â”€ Outputs/                         â† rendered informativo posts
    â””â”€â”€ {topic-slug}/               â† one folder per post
        â”œâ”€â”€ composition.png              â† Codex image tool visual (no text)
        â”œâ”€â”€ info_v1_{descriptor}.html    â† HTML text overlay
        â”œâ”€â”€ info_v1_{descriptor}.png     â† Final rendered (composition + text)
        â”œâ”€â”€ caption.txt
        â””â”€â”€ ...
```

## Brand-wide rules that apply

- **Always ask the user to confirm the post type** before starting (CLAUDE.md section 1)
- **Mandatory visual re-anchoring** (CLAUDE.md section 1.5)
- **After every post, ask which images are favorites** (CLAUDE.md section 1.6)
- **Colombian Spanish, tÃº form** â€” never Argentinian voseo
- **Codex image tool generates the full visual composition** (background, layout, icons, logos â€” NO text). HTML overlay adds all text.
- **Brand logos** from `Logos/` (existing) or generated with **Codex image tool** if missing â€” always user-reviewed
- **NO Alta Studio watermark** â€” that's news-only
- **Variety is essential** â€” posts must follow the same aesthetic but NOT all look the same

