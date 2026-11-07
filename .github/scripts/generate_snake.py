#!/usr/bin/env python3
import random

W = 880
H = 195
cols = 53
rows = 7
cell_size = 11
gap = 3
grid_x = 42
grid_y = 52

bg = '#0A101F'
panel = '#0C1426'
border = 'rgba(34, 211, 238, 0.28)'
text_dim = '#475569'
text_muted = '#94A3B8'
cyan = '#22D3EE'
violet = '#A78BFA'
violet2 = '#7C3AED'
emerald = '#10B981'

levels = ['#161F36', '#312E81', '#6D28D9', '#A78BFA', '#22D3EE']
weights = [0.52, 0.20, 0.14, 0.09, 0.05]

random.seed(42)
cells_svg = []
for c in range(cols):
    for r in range(rows):
        x = grid_x + c * (cell_size + gap)
        y = grid_y + r * (cell_size + gap)
        w = list(weights)
        if c > 35:
            w[0] -= 0.18
            w[2] += 0.09
            w[3] += 0.06
            w[4] += 0.03
        if r in (1, 2, 3, 4):
            w[0] -= 0.05
            w[1] += 0.05
        col = random.choices(levels, weights=w)[0]
        cells_svg.append(f'<rect x="{x}" y="{y}" width="{cell_size}" height="{cell_size}" rx="2.5" fill="{col}"/>')

months = ['Nov', 'Dec', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov']
month_svg = []
for i, m in enumerate(months):
    mx = grid_x + int(i * (cols / 12) * (cell_size + gap))
    month_svg.append(f'<text x="{mx}" y="{grid_y - 12}" font-size="10" fill="{text_muted}">{m}</text>')

days = [('Mon', 1), ('Wed', 3), ('Fri', 5)]
day_svg = []
for d, r in days:
    dy = grid_y + r * (cell_size + gap) + 9
    day_svg.append(f'<text x="16" y="{dy}" font-size="10" fill="{text_dim}">{d}</text>')

waypoints = [
    (2, 1), (12, 1), (12, 5), (22, 5), (22, 2), (32, 2), (32, 6), (42, 6),
    (42, 1), (51, 1), (51, 5), (46, 5), (46, 0), (36, 0), (36, 4), (26, 4),
    (26, 0), (16, 0), (16, 3), (2, 3), (2, 1)
]

px_points = []
for c, r in waypoints:
    px = grid_x + c * (cell_size + gap) + cell_size / 2
    py = grid_y + r * (cell_size + gap) + cell_size / 2
    px_points.append(f'{px},{py}')

path_d = 'M ' + ' L '.join(px_points)

snake_svg = f'''
  <path id="snakePath" d="{path_d}" fill="none" stroke="none"/>
  <circle r="5.5" fill="{cyan}">
    <animateMotion dur="24s" repeatCount="indefinite" path="{path_d}"/>
  </circle>
  <circle r="4.5" fill="{violet}" opacity="0.85">
    <animateMotion dur="24s" begin="-0.25s" repeatCount="indefinite" path="{path_d}"/>
  </circle>
  <circle r="3.8" fill="{violet2}" opacity="0.7">
    <animateMotion dur="24s" begin="-0.5s" repeatCount="indefinite" path="{path_d}"/>
  </circle>
  <circle r="3" fill="#6D28D9" opacity="0.55">
    <animateMotion dur="24s" begin="-0.75s" repeatCount="indefinite" path="{path_d}"/>
  </circle>
  <circle r="2.2" fill="#312E81" opacity="0.4">
    <animateMotion dur="24s" begin="-1.0s" repeatCount="indefinite" path="{path_d}"/>
  </circle>
'''

legend_x = W - 150
legend_y = H - 20
legend_svg = [
    f'<text x="{legend_x - 30}" y="{legend_y + 9}" font-size="9" fill="{text_dim}">Less</text>'
]
for i, col in enumerate(levels):
    lx = legend_x + i * 14
    legend_svg.append(f'<rect x="{lx}" y="{legend_y}" width="10" height="10" rx="2" fill="{col}"/>')
legend_svg.append(f'<text x="{legend_x + 5 * 14 + 4}" y="{legend_y + 9}" font-size="9" fill="{text_dim}">More</text>')

svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" role="img" aria-label="GitHub Contributions">
  <rect width="{W}" height="{H}" rx="12" fill="{panel}" stroke="{border}" stroke-width="1.2"/>
  <text x="20" y="24" font-size="11" font-weight="700" letter-spacing="2" fill="{cyan}">CONTRIBUTIONS.MAP</text>
  <circle cx="172" cy="20" r="3.5" fill="{emerald}">
    <animate attributeName="opacity" values="1;0.25;1" dur="1.8s" repeatCount="indefinite"/>
  </circle>
  <text x="183" y="24" font-size="10" fill="{text_dim}">--live-graph</text>
  <line x1="20" y1="32" x2="{W-20}" y2="32" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>
  
  {''.join(month_svg)}
  {''.join(day_svg)}
  {''.join(cells_svg)}
  {snake_svg}
  {''.join(legend_svg)}
</svg>'''

with open('github-contribution-grid-snake.svg', 'w') as f:
    f.write(svg_content)
with open('snake-dark.svg', 'w') as f:
    f.write(svg_content)

print('Generated github-contribution-grid-snake.svg and snake-dark.svg successfully!')
