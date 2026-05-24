# Informativos posts -- hacks, tips, listas, infografías (brand v2)

> **Skills are ready.** The design system is defined in [`Skills/informativo-post-design.md`](Skills/informativo-post-design.md). The brand visual system lives in [`Brand/brand-spec.md`](../../Brand/brand-spec.md). Read both before generating any informativo.

## What this type is for

Standalone informative posts: AI hacks, prompts útiles, tips sueltos, listas de herramientas, "did you know" content, mini-cheatsheets, tier lists, infographics. The viewer doesn't need to *do* the steps -- they're consuming **reference content worth saving**.

Differences vs the other types:

| | Step-by-step | News | **Informativo** |
|---|---|---|---|
| Goal | Teach a process | Report a fact | **Deliver save-worthy reference info** |
| Format | Carousel (6 slides typical) | Carousel (4 slides) | **Single image or short carousel (1-4)** |
| Density | Low -- 1 focal point per slide | Low -- photo + headline | **HIGH -- many items, icons, cards** |
| Visual generation | HTML+CSS+SVG | Higgsfield photo + HTML overlay | **Higgsfield full composition + HTML/PIL text overlay** |
| Labels | `TUTORIAL · PASO 0X` eyebrow | None | **Numbered items, section headers, category badges** |

## Trigger phrases

- "post informativo de {tema}"
- "post de hacks de {tema}"
- "post de tips para {tema}"
- "post tipo lista sobre {tema}"
- "5 prompts para {tema}" / "10 herramientas de {tema}"
- "infografía de {tema}"
- "tier list de {tema}"
- "cheatsheet de {tema}"

## Skills to load (in order)

1. [Brand/brand-spec.md](../../Brand/brand-spec.md) -- canonical palette, fonts, slide patterns
2. [Skills/informativo-post-design.md](Skills/informativo-post-design.md) -- 7 layout patterns + composition prompts + overlay scaffold
3. [../../Skills/informativo-visual-iteration.md](../../Skills/informativo-visual-iteration.md) -- mandatory self-iteration loop with scipy blob detection for organic compositions
4. [../../Skills/visual-qa.md](../../Skills/visual-qa.md) -- mandatory post-render QA
5. [../../Skills/slide-spacing.md](../../Skills/slide-spacing.md) -- universal spacing rules

Also read the brand-wide rules in the root [`CLAUDE.md`](../../CLAUDE.md) -- they apply to all post types.

## Workflow summary (updated 2026-05-23: single-step Higgsfield, no HTML overlay)

1. Confirm type + color + mode (CLAUDE.md §1)
2. Read brand-spec → skill → visual-qa
3. **Mandatory visual re-anchoring** -- review `Inspiracion/` AND `Favoritos_Claude_Generated/` (CLAUDE.md §1.5)
4. Understand the topic and choose a layout pattern (A-G in the skill)
5. Check `Logos/` and `Assets/` for needed brand assets
6. Propose content breakdown → wait for user approval
7. **Create the dated output folder:**
   ```bash
   mkdir -p "PostTypes/informativos/Outputs/$(date +%Y-%m-%d)_{topic-slug}"
   ```
   The `YYYY-MM-DD_` prefix is mandatory.
8. **Generate the complete image via Higgsfield MCP** (`mcp__higgsfield__generate_image`) -- one call with ALL text + visuals baked into the prompt. Model: `nano_banana_pro`, `aspect_ratio: "4:5"`, `resolution: "2k"`. The prompt includes title (with italic emphasis word styling), subtitle, each item's number + name + description, and `@lucianomusellaa` handle at the bottom. See `Skills/informativo-post-design.md §4` for the canonical template.
9. **Download + resize** from native ~1856×2304 to 1080×1350 via PIL LANCZOS. Save as the final deliverable PNG in the dated folder.
10. **Visual QA** -- read the PNG and verify spelling + layout. If broken, regenerate with a refined prompt. Do NOT patch via HTML.
11. Present to user
12. Ask for favorites → `cp` to `Favoritos_Claude_Generated/` with `{topic-slug}_{name}.png` naming
13. **Run auto-prune (MANDATORY):**
    ```bash
    python Brand/prune_outputs.py informativos
    ```
    Keeps the 5 most-recent dated folders. Favorites and historical pre-migration folders are exempt. See root CLAUDE.md §3.6.

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
│   └── informativo-post-design.md   ← the visual system + layouts + prompts
├── Inspiracion/                     ← user-provided reference images
│   └── Inspo_01.png ... Inspo_13.png
├── Favoritos_Claude_Generated/      ← past slides the user marked as favorites
└── Outputs/                         ← rendered informativo posts
    └── {topic-slug}/                ← one folder per post
        ├── composition.png              ← Higgsfield visual (no text)
        ├── info_v1_{descriptor}.html    ← HTML text overlay
        ├── info_v1_{descriptor}.png     ← Final rendered (composition + text)
        ├── caption.txt
        └── ...
```

## Brand-wide rules that apply

- **Always ask the user to confirm type + color + mode** (CLAUDE.md §1)
- **Mandatory visual re-anchoring** (CLAUDE.md §1.5)
- **After every post, ask which images are favorites** (CLAUDE.md §1.6)
- **Colombian Spanish, `tú` form** -- never Argentinian voseo
- **Higgsfield MCP generates the full visual composition** (background, layout, icons, logos -- NO text). HTML/PIL overlay adds all text.
- **Brand logos:** from `Logos/` first; generated via Higgsfield if missing -- always user-reviewed
- **No Alta Studio watermark** -- that's news-only
- **`@lucianomusellaa` handle present** at bottom (informativos use it; news doesn't)
- **No page dots** -- Instagram handles pagination
- **Variety is essential** -- posts must follow the same aesthetic but NOT all look the same
