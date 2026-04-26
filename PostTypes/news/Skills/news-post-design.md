---
name: news-post-design
description: Visual system for AI news Instagram posts â€” 5-slide carousel with Codex image tool photo compositions, HTML text overlays, and tweet slides. Covers, text+photo slides, and white-card slides on black editorial background.
type: skill
---

# News Post Design Skill

> **Project root:** `c:/Trabajo_AI/Visual_posts/`. The autoloaded **[`CLAUDE.md`](../../../CLAUDE.md)** at the project root contains the trigger phrases and routes to per-type workflows. The news workflow lives in [`../README.md`](../README.md). Read those for the *process*; read this skill for the *visual system*.

This skill defines the visual language for **AI news posts** â€” 5-slide Instagram carousels with a dark editorial feel, inspired by the references in [`../Inspiracion/`](../Inspiracion/) (Bridgemind-style accounts). The previous single-image + long-caption system is **deprecated** â€” news posts are now carousels.

---

## 0. What changed (and why)

| | Old system (deprecated) | New system |
|---|---|---|
| Format | Single image + long caption (6â€“10 paragraphs) | **5-slide carousel** (scalable to 7) + short caption (1â€“3 lines) |
| Cover render | Generated photo + PIL text overlay | Codex image tool photo + **HTML overlay via render.sh** |
| Body content | All in the caption | **Distributed across slides** (tweet + text + photo) |
| Alta Studio logo | Top-right (fixed position) | **One corner only** (top-left or top-right, composition-dependent) |
| Pipeline | PIL for text, render.sh for HTML | **Unified: render.sh for all slides, Codex image tool for all photos** |

**Why:** the carousel format is what AI news creators actually use on Instagram (see inspo). It's more visually engaging, each slide "earns its swipe", and people actually read digestible chunks instead of skipping long captions.

> **Viewport bug fix (2026-04-16):** Chrome headless on Windows subtracts ~96px from the `--window-size` height for window chrome decorations. The old `--window-size=1098,1368` caused content below yâ‰ˆ1272 to not render (pills, taglines were invisible). `render.sh` now uses `--window-size=1098,1550` and crops to 1080Ã—1350 via PIL. If elements near the bottom of a slide appear missing in renders, this is the first thing to check.

---

## 1. Canvas & format

| Property | Value |
|---|---|
| Aspect ratio | **4:5 portrait** (Instagram feed optimal) |
| Resolution | **1080 Ã— 1350 px** per slide |
| Format | **Carousel** â€” 5 slides default, 4â€“7 allowed |
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
| Gradient overlay (cover) | `linear-gradient(to top, rgba(0,0,0,0.95) 0%, rgba(0,0,0,0.88) 8%, rgba(0,0,0,0.72) 22%, rgba(0,0,0,0.35) 42%, transparent 62%)` | Bottom of cover â€” full-bleed photo with gradient for headline readability |

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
| **Cover headline** | Inter | 58â€“70 px | 800 | White + coral + yellow-marker spans |
| **Cover tagline** | Inter | 17â€“19 px | 600 | `rgba(255,255,255,0.75)`, ALL CAPS, letter-spacing 0.08em |
| **Body slide label** | Inter | 15 px | 700 | Coral `#E85D3C`, ALL CAPS, letter-spacing 0.14em |
| **Body slide text** | Inter | 34â€“42 px | 600 | White on dark, dark `#0E0E0E` on white card |
| **Tweet name** | Inter | 24 px | 700 | `#0F1419` |
| **Tweet handle** | Inter | 20 px | 400 | `#536471` |
| **Tweet body** | Inter | 30 px | 400 | `#0F1419`, line-height 1.4 |
| **Stat card number** | Inter | 180â€“240 px | 900 | Dark |
| **SWIPE pill** | Inter | 13 px | 700 | White on `rgba(255,255,255,0.12)`, letter-spacing 0.12em |

---

## 4. Slide taxonomy â€” the 5-slide default

Every news post follows this skeleton (deviations require user approval):

| # | Slide type | Purpose | Template |
|---|---|---|---|
| **1** | **Cover** | Hook: photo + killer headline | Â§5 |
| **2** | **Tweet / oficial** | Source of truth: reproduces the company or CEO's public announcement | Â§6 |
| **3** | **Text + photo** (Template A) | What happened â€” context in 2â€“3 short lines + supporting Codex image tool photo | Â§7 |
| **4** | **Text + photo** or **White card** | Why it matters â€” explanation with photo, OR punchline stat with white card | Â§7 or Â§8 |
| **5** | **Closer** | Reaction tweet (invented handle) OR stat card OR CTA | Â§6 or Â§8 |

### When to deviate

- **4 slides** â€” simple news (one fact, one consequence). Skip slide 4.
- **6 slides** â€” news with 2 distinct consequences. Add a second text+photo between 3 and 4.
- **7 slides** â€” complex news (announcement + reactions + data). Rare.
- **Never less than 4** â€” a 3-slide news post feels thin.

### Global elements across all body slides (not cover)

- **Alta Studio logo** top-left corner, **100px tall** (uniform across all 5 slides â€” cover, body, closer), opacity 0.98, with drop-shadow filter `drop-shadow(0 2px 14px rgba(0,0,0,.55))`. Position: `top:44px; left:50px`
- **No `@lucianomusellaa` handle** on news posts (editorial feel â€” replaced by Alta Studio logo)
- **Content positioning** â€” labels/cards/text blocks must start at `top: â‰¥170px` to clear the 100px-tall logo (which extends to yâ‰ˆ144 plus margin)

### What the cover does NOT have

- No Alta Studio in both corners â€” **only one**
- Instead: **SWIPE pill** bottom-right to signal carousel

---

## 5. Template: Cover slide

### Layout (full-bleed photo + CSS gradient overlay)

```
â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
â”‚ [Alta]                              â”‚  â† top-left, overlaps photo
â”‚                                     â”‚
â”‚                                     â”‚
â”‚    Codex image tool PHOTO (4:5)          â”‚  â† 1080 Ã— 1350 px FULL BLEED
â”‚    (shoe, scene, person, etc.)      â”‚    fills entire canvas
â”‚    editorial, cinematic,            â”‚    subject in upper 60%
â”‚    background-size: cover           â”‚
â”‚                                     â”‚
â”‚ â”„â”„â”„â”„â”„â”„â”„â”„â”„â”„â”„â”„â”„â”„â”„â”„â”„â”„â”„â”„â”„â”„â”„â”„â”„â”„â”„â”„â”„â”„â”„â”„ â”‚  â† CSS gradient starts fading ~62%
â”‚                                     â”‚
â”‚  TITULAR EN BOLD                    â”‚  â† headline at top:860px (absolute)
â”‚  CON PALABRAS RESALTADAS            â”‚    over gradient-darkened zone
â”‚  EN CORAL Y AMARILLO                â”‚
â”‚                                     â”‚
â”‚  TAGLINE          [SWIPE â†’]         â”‚  â† bottom-row at top:1268px (absolute)
â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
```

> **NOTE:** Headline and bottom-row are SEPARATE `position:absolute` elements on `<body>`, NOT nested inside each other. Chrome headless clips child content that extends beyond its parent's rendered height â€” nesting the bottom-row inside the headline block caused the SWIPE pill to be invisible. Independent positioning avoids this.

### Codex image tool prompt structure (cover photo)

```
Editorial cinematic photograph, vertical portrait composition, 4:5 aspect ratio.
[SCENE/PERSON description â€” position subject in the UPPER portion of the frame, leave lower 40% as open/dark space for text overlay].
Dramatic lighting, subtle film grain, slightly desaturated editorial tones.
Portrait format, magazine cover quality, vertical framing.
No text, no typography, no logos, no words, no watermarks anywhere in the image.
```

**Prompt rules:**
- **Always end with** "No text, no typography, no logos, no words anywhere" â€” image models love to add text
- Use a 4:5 target image (1080x1350 when saved into the project). Cover photos are **full-bleed** â€” they fill the entire canvas edge to edge. A CSS gradient overlay darkens the bottom for text readability
- **Position the subject in the upper portion** of the frame â€” the bottom 40% will be darkened by the gradient, so important details should sit above ~y=540. Keep the subject in the upper portion if any crop/resize is needed
- Describe the scene, not the frame: avoid "cover photo", "Instagram post", etc.
- Include **"film grain"** or "editorial photography" â€” avoids the plastic AI look
- **For real public figures** (Altman, Amodei, Pichai, Zuck) â€” OpenAI's content policy is stricter than Gemini's and will likely reject named real people. Describe by features, role, and setting instead: "a bearded tech CEO in a grey t-shirt at a Senate hearing" rather than "Sam Altman". If a prompt fails with `content_policy_violation`, rephrase as "a person who looks like X" or check `Assets/Personas/` for an existing reference photo
- For invented roles (researchers, analysts, workers) â€” describe demographics + context naturally

**Generate ONE cover photo.** Present to user. Only regenerate if rejected.

### Cover HTML scaffold

Save as `slide1_cover.html` in the post's output folder. The `composition.png` (Codex image tool 4:5 output) must be in the same folder.

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
    <span class="coral">LÃDERES RELIGIOSOS</span> PARA<br>
    DEFINIR LA <span class="yellow">BRÃšJULA Ã‰TICA</span><br>
    DE SU IA
  </div>
  <div class="bottom-row">
    <div class="tagline">EL AVANCE DE LA IA ABRE PREGUNTAS Ã‰TICAS INESPERADAS</div>
    <div class="swipe">DESLIZA â†’</div>
  </div>
</body></html>
```

### Cover rules

- **Photo** is a 4:5 full-bleed image filling the ENTIRE 1080Ã—1350 canvas. A CSS gradient overlay darkens the bottom ~40% for text readability. **No solid black text zone** â€” the old "photo top + black bottom" split layout is deprecated
- **CSS gradient** `linear-gradient(to top, rgba(0,0,0,0.95) 0%, rgba(0,0,0,0.88) 8%, rgba(0,0,0,0.72) 22%, rgba(0,0,0,0.35) 42%, transparent 62%)` is applied via a separate `<div class="gradient">` overlay. PIL baked fade-to-black is NOT needed for full-bleed covers
- **Headline and bottom-row are SEPARATE absolute-positioned elements** â€” headline at `top:860px`, bottom-row at `top:1268px`. They must NOT be nested inside a shared parent container. Chrome headless clips child content that extends beyond its parent's rendered height, which causes the SWIPE pill to be invisible when nested
- **Headline** 6â€“10 words, all-caps, Inter 800 at **62â€“68px**. 2â€“3 keywords highlighted (mix of coral + yellow marker). Line-height 1.1
- **SWIPE pill** ("DESLIZA â†’") â€” solid white bg `#fff`, dark text `#0E0E0E`, bold, letter-spacing 0.18em, with soft drop-shadow. Must be unmistakably visible â€” not semi-transparent (18% white bg rendered as invisible in previous tests)
- **Alta Studio logo** top-left overlaid on the photo. **100px tall, uniform across ALL slides** (cover + body + closer). Drop-shadow filter for contrast
- **Never** use `backdrop-filter: blur` on any element (render.sh / headless Chrome strip it)
- **Never** use the old split layout (4:3 photo top + solid black text zone bottom) â€” creates a visible "marco negro" artifact
- **Never** nest the bottom-row inside the headline block â€” use independent absolute positioning

---

## 6. Template: Tweet slide

The tweet is the "source of truth" slide. It reproduces either (a) a real public announcement by the company/CEO, or (b) a plausible reaction tweet from an invented commentator handle. **See Â§11 for the ethics rules.**

### Layout

```
â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
â”‚  [Alta Studio]                      â”‚  â† top-left, small
â”‚                                     â”‚
â”‚     â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”    â”‚
â”‚     â”‚  [avatar] Name âœ“         â”‚    â”‚  â† white card
â”‚     â”‚          @handle         â”‚    â”‚    with Twitter UI
â”‚     â”‚                          â”‚    â”‚
â”‚     â”‚  Tweet body text goes    â”‚    â”‚
â”‚     â”‚  here, in two or three   â”‚    â”‚
â”‚     â”‚  short paragraphs.       â”‚    â”‚
â”‚     â”‚                          â”‚    â”‚
â”‚     â”‚  12:30 PM Â· Apr 15, 2026 â”‚    â”‚
â”‚     â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜    â”‚
â”‚                                     â”‚
â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
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
      <p>Publicamos hoy un nuevo documento sobre cÃ³mo pensamos el alineamiento de Claude con valores humanos.</p>
      <p>Consultamos a lÃ­deres religiosos, filÃ³sofos y eticistas de diversas tradiciones.</p>
    </div>
    <div class="tweet-time">10:12 AM Â· Apr 15, 2026</div>
  </div>
</body>
```

### Avatar handling

- **Avatar image = Codex image tool generated.** For known brands, generate a logo-style avatar: *"Official [brand] logo avatar, circular format, solid background"*. Save to `Logos/` so it's reusable.
- **For invented commentator tweets**, generate a plausible portrait avatar: *"Professional headshot of a 30s Latin American AI researcher, neutral background, editorial photography"*. Do NOT save these to `Assets/Personas/` â€” they're post-specific.

### Tweet writing rules

- Length: 2â€“4 short lines
- Match the actual X/Twitter style (no emojis unless the real account uses them, casual but clean)
- Timestamps: use today's date or the actual announcement date if researched
- **Official tweets are the primary use** â€” reaction tweets only when the news benefits from commentary

---

## 7. Template A: Text + photo slide (default body slide)

This is the **workhorse** of the carousel. Used for slides 3 and often 4. Dark background, text in the top ~55%, Codex image tool photo (16:9 rectangle) in the bottom ~45%.

### Layout

```
â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
â”‚  [Alta Studio]                      â”‚  â† top-left, 46px
â”‚                                     â”‚
â”‚   LABEL CORAL OPCIONAL              â”‚  â† e.g. "LO QUE PASÃ“"
â”‚                                     â”‚
â”‚   Frase corta en blanco,            â”‚  â† Inter 600, 38â€“42px
â”‚   cada oraciÃ³n en lÃ­nea propia.     â”‚    2â€“4 lÃ­neas total
â”‚   Tercera lÃ­nea si hace falta.      â”‚
â”‚                                     â”‚
â”‚                                     â”‚  â† editorial whitespace
â”‚                                     â”‚
â”œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¤  â† hard edge at y=742
â”‚                                     â”‚
â”‚   Codex image tool PHOTO (16:9)          â”‚  â† 1080 Ã— 608 px
â”‚   concept-reinforcing,              â”‚    natively horizontal, fully visible
â”‚   editorial photography             â”‚    NOT cropped
â”‚                                     â”‚
â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
```

### Codex image tool prompt structure (body slide photo)

```
Editorial cinematic photograph, horizontal widescreen composition.
[SCENE description â€” concept-reinforcing, NOT person-centric].
[lighting / mood / color grading keywords].
16:9 widescreen format, wide horizontal framing.
No text, no logos, no words, no watermarks anywhere in the image.
```

**Use `--aspect-ratio 16:9`** â†’ outputs 1080Ã—608 after internal crop+resize. This matches the photo region in the HTML exactly, so the full composition is visible with NO cropping.

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
  <div class="label">LO QUE PASÃ“</div>
  <div class="text-block">
    <p>Anthropic consultÃ³ a <strong>rabinos, imames, pastores y teÃ³logos</strong>.</p>
    <p>Buscan respuestas a preguntas Ã©ticas que no vienen en manuales tÃ©cnicos.</p>
    <p>El objetivo: guiar cÃ³mo Claude razona sobre <span class="accent">dilemas morales</span>.</p>
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
- *"Interfaith gathering â€” diverse religious leaders in a conference room, soft natural light, 16:9 widescreen"* (for the Anthropic/religion example)

**Rules:**
- No text, no logos in the image
- Always `--aspect-ratio 16:9` (never 4:5 â€” that would crop)
- Match the emotional temperature of the text (warm for human stories, cold/industrial for tech)
- Same film grain / editorial treatment as cover for visual consistency

### Variant: swap which half is which

Sometimes the photo works better on top and text on bottom (e.g., when the photo is a horizon/landscape). That's fine â€” flip the `bottom:0` on the photo to `top:0` and adjust text/label positions. Photo aspect ratio stays 16:9.

---

## 8. Template B: White-card slide (punchline / stat / quote)

Used when a slide needs to **slam a single fact** without dilution. No photo. Big number or short quote on a white card over black.

### Layout

```
â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
â”‚  [Alta Studio]                      â”‚
â”‚                                     â”‚
â”‚     â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”    â”‚
â”‚     â”‚                          â”‚    â”‚
â”‚     â”‚  EL DATO                 â”‚    â”‚  â† coral label top
â”‚     â”‚                          â”‚    â”‚
â”‚     â”‚                          â”‚    â”‚
â”‚     â”‚      40%                 â”‚    â”‚  â† huge stat (180px+)
â”‚     â”‚                          â”‚    â”‚
â”‚     â”‚                          â”‚    â”‚
â”‚     â”‚  de las consultas ya     â”‚    â”‚  â† explanation
â”‚     â”‚  las resuelve IA.        â”‚    â”‚
â”‚     â”‚                          â”‚    â”‚
â”‚     â”‚  Fuente: Scotiabank      â”‚    â”‚  â† small source line
â”‚     â”‚                          â”‚    â”‚
â”‚     â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜    â”‚
â”‚                                     â”‚
â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
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
- **Never** use Template B back-to-back â€” needs a text+photo or tweet slide adjacent for rhythm

---

## 9. Closer slide (slide 5)

Three valid closer formats (pick based on the news):

1. **Reaction tweet** â€” invented commentator handle reacts to the news. Uses Template from Â§6 with an invented `@handle`.
2. **Stat card** â€” Template B with the most impactful number of the story.
3. **Key takeaway** â€” Template A with a one-line insight + photo (e.g., foto conceptual de "el futuro de la IA").

### When to use which

- **Reaction tweet:** news that benefits from a "outside voice" (policy news, controversy, launch receptions)
- **Stat card:** news with one killer number
- **Key takeaway:** news where the synthesis/meaning is the hook

---

## 10. Codex image tool â€” photo generation

### Aspect ratios by slide type (non-negotiable)

News photos use **rectangular aspect ratios** that match their designated region on the slide â€” **NOT** the full 4:5 Instagram canvas. Generating at 4:5 results in the subject being cropped or covered by text.

| Slide type | `--aspect-ratio` | Output | Purpose |
|---|---|---|---|
| **Cover (slide 1)** | `4:5` | 1080 Ã— 1350 | Full-bleed photo fills entire canvas; CSS gradient overlay darkens bottom for text |
| **Body text+photo (Template A)** | `16:9` | 1080 Ã— 608 | Photo occupies bottom ~45% of canvas; text + label occupy top ~55% |
| **Tweet avatar** | `1:1` | 1080 Ã— 1080 | Square for circular crop in tweet UI |
| **Closer photo (slide 5 Template A variant)** | `16:9` | 1080 Ã— 608 | Same as body photos |

> Save or resize the selected asset to the target dimensions before referencing it from HTML.

### Default generation flow`r`n`r`nGenerate the asset with Codex's integrated image tool, then save the selected image into `PostTypes/news/Outputs/{topic-slug}/{filename}.png`.`r`n`r`nUse the intended ratio from the table above: 4:5 for covers, 16:9 for body photos, and 1:1 for avatars.

### Naming convention for photo files

```
PostTypes/news/Outputs/{topic-slug}/
â”œâ”€â”€ composition.png       â† cover photo
â”œâ”€â”€ slide3_photo.png      â† text+photo slide 3
â”œâ”€â”€ slide4_photo.png      â† (if slide 4 is Template A)
â”œâ”€â”€ slide5_photo.png      â† (if closer is Template A)
â””â”€â”€ tweet_avatar.png      â† tweet slide avatar (if invented commentator)
```

### Rules

- **Generate ONE photo per slide.** Do not generate variants. The prompt is the craft â€” if the output is wrong, iterate on the prompt, not on the count.
- **Never use `--reference`** â€” per user preference, all news photos are 100% generative. Do not composite real person photos.
- **Never embed text** in prompts. Text = HTML overlay, always.
- **Content policy:** OpenAI rejects named real public figures. If the script fails with `content_policy_violation`, rephrase with role/features instead of the name, or use a reference photo from `Assets/Personas/` (last resort â€” violates the no-reference rule above, so only if the user explicitly OKs it).

### Prompt checklist (before submitting to API)

- [ ] Describes the scene, not the frame
- [ ] Includes "editorial photography" or "film grain" or "cinematic"
- [ ] For covers: positions subject in upper portion, leaves lower area for gradient overlay
- [ ] Ends with "No text, no typography, no logos, no words anywhere in the image"
- [ ] Correct aspect ratio flag set (4:5 for covers, 16:9 for body slides)
- [ ] Real public figures described by role/features, not by name (OpenAI content policy)

---

## 11. Tweet ethics â€” MANDATORY rules

News posts include tweets. **Approved rules (user-locked):**

| Case | What I do |
|---|---|
| **Official company announcement** (ej: "Perplexity anunciÃ³ X") | Research the actual tweet via WebSearch. Reproduce the real tweet faithfully â€” author, handle, text. **Cite, never invent.** |
| **Public CEO statement** (ej: Altman in Senate hearing, Amodei in a conference) | Paraphrase from documented public record only. Attribute to real handle. **If the quote can't be verified, do NOT attribute to a real person.** |
| **Reaction / analysis tweet** (journalist, researcher commentary) | Use **invented plausible handle** (e.g., `@sofia_reyes_ai`) with Codex image tool avatar. Clearly fictional persona. **Never attribute an invented quote to a real person.** |
| **Editorial quote card** (fallback) | If no real source and no need for commentary, use a quote card styled differently from a tweet â€” no Twitter UI, just typographic quote + source citation. |

### Why this matters

Fabricated quotes attributed to real people are **misinformation** â€” screenshots get shared, the user takes the reputational hit when it's debunked. These rules keep the pipeline automatic while protecting the brand.

### When researching real tweets

- Use WebSearch with queries like `"[company name] twitter announcement [topic] [year]"`
- Verify the tweet exists on a reputable source before reproducing
- If the original tweet isn't findable, shift to the editorial quote card option

---

## 12. Headline writing rules

### Language

- **Colombian Spanish, `tÃº` form.** Never voseo ("creÃ¡", "usÃ¡"). Use "crea", "usa", "mira", "descubre".
- Brand names stay in English: "Anthropic", "Perplexity", "Claude", "OpenAI"
- Numbers: prefer digits over words ("40%", "US$2.000 millones", "5 aÃ±os")
- Currency: adapt to LATAM reading ("$2B" â†’ "US$2.000 millones")

### Cover headline style

| Rule | Detail |
|---|---|
| Word count | **6â€“10 words** (tight, punchy, one breath) |
| Case | **ALL CAPS** |
| Font weight | 800 |
| Line count | 2â€“3 lines |
| Keyword highlight | **2â€“3 keywords** in coral and/or yellow marker |
| Tone | Factual, newsworthy â€” **not clickbait**. No exclamation marks, no "Â¡INCREÃBLE!", no "NO VAS A CREER" |

### Highlight pattern â€” which keyword gets which color

| Color | What it marks |
|---|---|
| **Coral text** `#E85D3C` | Brand name (Anthropic, OpenAI), strong noun (CHIPS, AGENTES), verb (ATACARON, FILTRAN) |
| **Yellow marker** `#FFE45C` (dark text inside) | Number/stat (40%, US$2.000M), short impactful noun (GRATIS, AHORA, HOY) |

### Good headlines

- *"ANTHROPIC CONSULTA A **LÃDERES RELIGIOSOS** PARA DEFINIR LA **BRÃšJULA Ã‰TICA** DE SU IA"*
- *"LA **CASA DE SAM ALTMAN** FUE ATACADA **DOS VECES** EN POCOS DÃAS"*
- *"INVESTIGADORES DEMOSTRARON QUE LOS **DESPIDOS POR IA** PUEDEN **ROMPER LA ECONOMÃA**"*

### Bad headlines

- *"Â¡INCREÃBLE lo que hizo Anthropic!"* â€” clickbait
- *"Anthropic"* â€” vacÃ­o
- *"Anthropic reportedly consults religious leaders..."* â€” estÃ¡ en inglÃ©s
- *"Crea tu propia IA Ã©tica"* â€” es un titular de tutorial, no de news

### Tagline (below headline)

- 1 line, all caps, Inter 600, 75% opacity
- Expands the "why this matters" in plain language
- Examples: *"EL AVANCE DE LA IA ABRE PREGUNTAS Ã‰TICAS INESPERADAS"*, *"LO QUE VIENE ESTA SEMANA"*, *"CUANDO LA SEGURIDAD Y LA VISIBILIDAD TIENEN UN COSTO PERSONAL"*

---

## 13. Caption â€” ahora es corto

Porque el contenido vive en los slides, el caption pasa a ser **breve y utilitario** (no informativo largo).

### Formato del caption

- **1â€“3 lÃ­neas** mÃ¡ximo
- **Objetivo:** dar contexto mÃ­nimo para el feed + facilitar bÃºsqueda
- **Sin hashtags** (el user los agrega si quiere)
- **Sin emojis**
- **Sin CTA** ("sÃ­gueme", "guarda")

### Ejemplos

```
Anthropic estÃ¡ consultando a lÃ­deres religiosos y filÃ³sofos para definir los valores con los que entrena a Claude.
```

```
La casa de Sam Altman ha sido atacada dos veces en menos de una semana.
Seguridad personal y figura pÃºblica, el costo del liderazgo en IA.
```

### Workflow del caption

- Generar en el paso final del workflow, despuÃ©s de aprobar todos los slides
- Guardar en `caption.txt` en la carpeta del post
- Presentar junto con los slides al cierre

---

## 14. Workflow when the user asks for a news post

1. **Read this skill** + base rules from [`CLAUDE.md`](../../../CLAUDE.md) + [`news/README.md`](../README.md).
2. **Mandatory visual re-anchoring:** review [`Inspiracion/`](../Inspiracion/) AND [`Favoritos_Claude_Generated/`](../Favoritos_Claude_Generated/) (CLAUDE.md Â§1.5). **Look at the carousel patterns, not just covers.**
3. **Understand the news:** what happened, who's involved, what's the data. If the user gave only a title, WebSearch for the full story.
4. **Draft the slide outline** â€” propose the 5-slide breakdown (headline, tweet angle, body slide 1, body slide 2, closer). Wait for approval.
5. **Propose 2â€“3 cover headline variations** (Colombian Spanish, with keyword highlights marked). Wait for approval.
6. **Research real tweets** if slide 2 is an official announcement (see Â§11). If the source announcement exists, capture the exact tweet text.
7. **Generate photos with Codex image tool** â€” ONE per slide that needs one (cover + 1â€“2 body slides). Cover at `--aspect-ratio 4:5` (full-bleed), body slides at `--aspect-ratio 16:9`. The script handles crop + resize internally.
8. **Present photos to user for review.** Only regenerate if rejected.
9. **Build the HTML for all slides** â€” cover, tweet, text+photo, (optional) white card, closer. Save each as `slide{N}_{descriptor}.html` in the output folder.
10. **Render via `./render.sh PostTypes/news/Outputs/{topic-slug}`** â€” renders all slides at once.
11. **MANDATORY Visual QA** (see [`Skills/visual-qa.md`](../../../Skills/visual-qa.md)) â€” open every PNG, verify no artifacts, text readable, photos correctly positioned, no page dots on any slide, Alta Studio logo visible, SWIPE pill only on cover.
12. **Draft the short caption** (1â€“3 lines), save as `caption.txt`.
13. **Present the complete carousel** â€” all 5 PNGs in order + caption, ready to upload to Instagram.
14. **Ask which slides are favorites** â†’ copy selected PNGs to `Favoritos_Claude_Generated/` (CLAUDE.md Â§1.6).

### Naming convention for news carousel outputs

```
PostTypes/news/Outputs/{topic-slug}/
â”œâ”€â”€ composition.png              â† cover photo (Codex image tool)
â”œâ”€â”€ slide3_photo.png             â† text+photo slide 3 photo
â”œâ”€â”€ slide4_photo.png             â† (optional) text+photo slide 4 photo
â”œâ”€â”€ slide5_photo.png             â† (optional) closer photo
â”œâ”€â”€ tweet_avatar.png             â† (optional) invented commentator avatar
â”œâ”€â”€ slide1_cover.html            â† cover HTML
â”œâ”€â”€ slide1_cover.png             â† rendered cover
â”œâ”€â”€ slide2_tweet.html
â”œâ”€â”€ slide2_tweet.png
â”œâ”€â”€ slide3_text.html
â”œâ”€â”€ slide3_text.png
â”œâ”€â”€ slide4_{text|card}.html
â”œâ”€â”€ slide4_{text|card}.png
â”œâ”€â”€ slide5_closer.html
â”œâ”€â”€ slide5_closer.png
â””â”€â”€ caption.txt
```

- `{topic-slug}`: kebab-case, descriptive. E.g. `anthropic-lideres-religiosos`, `altman-ataques-casa`, `perplexity-billion-build`.

---

## 15. Anti-patterns (news-specific)

- âŒ Single-image news posts (the old format â€” now deprecated)
- âŒ Long captions with 6â€“10 paragraphs of info (content now lives in slides)
- âŒ PIL for text overlay (deprecated â€” all text is HTML + render.sh)
- âŒ Cream background or grid pattern (that's step-by-step identity)
- âŒ `@lucianomusellaa` handle on news slides (news uses Alta Studio logo only)
- âŒ Alta Studio in BOTH corners (only one corner per slide)
- âŒ SWIPE pill on body slides (only on cover)
- âŒ Page dots on any slide (Instagram adds carousel dots natively)
- âŒ Codex image tool generating text, logos, or watermarks (always strip with "No text, no logos, no words")
- âŒ Using `--reference` with real person photos (100% generative per user preference)
- âŒ Generating cover photos at `--aspect-ratio 4:3` (the old split layout) â€” use `4:5` for full-bleed covers with CSS gradient overlay
- âŒ Using the old "photo top 810px + solid black text zone bottom" cover layout â€” creates a visible "marco negro". Use full-bleed photo + CSS gradient instead
- âŒ Generating body slide photos at `--aspect-ratio 4:5` â€” they get cropped to the 608px photo region. Use `16:9` so the full composition is visible
- âŒ Using `backdrop-filter: blur` anywhere â€” headless Chrome strips it, elements render invisible
- âŒ PIL baked fade-to-black on cover photos â€” this was for the old split layout. Full-bleed covers use CSS gradient overlay instead
- âŒ Nesting the bottom-row (tagline + SWIPE pill) inside the headline block â€” Chrome headless clips child content that extends beyond parent's rendered height. Use SEPARATE absolute-positioned elements
- âŒ Alta Studio logo smaller than ~80px on covers â€” it disappears visually. 100px is the target (uniform across all slides)
- âŒ Fabricating quotes attributed to real people (see Â§11 ethics)
- âŒ More than one Template B (white card) in a row â€” needs visual rhythm
- âŒ Headlines in English (always Colombian Spanish)
- âŒ Clickbait ("Â¡INCREÃBLE!", "Â¡NO VAS A CREER!")
- âŒ Generating multiple photo variants per slide (prompt well, generate once, iterate on prompt if needed)
- âŒ Hashtags or emojis in the caption

---

## 16. Quick-reference checklist (run before presenting the carousel)

### Content
- [ ] 4â€“7 slides total (5 is default)
- [ ] Cover has killer headline with 2â€“3 keyword highlights (coral + yellow)
- [ ] Slide 2 is a real official tweet or a quote card (never a fabricated tweet from a real person)
- [ ] Body slides (3, 4) use Template A (text+photo) mostly, B (white card) for punchlines
- [ ] Closer is reaction tweet, stat card, or takeaway â€” chosen for impact
- [ ] Caption is 1â€“3 lines, no hashtags, no emojis

### Visual
- [ ] Every slide is 1080Ã—1350
- [ ] Alta Studio logo in one top corner on every slide (not both, not missing)
- [ ] SWIPE pill only on cover
- [ ] No page dots on any slide (Instagram adds them natively)
- [ ] No `@lucianomusellaa` anywhere
- [ ] Cover photo is Codex image tool at 4:5 (full-bleed), body photos at 16:9, all text/logo-free
- [ ] No black border artifacts (render.sh handles this â€” verify with QA)

### Language
- [ ] Colombian Spanish, `tÃº` form throughout
- [ ] Brand names kept in English
- [ ] Numbers as digits
- [ ] No voseo, no "Â¡!", no clickbait tone

### Pipeline
- [ ] All slides rendered via `./render.sh`
- [ ] Visual QA run on every PNG
- [ ] Output folder follows naming convention
- [ ] Caption saved as `caption.txt`
- [ ] User asked which slides are favorites


