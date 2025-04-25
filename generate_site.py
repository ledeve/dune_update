#!/usr/bin/env python3
import os, random, matplotlib.pyplot as plt

out_dir = 'docs/assets/charts'
os.makedirs(out_dir, exist_ok=True)

# Example: chart1 and chart2
for name in ('chart1','chart2'):
    x = list(range(10))
    y = [random.random() for _ in x]
    plt.figure()
    plt.plot(x, y, marker='o')
    plt.title(name)
    plt.tight_layout()
    plt.savefig(f"{out_dir}/{name}.png", dpi=100)
    plt.close()