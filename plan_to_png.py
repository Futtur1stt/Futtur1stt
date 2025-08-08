#!/usr/bin/env python3
import textwrap
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

PLAN_MD = Path('/workspace/plan.md')
OUT_PNG = Path('/workspace/plan.png')

# Basic settings
WIDTH = 1600
PADDING = 40
BG = (250, 250, 250)
FG = (20, 20, 20)
TITLE_FG = (0, 0, 0)
MONO_FG = (30, 30, 30)

# Try to load a common font
try:
    font_regular = ImageFont.truetype("DejaVuSans.ttf", 22)
    font_bold = ImageFont.truetype("DejaVuSans-Bold.ttf", 26)
    font_mono = ImageFont.truetype("DejaVuSansMono.ttf", 20)
except Exception:
    font_regular = ImageFont.load_default()
    font_bold = ImageFont.load_default()
    font_mono = ImageFont.load_default()

md = PLAN_MD.read_text(encoding='utf-8')
lines = md.splitlines()

# Very simple markdown-ish rendering: headings, bullets, code ticks simplified
wrapped_lines = []
wrap_width = 120
for raw in lines:
    line = raw.rstrip()
    if line.startswith('# '):
        wrapped_lines.append(('h1', line[2:].strip()))
    elif line.startswith('## '):
        wrapped_lines.append(('h2', line[3:].strip()))
    elif line.startswith('### '):
        wrapped_lines.append(('h3', line[4:].strip()))
    elif line.startswith('- '):
        content = line[2:]
        for wl in textwrap.wrap(content, width=wrap_width):
            wrapped_lines.append(('li', wl))
    elif line[:2].isdigit() and line[2:4] == ') ':
        # numeric list like '1) '
        content = line[4:]
        for wl in textwrap.wrap(content, width=wrap_width):
            wrapped_lines.append(('li', wl))
    elif line.strip().startswith('```'):
        # ignore code fences in this simple renderer
        continue
    elif line.strip() == '':
        wrapped_lines.append(('blank', ''))
    else:
        for wl in textwrap.wrap(line, width=wrap_width):
            wrapped_lines.append(('p', wl))

# Estimate height
line_heights = {
    'h1': 40,
    'h2': 34,
    'h3': 30,
    'li': 28,
    'p': 28,
    'blank': 18,
}
height = PADDING * 2 + sum(line_heights[k] for k, _ in wrapped_lines)
img = Image.new('RGB', (WIDTH, height), BG)
ctx = ImageDraw.Draw(img)

y = PADDING
for kind, text in wrapped_lines:
    if kind == 'h1':
        ctx.text((PADDING, y), text, font=font_bold, fill=TITLE_FG)
        y += line_heights[kind]
    elif kind == 'h2':
        ctx.text((PADDING, y), text, font=font_bold, fill=TITLE_FG)
        y += line_heights[kind]
    elif kind == 'h3':
        ctx.text((PADDING, y), text, font=font_regular, fill=TITLE_FG)
        y += line_heights[kind]
    elif kind == 'li':
        ctx.text((PADDING + 24, y), '• ' + text, font=font_regular, fill=FG)
        y += line_heights[kind]
    elif kind == 'p':
        ctx.text((PADDING, y), text, font=font_regular, fill=FG)
        y += line_heights[kind]
    elif kind == 'blank':
        y += line_heights[kind]

img.save(OUT_PNG)
print(f"Saved {OUT_PNG}")