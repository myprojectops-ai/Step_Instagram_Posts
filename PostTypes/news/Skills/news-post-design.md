---
name: news-post-design
description: Visual system for AI news Instagram posts — 5-slide carousel with gpt-image-1 photo compositions, HTML text overlays, and tweet slides. Covers, text+photo slides, and white-card slides on black editorial background.
type: skill
---

# News Post Design Skill

> **Project root:** `c:/Trabajo_AI/Visual_posts/`. The autoloaded **[`CLAUDE.md`](../../../CLAUDE.md)** at the project root contains the trigger phrases and routes to per-type workflows. The news workflow lives in [`../README.md`](../README.md). Read those for the *process*; read this skill for the *visual system*.

This skill defines the visual language for **AI news posts** — 5-slide Instagram carousels with a dark editorial feel, inspired by the references in [`../Inspiracion/`](../Inspiracion/) (Bridgemind-style accounts). The previous single-image + long-caption system is **deprecated** — news posts are now carousels.

---

## 0. What changed (and why)

| | Old system (deprecated) | New system |
|---|---|---|
| Format | Single image + long caption (6–10 paragraphs) | **5-slide carousel** (scalable to 7) + short caption (1–3 lines) |
| Cover render | Generated photo + PIL text overlay | gpt-image-1 photo + **HTML overlay via render.sh** |
| Body content | All in the caption | **Distributed across slides** (tweet + text + photo) |
| Alta Studio logo | Top-right (fixed position) | **One corner only** (top-left or top-right, composition-dependent) |
| Pipeline | PIL for text, render.sh for HTML | **Unified: render.sh for all slides, gpt-image-1 for all photos** |

**Why:** the carousel format is what AI news creators actually use on Instagram (see inspo). It's more visually engaging, each slide "earns its swipe", and people actually read digestible chunks instead of skipping long captions.

> **Viewport bug fix (2026-04-16):** Chrome headless on Windows subtracts ~96px from the `--window-size` height for window chrome decorations. The old `--window-size=1098,1368` caused content below y≈1272 to not render (pills, taglines were invisible). `render.sh` now uses `--window-size=1098,1550` and crops to 1080×1350 via PIL. If elements near the bottom of a slide appear missing in renders, this is the first thing to check.

---

## 1. Canvas & format

| Property | Value |
|---|---|
| Aspect ratio | **4:5 portrait** (Instagram feed optimal) |
| Resolution | **1080 × 1350 px** per slide |
| Format | **Carousel** — 5 slides default, 4–7 allowed |
| Safe margins | ~60 px on all sides for text |
| Background | **Pure black `#000000`** on all body slides (distinct from step-by-step cream) |

---

## 2. Color palette

News posts are **dark-first**. The photo is the hero on covers; black space is the hero on body slides.

| Role | Value | Use |
|---|---|---|
| Slide background | `#000000` | All body slides (tweet, text-with-photo, white-card) |
| Primary text (on dark) | `#FFFFFF` | Headlines, body copy on covers and dark body slides |
| Primary text (on card) | `#0E0E0E` | Body copy inside white cards |
| White card | `#FFFFFF` | Template B card, tweet card background |
| Accent coral | `#E85D3C` | Keyword highlight in headlines; small labels |
| Highlight yellow | `#FFE45C` | Yellow marker on keyword (rounded rect, dark text inside) |
| Muted white | `rgba(255,255,255,0.55)` | Taglines, source attributions |
| Gradient overlay (cover) | `linear-gradient(to top, rgba(0,0,0,0.95) 0%, rgba(0,0,0,0.88) 8%, rgba(0,0,0,0.72) 22%, rgba(0,0,0,0.35) 42%, transparent 62%)` | Bottom of cover — full-bleed photo with gradient for headline readability |

**Key rule:** white text must always sit over either (a) the dark portion of the cover gradient, (b) pure black body-slide background, or (c) inside a white card (in which case text is dark). Never white-on-photo without a gradient shield.

---

## 3. Typography

**Same family as all other post types** for brand consistency.

- **Family:** `'Inter', system-ui, -apple-system, sans-serif`
- **Import:** `https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap`
- **Code/data font:** `'JetBrains Mono', monospace` (for stat cards, numbers)

### Hierarchy

| Element | Font | Size | Weight | Color |
|---|---|---|---|---|
| **Cover headline** | Inter | 58–70 px | 800 | White + coral + yellow-marker spans |
| **Cover tagline** | Inter | 17–19 px | 600 | `rgba(255,255,255,0.75)`, ALL CAPS, letter-spacing 0.08em |
| **Body slide label** | Inter | 15 px | 700 | Coral `#E85D3C`, ALL CAPS, letter-spacing 0.14em |
| **Body slide text** | Inter | 34–42 px | 600 | White on dark, dark `#0E0E0E` on white card |
| **Tweet name** | Inter | 24 px | 700 | `#0F1419` |
| **Tweet handle** | Inter | 20 px | 400 | `#536471` |
| **Tweet body** | Inter | 30 px | 400 | `#0F1419`, line-height 1.4 |
| **Stat card number** | Inter | 180–240 px | 900 | Dark |
| **SWIPE pill** | Inter | 13 px | 700 | White on `rgba(255,255,255,0.12)`, letter-spacing 0.12em |

---

## 4. Slide taxonomy — the 5-slide default

Every news post follows this skeleton (deviations require user approval):

| # | Slide type | Purpose | Template |
|---|---|---|---|
| **1** | **Cover** | Hook: photo + killer headline | §5 |
| **2** | **Tweet / oficial** | Source of truth: reproduces the company or CEO's public announcement | §6 |
| **3** | **Text + photo** (Template A) | What happened — context in 2–3 short lines + supporting gpt-image-1 photo | §7 |
| **4** | **Text + photo** or **White card** | Why it matters — explanation with photo, OR punchline stat with white card | §7 or §8 |
| **5** | **Closer** | Reaction tweet (invented handle) OR stat card OR CTA | §6 or §8 |

### When to deviate

- **4 slides** — simple news (one fact, one consequence). Skip slide 4.
- **6 slides** — news with 2 distinct consequences. Add a second text+photo between 3 and 4.
- **7 slides** — complex news (announcement + reactions + data). Rare.
- **Never less than 4** — a 3-slide news post feels thin.

### Global elements across all body slides (not cover)

- **Alta Studio logo** top-left corner, **100px tall** (uniform across all 5 slides — cover, body, closer), opacity 0.98, with drop-shadow filter `drop-shadow(0 2px 14px rgba(0,0,0,.55))`. Position: `top:44px; left:50px`
- **No `@lucianomusellaa` handle** on news posts (editorial feel — replaced by Alta Studio logo)
- **Content positioning** — labels/cards/text blocks must start at `top: ≥170px` to clear the 100px-tall logo (which extends to y≈144 plus margin)

### What the cover does NOT have

- No Alta Studio in both corners — **only one**
- Instead: **SWIPE pill** bottom-right to signal carousel

---

## 5. Template: Cover slide

### Layout (full-bleed photo + CSS gradient overlay)

```
┌─────────────────────────────────────┐
│ [Alta]                              │  ← top-left, overlaps photo
│                                     │
│                                     │
│    GPT-IMAGE-1 PHOTO (4:5)          │  ← 1080 × 1350 px FULL BLEED
│    (shoe, scene, person, etc.)      │    fills entire canvas
│    editorial, cinematic,            │    subject in upper 60%
│    background-size: cover           │
│                                     │
│ ┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄ │  ← CSS gradient starts fading ~62%
│                                     │
│  TITULAR EN BOLD                    │  ← headline at top:860px (absolute)
│  CON PALABRAS RESALTADAS            │    over gradient-darkened zone
│  EN CORAL Y AMARILLO                │
│                                     │
│  TAGLINE          [SWIPE →]         │  ← bottom-row at top:1268px (absolute)
└─────────────────────────────────────┘
```

> **NOTE:** Headline and bottom-row are SEPARATE `position:absolute` elements on `<body>`, NOT nested inside each other. Chrome headless clips child content that extends beyond its parent's rendered height — nesting the bottom-row inside the headline block caused the SWIPE pill to be invisible. Independent positioning avoids this.

### gpt-image-1 prompt structure (cover photo)

```
Editorial cinematic photograph, vertical portrait composition, 4:5 aspect ratio.
[SCENE/PERSON description — position subject in the UPPER portion of the frame, leave lower 40% as open/dark space for text overlay].
Dramatic lighting, subtle film grain, slightly desaturated editorial tones.
Portrait format, magazine cover quality, vertical framing.
No text, no typography, no logos, no words, no watermarks anywhere in the image.
```

**Prompt rules:**
- **Always end with** "No text, no typography, no logos, no words anywhere" — image models love to add text
- Use `--aspect-ratio 4:5` (outputs 1080×1350 after internal crop+resize). Cover photos are **full-bleed** — they fill the entire canvas edge to edge. A CSS gradient overlay darkens the bottom for text readability
- **Position the subject in the upper portion** of the frame — the bottom 40% will be darkened by the gradient, so important details should sit above ~y=540. The default `--crop top` preserves the upper portion if any trim is needed
- Describe the scene, not the frame: avoid "cover photo", "Instagram post", etc.
- Include **"film grain"** or "editorial photography" — avoids the plastic AI look
- **For real public figures** (Altman, Amodei, Pichai, Zuck) — OpenAI's content policy is stricter than Gemini's and will likely reject named real people. Describe by features, role, and setting instead: "a bearded tech CEO in a grey t-shirt at a Senate hearing" rather than "Sam Altman". If a prompt fails with `content_policy_violation`, rephrase as "a person who looks like X" or check `Assets/Personas/` for an existing reference photo
- For invented roles (researchers, analysts, workers) — describe demographics + context naturally

**Generate ONE cover photo.** Present to user. Only regenerate if rejected.

### Cover HTML scaffold

Save as `slide1_cover.html` in the post's output folder. The `composition.png` (gpt-image-1 4:5 output) must be in the same folder.

```html
<!DOCTYPE html>
<html lang="es"><head><meta charset="UTF-8">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
<style>
  *{margin:0;padding:0;box-sizing:border-box}
  body{width:1080px;height:1350px;font-family:'Inter',system-ui,sans-serif;overflow:hidden;position:relative;background:#000}
  .photo{position:absolute;top:0;left:0;right:0;bottom:0;background-image:url('composition.png');background-size:cover;background-position:center center}
  .gradient{position:absolute;top:0;left:0;right:0;bottom:0;background:linear-gradient(to top, rgba(0,0,0,0.95) 0%, rgba(0,0,0,0.88) 8%, rgba(0,0,0,0.72) 22%, rgba(0,0,0,0.35) 42%, transparent 62%);z-index:2}
  .alta{position:absolute;top:44px;left:50px;height:100px;opacity:.98;z-index:10;filter:drop-shadow(0 2px 14px rgba(0,0,0,.55))}
  /* IMPORTANT: headline and bottom-row are SEPARATE absolute elements, NOT nested.
     Chrome headless clips children that extend beyond parent's rendered height. */
  .headline{position:absolute;top:860px;left:60px;right:60px;z-index:10;font-size:64px;font-weight:800;line-height:1.1;color:#fff;letter-spacing:-.012em;text-transform:uppercase}
  .headline .coral{color:#E85D3C}
  .headline .yellow{background:#FFE45C;color:#0E0E0E;padding:0 12px 5px 12px;border-radius:6px;display:inline-block;line-height:1}
  .bottom-row{position:absolute;top:1268px;left:60px;right:60px;z-index:10;display:flex;justify-content:space-between;align-items:center;gap:24px}
  .tagline{font-size:16px;font-weight:600;color:rgba(255,255,255,.72);text-transform:uppercase;letter-spacing:.1em;line-height:1.4;flex:1}
  .swipe{background:#fff;padding:13px 24px;border-radius:999px;color:#0E0E0E;font-size:14px;font-weight:800;letter-spacing:.18em;text-transform:uppercase;white-space:nowrap;box-shadow:0 4px 18px rgba(0,0,0,.55)}
</style></head>
<body>
  <div class="photo"></div>
  <div class="gradient"></div>
  <img class="alta" src="../../../../Logos/Alta_Studio_logo_white.png">
  <div class="headline">
    ANTHROPIC CONSULTA A<br>
    <span class="coral">LÍDERES RELIGIOSOS</span> PARA<br>
    DEFINIR LA <span class="yellow">BRÚJULA ÉTICA</span><br>
    DE SU IA
  </div>
  <div class="bottom-row">
    <div class="tagline">EL AVANCE DE LA IA ABRE PREGUNTAS ÉTICAS INESPERADAS</div>
    <div class="swipe">DESLIZA →</div>
  </div>
</body></html>
```

### Cover rules

- **Photo** is a 4:5 full-bleed image filling the ENTIRE 1080×1350 canvas. A CSS gradient overlay darkens the bottom ~40% for text readability. **No solid black text zone** — the old "photo top + black bottom" split layout is deprecated
- **CSS gradient** `linear-gradient(to top, rgba(0,0,0,0.95) 0%, rgba(0,0,0,0.88) 8%, rgba(0,0,0,0.72) 22%, rgba(0,0,0,0.35) 42%, transparent 62%)` is applied via a separate `<div class="gradient">` overlay. PIL baked fade-to-black is NOT needed for full-bleed covers
- **Headline and bottom-row are SEPARATE absolute-positioned elements** — headline at `top:860px`, bottom-row at `top:1268px`. They must NOT be nested inside a shared parent container. Chrome headless clips child content that extends beyond its parent's rendered height, which causes the SWIPE pill to be invisible when nested
- **Headline** 6–10 words, all-caps, Inter 800 at **62–68px**. 2–3 keywords highlighted (mix of coral + yellow marker). Line-height 1.1
- **SWIPE pill** ("DESLIZA →") — solid white bg `#fff`, dark text `#0E0E0E`, bold, letter-spacing 0.18em, with soft drop-shadow. Must be unmistakably visible — not semi-transparent (18% white bg rendered as invisible in previous tests)
- **Alta Studio logo** top-left overlaid on the photo. **100px tall, uniform across ALL slides** (cover + body + closer). Drop-shadow filter for contrast
- **Never** use `backdrop-filter: blur` on any element (render.sh / headless Chrome strip it)
- **Never** use the old split layout (4:3 photo top + solid black text zone bottom) — creates a visible "marco negro" artifact
- **Never** nest the bottom-row inside the headline block — use independent absolute positioning

---

## 6. Template: Tweet slide

The tweet is the "source of truth" slide. It reproduces either (a) a real public announcement by the company/CEO, or (b) a plausible reaction tweet from an invented commentator handle. **See §11 for the ethics rules.**

### Layout

```
┌─────────────────────────────────────┐
│  [Alta Studio]                      │  ← top-left, small
│                                     │
│     ┌──────────────────────────┐    │
│     │  [avatar] Name ✓         │    │  ← white card
│     │          @handle         │    │    with Twitter UI
│     │                          │    │
│     │  Tweet body text goes    │    │
│     │  here, in two or three   │    │
│     │  short paragraphs.       │    │
│     │                          │    │
│     │  12:30 PM · Apr 15, 2026 │    │
│     └──────────────────────────┘    │
│                                     │
└─────────────────────────────────────┘
```

### HTML scaffold (key parts)

```html
<style>
  body{background:#000;color:#fff}
  .alta{position:absolute;top:40px;left:48px;height:44px;opacity:.95}
  .tweet-card{position:absolute;top:130px;left:60px;right:60px;background:#fff;border-radius:24px;padding:36px 40px;color:#0F1419}
  .tweet-header{display:flex;align-items:center;gap:14px;margin-bottom:22px}
  .avatar{width:56px;height:56px;border-radius:50%;background-size:cover;background-position:center}
  .name{font-size:24px;font-weight:700;display:flex;align-items:center;gap:6px}
  .verified{width:22px;height:22px;fill:#1D9BF0}
  .handle{font-size:20px;color:#536471;font-weight:400;margin-top:2px}
  .tweet-body{font-size:30px;line-height:1.42;font-weight:400}
  .tweet-body p{margin-bottom:18px}
  .tweet-time{font-size:18px;color:#536471;margin-top:26px}
</style>
<body>
  <img class="alta" src="../../../../Logos/Alta_Studio_logo.png">
  <div class="tweet-card">
    <div class="tweet-header">
      <div class="avatar" style="background-image:url('tweet_avatar.png')"></div>
      <div>
        <div class="name">Anthropic <svg class="verified" viewBox="0 0 24 24"><path d="M22.5 12.5c0-1.58-.875-2.95-2.148-3.6.154-.435.238-.905.238-1.4 0-2.21-1.71-4-3.818-4-.47 0-.92.084-1.336.25C14.818 2.415 13.51 1.5 12 1.5s-2.816.917-3.437 2.25c-.415-.165-.866-.25-1.336-.25-2.11 0-3.818 1.79-3.818 4 0 .494.083.964.237 1.4-1.272.65-2.147 2.018-2.147 3.6 0 1.495.782 2.798 1.942 3.486-.02.17-.032.34-.032.514 0 2.21 1.708 4 3.818 4 .47 0 .92-.086 1.335-.25.62 1.334 1.926 2.25 3.437 2.25 1.512 0 2.818-.916 3.437-2.25.415.163.865.248 1.336.248 2.11 0 3.818-1.79 3.818-4 0-.174-.012-.344-.033-.513 1.158-.687 1.943-1.99 1.943-3.484zm-6.616-3.334l-4.334 6.5c-.145.217-.382.354-.643.371h-.05c-.24 0-.47-.09-.644-.26l-2.5-2.5c-.33-.33-.33-.866 0-1.195.33-.33.866-.33 1.196 0l2.064 2.064 3.71-5.566c.245-.367.78-.26.986-.16.366.245.466.76.22 1.126z"/></svg></div>
        <div class="handle">@AnthropicAI</div>
      </div>
    </div>
    <div class="tweet-body">
      <p>Publicamos hoy un nuevo documento sobre cómo pensamos el alineamiento de Claude con valores humanos.</p>
      <p>Consultamos a líderes religiosos, filósofos y eticistas de diversas tradiciones.</p>
    </div>
    <div class="tweet-time">10:12 AM · Apr 15, 2026</div>
  </div>
</body>
```

### Avatar handling

- **Avatar image = gpt-image-1 generated.** For known brands, generate a logo-style avatar: *"Official [brand] logo avatar, circular format, solid background"*. Save to `Logos/` so it's reusable.
- **For invented commentator tweets**, generate a plausible portrait avatar: *"Professional headshot of a 30s Latin American AI researcher, neutral background, editorial photography"*. Do NOT save these to `Assets/Personas/` — they're post-specific.

### Tweet writing rules

- Length: 2–4 short lines
- Match the actual X/Twitter style (no emojis unless the real account uses them, casual but clean)
- Timestamps: use today's date or the actual announcement date if researched
- **Official tweets are the primary use** — reaction tweets only when the news benefits from commentary

---

## 7. Template A: Text + photo slide (default body slide)

This is the **workhorse** of the carousel. Used for slides 3 and often 4. Dark background, text in the top ~55%, gpt-image-1 photo (16:9 rectangle) in the bottom ~45%.

### Layout

```
┌─────────────────────────────────────┐
│  [Alta Studio]                      │  ← top-left, 46px
│                                     │
│   LABEL CORAL OPCIONAL              │  ← e.g. "LO QUE PASÓ"
│                                     │
│   Frase corta en blanco,            │  ← Inter 600, 38–42px
│   cada oración en línea propia.     │    2–4 líneas total
│   Tercera línea si hace falta.      │
│                                     │
│                                     │  ← editorial whitespace
│                                     │
├─────────────────────────────────────┤  ← hard edge at y=742
│                                     │
│   GPT-IMAGE-1 PHOTO (16:9)          │  ← 1080 × 608 px
│   concept-reinforcing,              │    natively horizontal, fully visible
│   editorial photography             │    NOT cropped
│                                     │
└─────────────────────────────────────┘
```

### gpt-image-1 prompt structure (body slide photo)

```
Editorial cinematic photograph, horizontal widescreen composition.
[SCENE description — concept-reinforcing, NOT person-centric].
[lighting / mood / color grading keywords].
16:9 widescreen format, wide horizontal framing.
No text, no logos, no words, no watermarks anywhere in the image.
```

**Use `--aspect-ratio 16:9`** → outputs 1080×608 after internal crop+resize. This matches the photo region in the HTML exactly, so the full composition is visible with NO cropping.

### HTML scaffold

```html
<style>
  body{background:#000;color:#fff;font-family:'Inter',sans-serif}
  .alta{position:absolute;top:42px;left:48px;height:46px;opacity:.95}
  .label{position:absolute;top:148px;left:60px;font-size:15px;font-weight:700;color:#E85D3C;text-transform:uppercase;letter-spacing:.14em;z-index:10}
  .text-block{position:absolute;top:210px;left:60px;right:60px;font-size:40px;font-weight:600;line-height:1.28;color:#fff;letter-spacing:-.008em;z-index:10}
  .text-block p{margin-bottom:22px}
  .text-block p:last-child{margin-bottom:0}
  .text-block .accent{color:#FFE45C}
  .text-block strong{font-weight:700}
  .photo{position:absolute;bottom:0;left:0;right:0;height:608px;background-image:url('slide3_photo.png');background-size:cover;background-position:center center}
  .photo-fade-top{position:absolute;bottom:608px;left:0;right:0;height:30px;background:linear-gradient(to top,rgba(0,0,0,.5) 0%,transparent 100%);pointer-events:none;z-index:4}
</style>
<body>
  <img class="alta" src="../../../../Logos/Alta_Studio_logo_white.png">
  <div class="label">LO QUE PASÓ</div>
  <div class="text-block">
    <p>Anthropic consultó a <strong>rabinos, imames, pastores y teólogos</strong>.</p>
    <p>Buscan respuestas a preguntas éticas que no vienen en manuales técnicos.</p>
    <p>El objetivo: guiar cómo Claude razona sobre <span class="accent">dilemas morales</span>.</p>
  </div>
  <div class="photo"></div>
</body>
```

### Photo prompt for body slides (different from cover)

Body slide photos are **concept-reinforcing**, not person-centric. They evoke the idea, not dramatize a face.

Good prompts (all at `--aspect-ratio 16:9`):
- *"University campus with medieval architecture in autumn light, editorial photography, cinematic, 16:9 widescreen"* (for a research paper slide)
- *"Factory floor with robotic arms assembling electronics, blue industrial lighting, realistic, 16:9 widescreen"* (for an automation slide)
- *"Aerial night view of a dense city with glowing streets, film grain, editorial, 16:9 widescreen"* (for an economy slide)
- *"Interfaith gathering — diverse religious leaders in a conference room, soft natural light, 16:9 widescreen"* (for the Anthropic/religion example)

**Rules:**
- No text, no logos in the image
- Always `--aspect-ratio 16:9` (never 4:5 — that would crop)
- Match the emotional temperature of the text (warm for human stories, cold/industrial for tech)
- Same film grain / editorial treatment as cover for visual consistency

### Variant: swap which half is which

Sometimes the photo works better on top and text on bottom (e.g., when the photo is a horizon/landscape). That's fine — flip the `bottom:0` on the photo to `top:0` and adjust text/label positions. Photo aspect ratio stays 16:9.

---

## 8. Template B: White-card slide (punchline / stat / quote)

Used when a slide needs to **slam a single fact** without dilution. No photo. Big number or short quote on a white card over black.

### Layout

```
┌─────────────────────────────────────┐
│  [Alta Studio]                      │
│                                     │
│     ┌──────────────────────────┐    │
│     │                          │    │
│     │  EL DATO                 │    │  ← coral label top
│     │                          │    │
│     │                          │    │
│     │      40%                 │    │  ← huge stat (180px+)
│     │                          │    │
│     │                          │    │
│     │  de las consultas ya     │    │  ← explanation
│     │  las resuelve IA.        │    │
│     │                          │    │
│     │  Fuente: Scotiabank      │    │  ← small source line
│     │                          │    │
│     └──────────────────────────┘    │
│                                     │
└─────────────────────────────────────┘
```

### HTML scaffold

```html
<style>
  body{background:#000;font-family:'Inter',sans-serif}
  .alta{position:absolute;top:40px;left:48px;height:44px;opacity:.95}
  .card{position:absolute;top:130px;left:60px;right:60px;bottom:100px;background:#fff;border-radius:28px;padding:60px 56px;color:#0E0E0E;display:flex;flex-direction:column;justify-content:space-between}
  .card-label{font-size:16px;font-weight:700;color:#E85D3C;text-transform:uppercase;letter-spacing:.14em}
  .stat{font-size:220px;font-weight:900;line-height:.95;letter-spacing:-.04em;margin-top:auto;margin-bottom:20px}
  .stat-body{font-size:36px;font-weight:600;line-height:1.25;letter-spacing:-.01em}
  .source{font-size:18px;font-weight:500;color:#6B6B6B;margin-top:34px}
</style>
<body>
  <img class="alta" src="../../../../Logos/Alta_Studio_logo.png">
  <div class="card">
    <div class="card-label">EL DATO</div>
    <div>
      <div class="stat">40%</div>
      <div class="stat-body">de las consultas de clientes de Scotiabank ya las resuelve su IA interna.</div>
      <div class="source">Fuente: Artificial Intelligence News</div>
    </div>
  </div>
</body>
```

### When to use Template B

- Slide carries a **single killer stat** (percentage, dollar figure, multiplier)
- Slide is a **short pull quote** from the source
- Slide is the **closer** and needs max impact
- **Never** use Template B back-to-back — needs a text+photo or tweet slide adjacent for rhythm

---

## 9. Closer slide (slide 5)

Three valid closer formats (pick based on the news):

1. **Reaction tweet** — invented commentator handle reacts to the news. Uses Template from §6 with an invented `@handle`.
2. **Stat card** — Template B with the most impactful number of the story.
3. **Key takeaway** — Template A with a one-line insight + photo (e.g., foto conceptual de "el futuro de la IA").

### When to use which

- **Reaction tweet:** news that benefits from a "outside voice" (policy news, controversy, launch receptions)
- **Stat card:** news with one killer number
- **Key takeaway:** news where the synthesis/meaning is the hook

---

## 10. gpt-image-1 — photo generation

### Aspect ratios by slide type (non-negotiable)

News photos use **rectangular aspect ratios** that match their designated region on the slide — **NOT** the full 4:5 Instagram canvas. Generating at 4:5 results in the subject being cropped or covered by text.

| Slide type | `--aspect-ratio` | Output | Purpose |
|---|---|---|---|
| **Cover (slide 1)** | `4:5` | 1080 × 1350 | Full-bleed photo fills entire canvas; CSS gradient overlay darkens bottom for text |
| **Body text+photo (Template A)** | `16:9` | 1080 × 608 | Photo occupies bottom ~45% of canvas; text + label occupy top ~55% |
| **Tweet avatar** | `1:1` | 1080 × 1080 | Square for circular crop in tweet UI |
| **Closer photo (slide 5 Template A variant)** | `16:9` | 1080 × 608 | Same as body photos |

> The script crops + resizes internally to these exact dimensions. No post-script PIL resize is needed — that step is baked in.

### Default command

```bash
python generate-image.py \
  --prompt "[detailed prompt]" \
  --output PostTypes/news/Outputs/{topic-slug}/{filename}.png \
  --aspect-ratio {4:5 | 16:9 | 1:1 — per table above}
```

The default `--quality high` and `--crop top` are correct for news photos (editorial quality, preserves faces in portraits).

### Naming convention for photo files

```
PostTypes/news/Outputs/{topic-slug}/
├── composition.png       ← cover photo
├── slide3_photo.png      ← text+photo slide 3
├── slide4_photo.png      ← (if slide 4 is Template A)
├── slide5_photo.png      ← (if closer is Template A)
└── tweet_avatar.png      ← tweet slide avatar (if invented commentator)
```

### Rules

- **Generate ONE photo per slide.** Do not generate variants. The prompt is the craft — if the output is wrong, iterate on the prompt, not on the count.
- **Never use `--reference`** — per user preference, all news photos are 100% generative. Do not composite real person photos.
- **Never embed text** in prompts. Text = HTML overlay, always.
- **Content policy:** OpenAI rejects named real public figures. If the script fails with `content_policy_violation`, rephrase with role/features instead of the name, or use a reference photo from `Assets/Personas/` (last resort — violates the no-reference rule above, so only if the user explicitly OKs it).

### Prompt checklist (before submitting to API)

- [ ] Describes the scene, not the frame
- [ ] Includes "editorial photography" or "film grain" or "cinematic"
- [ ] For covers: positions subject in upper portion, leaves lower area for gradient overlay
- [ ] Ends with "No text, no typography, no logos, no words anywhere in the image"
- [ ] Correct aspect ratio flag set (4:5 for covers, 16:9 for body slides)
- [ ] Real public figures described by role/features, not by name (OpenAI content policy)

---

## 11. Tweet ethics — MANDATORY rules

News posts include tweets. **Approved rules (user-locked):**

| Case | What I do |
|---|---|
| **Official company announcement** (ej: "Perplexity anunció X") | Research the actual tweet via WebSearch. Reproduce the real tweet faithfully — author, handle, text. **Cite, never invent.** |
| **Public CEO statement** (ej: Altman in Senate hearing, Amodei in a conference) | Paraphrase from documented public record only. Attribute to real handle. **If the quote can't be verified, do NOT attribute to a real person.** |
| **Reaction / analysis tweet** (journalist, researcher commentary) | Use **invented plausible handle** (e.g., `@sofia_reyes_ai`) with gpt-image-1 avatar. Clearly fictional persona. **Never attribute an invented quote to a real person.** |
| **Editorial quote card** (fallback) | If no real source and no need for commentary, use a quote card styled differently from a tweet — no Twitter UI, just typographic quote + source citation. |

### Why this matters

Fabricated quotes attributed to real people are **misinformation** — screenshots get shared, the user takes the reputational hit when it's debunked. These rules keep the pipeline automatic while protecting the brand.

### When researching real tweets

- Use WebSearch with queries like `"[company name] twitter announcement [topic] [year]"`
- Verify the tweet exists on a reputable source before reproducing
- If the original tweet isn't findable, shift to the editorial quote card option

---

## 12. Headline writing rules

### Language

- **Colombian Spanish, `tú` form.** Never voseo ("creá", "usá"). Use "crea", "usa", "mira", "descubre".
- Brand names stay in English: "Anthropic", "Perplexity", "Claude", "OpenAI"
- Numbers: prefer digits over words ("40%", "US$2.000 millones", "5 años")
- Currency: adapt to LATAM reading ("$2B" → "US$2.000 millones")

### Cover headline style

| Rule | Detail |
|---|---|
| Word count | **6–10 words** (tight, punchy, one breath) |
| Case | **ALL CAPS** |
| Font weight | 800 |
| Line count | 2–3 lines |
| Keyword highlight | **2–3 keywords** in coral and/or yellow marker |
| Tone | Factual, newsworthy — **not clickbait**. No exclamation marks, no "¡INCREÍBLE!", no "NO VAS A CREER" |

### Highlight pattern — which keyword gets which color

| Color | What it marks |
|---|---|
| **Coral text** `#E85D3C` | Brand name (Anthropic, OpenAI), strong noun (CHIPS, AGENTES), verb (ATACARON, FILTRAN) |
| **Yellow marker** `#FFE45C` (dark text inside) | Number/stat (40%, US$2.000M), short impactful noun (GRATIS, AHORA, HOY) |

### Good headlines

- *"ANTHROPIC CONSULTA A **LÍDERES RELIGIOSOS** PARA DEFINIR LA **BRÚJULA ÉTICA** DE SU IA"*
- *"LA **CASA DE SAM ALTMAN** FUE ATACADA **DOS VECES** EN POCOS DÍAS"*
- *"INVESTIGADORES DEMOSTRARON QUE LOS **DESPIDOS POR IA** PUEDEN **ROMPER LA ECONOMÍA**"*

### Bad headlines

- *"¡INCREÍBLE lo que hizo Anthropic!"* — clickbait
- *"Anthropic"* — vacío
- *"Anthropic reportedly consults religious leaders..."* — está en inglés
- *"Crea tu propia IA ética"* — es un titular de tutorial, no de news

### Tagline (below headline)

- 1 line, all caps, Inter 600, 75% opacity
- Expands the "why this matters" in plain language
- Examples: *"EL AVANCE DE LA IA ABRE PREGUNTAS ÉTICAS INESPERADAS"*, *"LO QUE VIENE ESTA SEMANA"*, *"CUANDO LA SEGURIDAD Y LA VISIBILIDAD TIENEN UN COSTO PERSONAL"*

---

## 13. Caption — ahora es corto

Porque el contenido vive en los slides, el caption pasa a ser **breve y utilitario** (no informativo largo).

### Formato del caption

- **1–3 líneas** máximo
- **Objetivo:** dar contexto mínimo para el feed + facilitar búsqueda
- **Sin hashtags** (el user los agrega si quiere)
- **Sin emojis**
- **Sin CTA** ("sígueme", "guarda")

### Ejemplos

```
Anthropic está consultando a líderes religiosos y filósofos para definir los valores con los que entrena a Claude.
```

```
La casa de Sam Altman ha sido atacada dos veces en menos de una semana.
Seguridad personal y figura pública, el costo del liderazgo en IA.
```

### Workflow del caption

- Generar en el paso final del workflow, después de aprobar todos los slides
- Guardar en `caption.txt` en la carpeta del post
- Presentar junto con los slides al cierre

---

## 14. Workflow when the user asks for a news post

1. **Read this skill** + base rules from [`CLAUDE.md`](../../../CLAUDE.md) + [`news/README.md`](../README.md).
2. **Mandatory visual re-anchoring:** review [`Inspiracion/`](../Inspiracion/) AND [`Favoritos_Claude_Generated/`](../Favoritos_Claude_Generated/) (CLAUDE.md §1.5). **Look at the carousel patterns, not just covers.**
3. **Understand the news:** what happened, who's involved, what's the data. If the user gave only a title, WebSearch for the full story.
4. **Draft the slide outline** — propose the 5-slide breakdown (headline, tweet angle, body slide 1, body slide 2, closer). Wait for approval.
5. **Propose 2–3 cover headline variations** (Colombian Spanish, with keyword highlights marked). Wait for approval.
6. **Research real tweets** if slide 2 is an official announcement (see §11). If the source announcement exists, capture the exact tweet text.
7. **Generate photos with gpt-image-1** — ONE per slide that needs one (cover + 1–2 body slides). Cover at `--aspect-ratio 4:5` (full-bleed), body slides at `--aspect-ratio 16:9`. The script handles crop + resize internally.
8. **Present photos to user for review.** Only regenerate if rejected.
9. **Build the HTML for all slides** — cover, tweet, text+photo, (optional) white card, closer. Save each as `slide{N}_{descriptor}.html` in the output folder.
10. **Render via `./render.sh PostTypes/news/Outputs/{topic-slug}`** — renders all slides at once.
11. **MANDATORY Visual QA** (see [`Skills/visual-qa.md`](../../../Skills/visual-qa.md)) — open every PNG, verify no artifacts, text readable, photos correctly positioned, no page dots on any slide, Alta Studio logo visible, SWIPE pill only on cover.
12. **Draft the short caption** (1–3 lines), save as `caption.txt`.
13. **Present the complete carousel** — all 5 PNGs in order + caption, ready to upload to Instagram.
14. **Ask which slides are favorites** → copy selected PNGs to `Favoritos_Claude_Generated/` (CLAUDE.md §1.6).

### Naming convention for news carousel outputs

```
PostTypes/news/Outputs/{topic-slug}/
├── composition.png              ← cover photo (gpt-image-1)
├── slide3_photo.png             ← text+photo slide 3 photo
├── slide4_photo.png             ← (optional) text+photo slide 4 photo
├── slide5_photo.png             ← (optional) closer photo
├── tweet_avatar.png             ← (optional) invented commentator avatar
├── slide1_cover.html            ← cover HTML
├── slide1_cover.png             ← rendered cover
├── slide2_tweet.html
├── slide2_tweet.png
├── slide3_text.html
├── slide3_text.png
├── slide4_{text|card}.html
├── slide4_{text|card}.png
├── slide5_closer.html
├── slide5_closer.png
└── caption.txt
```

- `{topic-slug}`: kebab-case, descriptive. E.g. `anthropic-lideres-religiosos`, `altman-ataques-casa`, `perplexity-billion-build`.

---

## 15. Anti-patterns (news-specific)

- ❌ Single-image news posts (the old format — now deprecated)
- ❌ Long captions with 6–10 paragraphs of info (content now lives in slides)
- ❌ PIL for text overlay (deprecated — all text is HTML + render.sh)
- ❌ Cream background or grid pattern (that's step-by-step identity)
- ❌ `@lucianomusellaa` handle on news slides (news uses Alta Studio logo only)
- ❌ Alta Studio in BOTH corners (only one corner per slide)
- ❌ SWIPE pill on body slides (only on cover)
- ❌ Page dots on any slide (Instagram adds carousel dots natively)
- ❌ gpt-image-1 generating text, logos, or watermarks (always strip with "No text, no logos, no words")
- ❌ Using `--reference` with real person photos (100% generative per user preference)
- ❌ Generating cover photos at `--aspect-ratio 4:3` (the old split layout) — use `4:5` for full-bleed covers with CSS gradient overlay
- ❌ Using the old "photo top 810px + solid black text zone bottom" cover layout — creates a visible "marco negro". Use full-bleed photo + CSS gradient instead
- ❌ Generating body slide photos at `--aspect-ratio 4:5` — they get cropped to the 608px photo region. Use `16:9` so the full composition is visible
- ❌ Using `backdrop-filter: blur` anywhere — headless Chrome strips it, elements render invisible
- ❌ PIL baked fade-to-black on cover photos — this was for the old split layout. Full-bleed covers use CSS gradient overlay instead
- ❌ Nesting the bottom-row (tagline + SWIPE pill) inside the headline block — Chrome headless clips child content that extends beyond parent's rendered height. Use SEPARATE absolute-positioned elements
- ❌ Alta Studio logo smaller than ~80px on covers — it disappears visually. 100px is the target (uniform across all slides)
- ❌ Fabricating quotes attributed to real people (see §11 ethics)
- ❌ More than one Template B (white card) in a row — needs visual rhythm
- ❌ Headlines in English (always Colombian Spanish)
- ❌ Clickbait ("¡INCREÍBLE!", "¡NO VAS A CREER!")
- ❌ Generating multiple photo variants per slide (prompt well, generate once, iterate on prompt if needed)
- ❌ Hashtags or emojis in the caption

---

## 16. Quick-reference checklist (run before presenting the carousel)

### Content
- [ ] 4–7 slides total (5 is default)
- [ ] Cover has killer headline with 2–3 keyword highlights (coral + yellow)
- [ ] Slide 2 is a real official tweet or a quote card (never a fabricated tweet from a real person)
- [ ] Body slides (3, 4) use Template A (text+photo) mostly, B (white card) for punchlines
- [ ] Closer is reaction tweet, stat card, or takeaway — chosen for impact
- [ ] Caption is 1–3 lines, no hashtags, no emojis

### Visual
- [ ] Every slide is 1080×1350
- [ ] Alta Studio logo in one top corner on every slide (not both, not missing)
- [ ] SWIPE pill only on cover
- [ ] No page dots on any slide (Instagram adds them natively)
- [ ] No `@lucianomusellaa` anywhere
- [ ] Cover photo is gpt-image-1 at 4:5 (full-bleed), body photos at 16:9, all text/logo-free
- [ ] No black border artifacts (render.sh handles this — verify with QA)

### Language
- [ ] Colombian Spanish, `tú` form throughout
- [ ] Brand names kept in English
- [ ] Numbers as digits
- [ ] No voseo, no "¡!", no clickbait tone

### Pipeline
- [ ] All slides rendered via `./render.sh`
- [ ] Visual QA run on every PNG
- [ ] Output folder follows naming convention
- [ ] Caption saved as `caption.txt`
- [ ] User asked which slides are favorites
