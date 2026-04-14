from PIL import Image, ImageDraw, ImageFont
import os

out_dir = os.path.dirname(os.path.abspath(__file__))
FONT_DIR = 'C:/Visual_posts/Assets/Fonts'

# Fonts
font_handle = ImageFont.truetype(os.path.join(FONT_DIR, 'Inter-Medium.ttf'), 24)
font_title_big = ImageFont.truetype(os.path.join(FONT_DIR, 'Inter-ExtraBold.ttf'), 64)
font_slide_title = ImageFont.truetype(os.path.join(FONT_DIR, 'Inter-ExtraBold.ttf'), 42)
font_subtitle = ImageFont.truetype(os.path.join(FONT_DIR, 'Inter-Medium.ttf'), 26)
font_slide_num = ImageFont.truetype(os.path.join(FONT_DIR, 'Inter-Bold.ttf'), 18)
font_body = ImageFont.truetype(os.path.join(FONT_DIR, 'Inter-Medium.ttf'), 22)
font_slide_desc = ImageFont.truetype(os.path.join(FONT_DIR, 'Inter-Medium.ttf'), 23)

CORAL = '#E85D3C'
YELLOW = '#FFE45C'
BLACK = '#0E0E0E'
GREY = '#8A8780'
BODY = '#3A3A38'
W = 1080


def load_comp(name):
    img = Image.open(os.path.join(out_dir, name)).convert('RGBA')
    if img.size != (1080, 1350):
        img = img.resize((1080, 1350), Image.LANCZOS)
    return img


def center_x(draw, text, font):
    """Return x to center text on canvas."""
    bbox = draw.textbbox((0, 0), text, font=font)
    return (W - (bbox[2] - bbox[0])) // 2


def text_w(draw, text, font):
    bbox = draw.textbbox((0, 0), text, font=font)
    return bbox[2] - bbox[0]


def draw_centered(draw, text, y, font, fill):
    x = center_x(draw, text, font)
    draw.text((x, y), text, font=font, fill=fill)


def draw_yellow_hl(draw, text, x, y, font, text_color=None):
    """Draw yellow highlight properly centered around text."""
    if text_color is None:
        text_color = BLACK
    # Get actual bounding box at the real position
    bbox = draw.textbbox((x, y), text, font=font)
    pad_x, pad_y = 10, 6
    draw.rectangle(
        [bbox[0] - pad_x, bbox[1] - pad_y, bbox[2] + pad_x, bbox[3] + pad_y],
        fill=YELLOW,
    )
    draw.text((x, y), text, font=font, fill=text_color)
    return bbox[2] - bbox[0]


def draw_dots(draw, current, total, y):
    dot_r = 5
    gap = 16
    total_w = total * (dot_r * 2) + (total - 1) * gap
    sx = (W - total_w) // 2
    for i in range(total):
        cx = sx + i * (dot_r * 2 + gap) + dot_r
        cy = y + dot_r
        c = CORAL if i == current else '#D4D0C8'
        draw.ellipse([cx - dot_r, cy - dot_r, cx + dot_r, cy + dot_r], fill=c)


def draw_two_tone_centered(draw, parts, y, font):
    """Draw text with mixed colors, centered. parts = [(text, color), ...]"""
    total = sum(text_w(draw, t, font) for t, _ in parts)
    x = (W - total) // 2
    for t, c in parts:
        draw.text((x, y), t, font=font, fill=c)
        x += text_w(draw, t, font)


# ============================================================
# SLIDE 1: COVER
# ============================================================
canvas = load_comp('cover_composition.png')
draw = ImageDraw.Draw(canvas)

# Handle
draw_centered(draw, '@lucianomusellaa', 50, font_handle, GREY)

# Title - BIGGER (64px) and LOWER (y=280)
y_t = 280

# Line 1: "Ahorro" + [4 horas] yellow + "de mi"
parts_1a = 'Ahorro '
parts_1h = '4 horas'
parts_1b = ' de mi'

w_1a = text_w(draw, parts_1a, font_title_big)
w_1h = text_w(draw, parts_1h, font_title_big)
w_1b = text_w(draw, parts_1b, font_title_big)
hl_pad = 20  # total horizontal padding of highlight
line1_total = w_1a + w_1h + hl_pad + w_1b
x1 = (W - line1_total) // 2

draw.text((x1, y_t), parts_1a, font=font_title_big, fill=BLACK)
draw_yellow_hl(draw, parts_1h, x1 + w_1a + hl_pad // 2, y_t, font_title_big, BLACK)
draw.text((x1 + w_1a + w_1h + hl_pad, y_t), parts_1b, font=font_title_big, fill=BLACK)

# Line 2: "dia con" + "Claude Code" coral
y_t2 = y_t + 80
draw_two_tone_centered(draw, [
    ('dia con ', BLACK),
    ('Claude Code', CORAL),
], y_t2, font_title_big)

# Subtitle
draw_centered(draw, 'Mis workflows favoritos', y_t2 + 90, font_subtitle, GREY)

# Slide indicator + Desliza
draw_dots(draw, 0, 4, 1300)
desliza = 'Desliza  \u2192'
dw = text_w(draw, desliza, font_slide_num)
draw.text((W - dw - 50, 1300), desliza, font=font_slide_num, fill=GREY)

canvas.convert('RGB').save(os.path.join(out_dir, 'slide1_cover.png'), quality=95)
print('Slide 1 saved')


# ============================================================
# SLIDE 2: Refactoriza codigo — card bbox (176,272)-(903,1077)
# Title above card, description inside card bottom
# ============================================================
canvas = load_comp('slide2_composition.png')
draw = ImageDraw.Draw(canvas)

draw_centered(draw, '@lucianomusellaa', 40, font_handle, GREY)

# Title above card (card starts at y=272)
draw_centered(draw, 'Refactoriza codigo', 95, font_slide_title, BLACK)
draw_two_tone_centered(draw, [
    ('completo en ', BLACK),
    ('segundos', CORAL),
], 148, font_slide_title)

# Description inside card bottom area (card bottom at y=1077)
# The code editor takes roughly top 60% of card, white space below ~y=850-1050
desc = [
    'Le digo que refactorice un archivo',
    'y reestructura todo sin romper nada.',
    'Lo que antes tomaba 1 hora,',
    'ahora son 30 segundos.',
]
y_d = 890
for line in desc:
    draw_centered(draw, line, y_d, font_slide_desc, BODY)
    y_d += 34

draw_dots(draw, 1, 4, 1300)

canvas.convert('RGB').save(os.path.join(out_dir, 'slide2_refactoriza.png'), quality=95)
print('Slide 2 saved')


# ============================================================
# SLIDE 3: Depura errores — card bbox (156,366)-(923,983)
# Title above card, description below card
# ============================================================
canvas = load_comp('slide3_composition.png')
draw = ImageDraw.Draw(canvas)

draw_centered(draw, '@lucianomusellaa', 40, font_handle, GREY)

# Title above card (card starts at y=366)
draw_centered(draw, 'Depura errores sin', 95, font_slide_title, BLACK)
draw_two_tone_centered(draw, [
    ('buscar en ', BLACK),
    ('Stack Overflow', CORAL),
], 148, font_slide_title)

# Description below card (card ends at y=983)
desc = [
    'Le pego el error y me da la solucion',
    'con contexto de MI proyecto.',
    'Entiende mis archivos, mis dependencias,',
    'y sugiere el fix exacto.',
]
y_d = 1020
for line in desc:
    draw_centered(draw, line, y_d, font_slide_desc, BODY)
    y_d += 34

draw_dots(draw, 2, 4, 1300)

canvas.convert('RGB').save(os.path.join(out_dir, 'slide3_depura.png'), quality=95)
print('Slide 3 saved')


# ============================================================
# SLIDE 4: Tests + docs — card bbox (206,331)-(873,1027)
# Title above card, description inside card bottom, CTA below
# ============================================================
canvas = load_comp('slide4_composition.png')
draw = ImageDraw.Draw(canvas)

draw_centered(draw, '@lucianomusellaa', 40, font_handle, GREY)

# Title above card (card starts at y=331)
draw_centered(draw, 'Genera tests y docs', 95, font_slide_title, BLACK)
draw_two_tone_centered(draw, [
    ('en ', BLACK),
    ('automatico', CORAL),
], 148, font_slide_title)

# Description inside card bottom (icons cycle in center, white space below ~y=820-1000)
desc = [
    'Lo tedioso lo hace Claude Code.',
    'Tests unitarios, documentacion, types.',
    'Tu te enfocas en lo que importa:',
    'construir el producto.',
]
y_d = 840
for line in desc:
    draw_centered(draw, line, y_d, font_slide_desc, BODY)
    y_d += 34

# CTA below card
draw_centered(draw, 'Guarda este post para cuando lo necesites', 1090, font_body, CORAL)

draw_dots(draw, 3, 4, 1300)

canvas.convert('RGB').save(os.path.join(out_dir, 'slide4_tests.png'), quality=95)
print('Slide 4 saved')

print('ALL SLIDES DONE')
