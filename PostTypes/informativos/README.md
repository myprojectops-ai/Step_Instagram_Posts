# Informativos posts — hacks, tips, listas, infografías

> **Skills are READY.** The design system is defined in [`Skills/informativo-post-design.md`](Skills/informativo-post-design.md). Read it before generating any informativo.

## What this type is for

Standalone informative posts: AI hacks, prompts útiles, tips sueltos, listas de herramientas, "did you know" content, mini-cheatsheets, tier lists, infographics. The viewer doesn't need to "do" the steps — they're consuming **reference content worth saving**.

Differences vs the other types:

| | Step-by-step | News | **Informativo** |
|---|---|---|---|
| Goal | Teach a process | Report a fact | **Deliver save-worthy reference info** |
| Format | Carousel (6–8 slides) | Single image | **Single image or short carousel (1–4)** |
| Density | Low — 1 focal point | Low — photo + headline | **HIGH — many items, icons, cards** |
| Background | Cream + grid | Dark photo | **gpt-image-1 composition** (cream-based) |
| Labels | "PASO X" | "AI NEWS" badge | **Numbered items, section headers** |

## Trigger phrases

- "post informativo de {tema}"
- "post de hacks de {tema}"
- "post de tips para {tema}"
- "post tipo lista sobre {tema}"
- "5 prompts para {tema}" / "10 herramientas de {tema}"
- "infografía de {tema}"
- "tier list de {tema}"
- "cheatsheet de {tema}"

## Skills to load

1. **[`Skills/informativo-post-design.md`](Skills/informativo-post-design.md)** — the complete visual system (layouts, palette, scaffolds, workflow)
2. **[`../../Skills/visual-qa.md`](../../Skills/visual-qa.md)** — mandatory post-render verification (global skill)

Also read the brand-wide rules in the root [`CLAUDE.md`](../../CLAUDE.md) — they apply to all post types.

## Workflow summary

1. Confirm post type with the user (CLAUDE.md section 1)
2. Load this README → load the skill file → load visual-qa
3. **Mandatory visual re-anchoring** — review `Inspiracion/` AND `Favoritos_Claude_Generated/` (CLAUDE.md section 1.5)
4. Understand the topic and choose a layout pattern (A–G in the skill)
5. Check `Logos/` and `Assets/` for needed brand assets
6. Propose content breakdown → wait for user approval
7. Draft caption (no approval needed)
8. **Generate ONE visual composition with gpt-image-1** — the full visual (background, layout structure, icons, logos, decorative elements — NO text). Present to user for approval.
9. **Generate HTML text overlay** — use approved composition as `background-image`, position all text to align with the visual structure
10. Render via `./render.sh` → Visual QA (inspect every PNG)
11. Present rendered image(s) + caption to user
12. Ask for favorites → save to `Favoritos_Claude_Generated/`

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
├── README.md                        ← this file
├── Skills/
│   └── informativo-post-design.md   ← the visual system
├── Inspiracion/                     ← user-provided reference images
│   └── Inspo_01.png ... Inspo_13.png
├── Favoritos_Claude_Generated/      ← past slides the user marked as favorites
└── Outputs/                         ← rendered informativo posts
    └── {topic-slug}/               ← one folder per post
        ├── composition.png              ← gpt-image-1 visual (no text)
        ├── info_v1_{descriptor}.html    ← HTML text overlay
        ├── info_v1_{descriptor}.png     ← Final rendered (composition + text)
        ├── caption.txt
        └── ...
```

## Brand-wide rules that apply

- **Always ask the user to confirm the post type** before starting (CLAUDE.md section 1)
- **Mandatory visual re-anchoring** (CLAUDE.md section 1.5)
- **After every post, ask which images are favorites** (CLAUDE.md section 1.6)
- **Colombian Spanish, tú form** — never Argentinian voseo
- **gpt-image-1 generates the full visual composition** (background, layout, icons, logos — NO text). HTML overlay adds all text.
- **Brand logos** from `Logos/` (existing) or generated with **gpt-image-1** if missing — always user-reviewed
- **NO Alta Studio watermark** — that's news-only
- **Variety is essential** — posts must follow the same aesthetic but NOT all look the same
