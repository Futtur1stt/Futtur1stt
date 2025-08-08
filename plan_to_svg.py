#!/usr/bin/env python3
import textwrap
from pathlib import Path

PLAN_MD = Path('/workspace/plan.md')
OUT_SVG = Path('/workspace/plan.svg')

WIDTH = 1600
PADDING = 20
LINE_HEIGHTS = {
    'h1': 40,
    'h2': 32,
    'h3': 28,
    'li': 24,
    'p': 24,
    'blank': 16,
}
WRAP_WIDTH = 120

md = PLAN_MD.read_text(encoding='utf-8')
lines = md.splitlines()

wrapped = []
for raw in lines:
    line = raw.rstrip()
    if line.startswith('# '):
        wrapped.append(('h1', line[2:].strip()))
    elif line.startswith('## '):
        wrapped.append(('h2', line[3:].strip()))
    elif line.startswith('### '):
        wrapped.append(('h3', line[4:].strip()))
    elif line.startswith('- '):
        content = line[2:].strip()
        for wl in textwrap.wrap(content, width=WRAP_WIDTH):
            wrapped.append(('li', wl))
    elif line[:2].isdigit() and line[2:4] == ') ':
        content = line[4:].strip()
        for wl in textwrap.wrap(content, width=WRAP_WIDTH):
            wrapped.append(('li', wl))
    elif line.strip().startswith('```'):
        # ignore code fences
        continue
    elif line.strip() == '':
        wrapped.append(('blank', ''))
    else:
        for wl in textwrap.wrap(line, width=WRAP_WIDTH):
            wrapped.append(('p', wl))

height = PADDING * 2 + sum(LINE_HEIGHTS[k] for k, _ in wrapped)

# SVG header
svg_lines = [
    f'<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{height}" viewBox="0 0 {WIDTH} {height}">',
    '<style>',
    '  .bg { fill: #FAFAFA; }',
    '  .h1 { font: 700 26px system-ui, -apple-system, Segoe UI, Roboto, Arial; fill: #111; }',
    '  .h2 { font: 700 22px system-ui, -apple-system, Segoe UI, Roboto, Arial; fill: #111; }',
    '  .h3 { font: 600 20px system-ui, -apple-system, Segoe UI, Roboto, Arial; fill: #111; }',
    '  .p, .li { font: 400 18px system-ui, -apple-system, Segoe UI, Roboto, Arial; fill: #222; }',
    '</style>',
    f'<rect class="bg" x="0" y="0" width="{WIDTH}" height="{height}" />'
]

y = PADDING
for kind, text in wrapped:
    if kind == 'blank':
        y += LINE_HEIGHTS[kind]
        continue
    cls = kind if kind in ('h1','h2','h3','li') else 'p'
    x = PADDING + (24 if kind == 'li' else 0)
    # escape basic xml characters
    text_esc = (text.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;'))
    svg_lines.append(f'<text class="{cls}" x="{x}" y="{y}">{("• " if kind=="li" else "")}{text_esc}</text>')
    y += LINE_HEIGHTS[kind]

svg_lines.append('</svg>')
OUT_SVG.write_text('\n'.join(svg_lines), encoding='utf-8')
print(f"Saved {OUT_SVG}")