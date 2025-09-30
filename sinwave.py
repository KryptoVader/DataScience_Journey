import numpy as np
import matplotlib.pyplot as plt

# Define the input range
x = np.linspace(0, 2 * np.pi, 1000)

# Define the function: 3 * sin^2(x) * cos(x)
y = 3 * (np.sin(x)**2) * np.cos(x)

# Plot
plt.plot(x, y)
plt.title("Plot of 3 * sin²(x) * cos(x)")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()
