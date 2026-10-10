"""Illustrative weak-field gravitational light-deflection plot.

This is an educational approximation, not full GR ray tracing.
Run from the repository root: python src/lensing_demo.py
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

# Geometric units: G = c = 1. Choose M = 1 for a dimensionless example.
M = 1.0
b_over_M = np.linspace(10.0, 50.0, 400)  # impact parameter in units of M
b = b_over_M * M

# Leading-order weak-field approximation: alpha ≈ 4M/b (radians).
alpha = 4.0 * M / b
alpha_mrad = alpha * 1_000.0

fig, ax = plt.subplots(figsize=(7.5, 4.8))
ax.plot(b_over_M, alpha_mrad, linewidth=2)
ax.set_xlabel(r"Impact parameter $b/M$")
ax.set_ylabel("Deflection angle (milliradians)")
ax.set_title("Weak-field gravitational light deflection")
ax.grid(True, alpha=0.3)
fig.tight_layout()

output = Path("outputs")
output.mkdir(parents=True, exist_ok=True)
file_path = output / "deflection_vs_impact_parameter.png"
fig.savefig(file_path, dpi=200)
print(f"Saved plot to {file_path}")
plt.show()
