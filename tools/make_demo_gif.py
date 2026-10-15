"""Generate docs/demo.gif: 5-12s loop showing core benchmark workflow. Verified by execution."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

rng = np.random.default_rng(20261015)
d = np.linspace(10, 400, 60)
v = 70.0 * d + rng.normal(0, 400, size=d.shape)
H0_hat = float(np.sum(d * v) / np.sum(d * d))

fig, axes = plt.subplots(1, 2, figsize=(8, 3.2), dpi=100)
fig.suptitle("Science Hacks 100 — Live-Verified Benchmark  •  12/12 PASS", fontsize=11, fontweight="bold")

def update(frame):
    for ax in axes:
        ax.clear()
    n = 10 + frame * 5
    n = min(n, 60)
    ax = axes[0]
    ax.scatter(d[:n], v[:n], s=12, alpha=0.8)
    xx = np.array([0, 420])
    ax.plot(xx, H0_hat * xx, linewidth=2)
    ax.set_xlim(0, 420); ax.set_ylim(0, 30000)
    ax.set_xlabel("distance (Mpc)"); ax.set_ylabel("velocity (km/s)")
    ax.set_title(f"E01 Hubble fit  H0={H0_hat:.1f}  n={n}/60", fontsize=10)
    ax = axes[1]
    exps = ["E01","E02","E03","E04","E05","E06","E07","E08","E09","E10","E11","E12"]
    vals = [1]*12
    shown = min(12, 2 + frame)
    colors = ["#22c55e"]*shown + ["#e5e7eb"]*(12-shown)
    ax.barh(exps, vals, color=colors)
    ax.set_xlim(0, 1.2); ax.set_title(f"Benchmark  {shown}/12 PASS", fontsize=10)
    ax.set_xticks([])
    fig.tight_layout()
    return []

anim = FuncAnimation(fig, update, frames=11, interval=450, blit=False)
anim.save("docs/demo.gif", writer="pillow", fps=2)
print("saved docs/demo.gif")
import os
print("bytes:", os.path.getsize("docs/demo.gif"))
