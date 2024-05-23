import numpy as np
import matplotlib.pyplot as pl
from mpl_toolkits.mplot3d import Axes3D as ax3

A = 10
x = np.linspace(-5.12, 5.12, 100)
y = np.linspace(-5.12, 5.12, 100)
X, Y = np.meshgrid(x, y)
Z = A + (X**2 - A * np.cos(2 * np.pi * X)) + (Y**2 - A * np.cos(2 * np.pi * Y))

fig = pl.figure(figsize=(10,8))
ax = fig.add_subplot(111, projection='3d')

surf = ax.plot_surface(X, Y, Z, cmap='inferno')
ax.set_title('Rastrigin')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('F(x, y)')
fig.colorbar(surf, ax=ax, shrink=0.5, aspect=5)

pl.show()