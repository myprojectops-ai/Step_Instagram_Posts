# Personas — Fotos de personas reales

Carpeta global para fotos de personas (CEOs, fundadores, figuras públicas) que se usan en los posts. Compartida entre todos los tipos de posts.

## Cómo nombrar los archivos

Usa el formato: `nombre_apellido.png` (o `.jpg`). Ejemplos:

- `dario_amodei.png`
- `andy_jassy.png`
- `sam_altman.png`
- `aravind_srinivas.png`
- `mark_zuckerberg.png`

## Cómo conseguir las fotos

Busca en Google: `"{nombre} headshot"` o `"{nombre} press photo"`. Usa fotos de buena resolución (mínimo 800px de ancho), preferiblemente con fondo limpio o que se vea bien con un overlay oscuro encima.

## Uso

Claude las referencia desde los HTMLs de los posts vía `<img>` con ruta relativa. No es necesario recortarlas — el CSS del post se encarga del crop y overlay.
