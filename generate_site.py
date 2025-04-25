#!/usr/bin/env python3
import os, datetime, random, matplotlib.pyplot as plt

# ensure output dir exists
os.makedirs('docs', exist_ok=True)

# generate random data chart
x = list(range(10))
y = [random.random() for _ in x]
plt.figure()
plt.plot(x, y, marker='o')
plt.title('Random Data')
plt.xlabel('X'); plt.ylabel('Y')
plt.tight_layout()
chart_path = 'docs/chart.png'
plt.savefig(chart_path)
plt.close()

# write HTML with timestamp
now = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC')
html = f"""<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><title>Auto-updated Chart</title></head>
<body>
  <h1>Auto-updated Chart</h1>
  <p>Last updated: {now}</p>
  <img src="chart.png" alt="Random data chart">
</body>
</html>"""
with open('docs/index.html', 'w') as f:
    f.write(html)