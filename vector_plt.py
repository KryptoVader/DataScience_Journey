import matplotlib.pyplot as plt
import numpy as np

# Define vectors
x = np.array([0, 1, 2, 3])
y = np.array([0, 1, 2, 3])
u = np.array([1, 2, 3, 4])
v = np.array([2, 3, 4, 5])

# Compute vector magnitudes
magnitude = np.sqrt(u**2 + v**2)

# Normalize colors based on magnitude
norm = plt.Normalize(magnitude.min(), magnitude.max())
colors = plt.cm.viridis(norm(magnitude))

# Plot setup
plt.figure(figsize=(8, 8))
plt.quiver(x, y, u, v, color=colors, angles='xy', scale_units='xy', scale=1, width=0.007)

# Add vector labels with magnitude
for i in range(len(x)):
    plt.text(x[i] + u[i]*0.5, y[i] + v[i]*0.5, f"|V{i+1}|={magnitude[i]:.2f}",
             fontsize=9, color='black', ha='center', va='center',
             bbox=dict(facecolor='white', alpha=0.6, edgecolor='gray'))

# Set axis limits to fit vectors
plt.xlim(-1, max(x + u) + 1)
plt.ylim(-1, max(y + v) + 1)

# Draw central axes
plt.axhline(0, color='gray', linewidth=1)
plt.axvline(0, color='gray', linewidth=1)

# Grid and labels
plt.grid(True, linestyle='--', alpha=0.5)
plt.xlabel("X-Axis", fontsize=12)
plt.ylabel("Y-Axis", fontsize=12)
plt.title("Vector Field Visualization", fontsize=14, fontweight='bold')

plt.gca().set_aspect('equal')  # Keep aspect ratio equal
plt.tight_layout()
plt.show()
