import numpy as np
import matplotlib.pyplot as plt

# Generate data
x = np.linspace(0, 4 * np.pi, 500)
y = np.sin(x)
colors = plt.cm.viridis((y + 1) / 2)

plt.figure(figsize=(10, 6))
plt.scatter(x, y, c=colors, s=40, edgecolor='k', alpha=0.8)
plt.title('Colorful Sine Wave Visualization', fontsize=18)
plt.xlabel('X Value', fontsize=14)
plt.ylabel('Sine of X', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()
