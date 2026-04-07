# Step_Instagram_Posts

Sistema de generación de **carruseles de Instagram** con un lenguaje visual consistente — covers + step slides + cierre — pensado para la cuenta **@lucianomusellaa**.

El proyecto está diseñado para operarse desde [Claude Code](https://claude.com/claude-code): tú escribes una intención en lenguaje natural ("hagamos un post sobre X") y el agente sigue un workflow definido para producir un carrusel renderizado en PNG, listo para subir.

---

## ¿Qué hace esta herramienta?

A partir de un tema y (opcionalmente) un material fuente, genera:

1. **Un cover** con doble highlight (una palabra coral + otra sobre marcador amarillo) — el formato más "catchy" del sistema.
2. **N step slides** (`PASO 1`, `PASO 2`, …) cada una con headline + subtítulo opcional + mockup visual.
3. **Un slide de cierre** con CTA tipo "follow for more".
4. Un **slide indicator** consistente en toda la serie.
5. Todo renderizado a **1080×1350 px** (4:5 portrait) en PNG, listo para Instagram.

El agente sigue un workflow estricto: re-anclar al lenguaje visual → pedir contexto → proponer desglose en texto → esperar aprobación → generar HTML → renderizar → verificar visualmente → iterar.

---

## Estructura del proyecto

```
Step_Instagram_Posts/
├── CLAUDE.md                          ← instrucciones del agente (autoload en Claude Code)
├── README.md                          ← este archivo
├── Skills/                            ← sistema visual (la "spec" de diseño)
│   ├── instagram-post-design.md       ← BASE: paleta, tipografía, grid, reglas
│   ├── instagram-cover-design.md      ← layouts de cover
│   └── instagram-step-slide-design.md ← layouts de step + cierre
├── Ejemplos/                          ← imágenes de referencia visual
│   ├── Ej_.png   → Cover tipo A (2 logos)
│   ├── Ej_1.png  → Cover tipo B (mockup)
│   ├── Ej_2.png  → Step con subtítulo
│   ├── Ej_3.png  → Cover con screenshot
│   ├── Ej_4.png  → Step sin subtítulo
│   └── Ej_5.png  → Closing "follow for more"
├── Logos/                             ← assets de marca reales
│   └── Claude_AI_symbol.svg
├── Assets/                            ← screenshots e imágenes generadas
├── Outputs/                           ← carruseles renderizados (uno por carpeta)
│   └── {topic-slug}/
│       ├── cover_v1_*.html / .png
│       ├── paso_1_*.html / .png
│       ├── ...
│       └── cierre_cta.html / .png
├── Errors/                            ← marcado de bugs visuales para iteraciones
└── render.sh                          ← batch renderer HTML → PNG (Chrome headless)
```

---

## Reglas no negociables del sistema visual

- **Handle**: siempre `@lucianomusellaa` en la parte superior de cada slide.
- **Idioma**: español **colombiano** con `tú` (nunca voseo argentino: ✅ `crea`, `define`, `instala` / ❌ `creá`, `definí`, `instalá`).
- **Paleta**:
  - Fondo crema `#F5F2ED` con grid sutil `#E8E4DD`
  - Texto principal `#0E0E0E`
  - Acento coral `#E85D3C`
  - Highlight amarillo `#FFE45C`
- **Tipografía**: Inter (500/600/700/800) + JetBrains Mono para código.
- **Canvas**: 1080 × 1350 px.
- **Highlights**:
  - Covers → **doble highlight** (coral + marcador amarillo).
  - Step slides → **single highlight** (coral O amarillo, no ambos).
- **Slide indicator**: dots al pie de cada slide, el actual coral y más grande.

Detalle completo en [CLAUDE.md](CLAUDE.md) y en la carpeta [Skills/](Skills/).

---

## Cómo usarlo (con Claude Code)

1. Clona este repo y ábrelo en Claude Code:
   ```bash
   git clone https://github.com/myprojectops-ai/Step_Instagram_Posts.git
   cd Step_Instagram_Posts
   ```
2. Crea un `.env` con tu key de Gemini (si vas a usar generación de imágenes):
   ```
   GEMINI_API_KEY=tu_key_aqui
   ```
3. Asegúrate de tener Google Chrome instalado (lo usa `render.sh` en modo headless).
4. En Claude Code, dispara un nuevo post con cualquiera de estas frases:
   - `nuevo post: {tema}`
   - `hagamos un post sobre {tema}`
   - `generemos un carrusel de {tema}`
   - `quiero un post de {tema}`
5. El agente te pedirá el contexto faltante, te propondrá el desglose en texto, y solo después de tu aprobación generará y renderizará los slides.

### Renderizar manualmente

```bash
./render.sh Outputs/{topic-slug}
```

Convierte todos los `.html` de la carpeta a PNGs del mismo nombre.

---

## Workflow estándar (resumen)

1. **Re-anclar visualmente** — leer skills + abrir referencias de `Ejemplos/`.
2. **Pedir contexto** — slides, fuente, keywords, assets, tono.
3. **Proponer desglose en texto** — covers (3 variantes), pasos, cierre.
4. **Esperar aprobación** del usuario.
5. **Crear carpeta** `Outputs/{topic-slug}/`.
6. **Escribir HTML** de cada slide (CSS inline).
7. **Renderizar** con `./render.sh`.
8. **Verificar** cada PNG visualmente.
9. **Presentar** el carrusel.
10. **Iterar** slide por slide.

Workflow completo en [CLAUDE.md](CLAUDE.md) sección 4.

---

## Créditos visuales

El lenguaje visual está inspirado en el estilo de creadores de contenido AI (referencia: @ramiro.cubria — solo estilo visual, no el handle). El proyecto está adaptado a la voz y audiencia de **@lucianomusellaa**.
