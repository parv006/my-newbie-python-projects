import numpy as np
import matplotlib.pyplot as plt # type: ignor

x = np.arange(-2, 2, 0.5)
y = np.arange(-2, 2, 0.5)
X, Y = np.meshgrid(x, y)

Ex = np.cos(X)
Ey = X * np.sin(X) * np.cos(X)
magnitude = np.sqrt(Ex**2 + Ey**2)

norm = plt.Normalize(magnitude.min(), magnitude.max())
cmap = plt.cm.coolwarm

colors = cmap(norm(magnitude)).reshape(-1, 4)
Xf = X.flatten()
Yf = Y.flatten()
Exf = Ex.flatten()
Eyf = Ey.flatten()

fig, ax = plt.subplots(figsize=(10, 10))
q = ax.quiver(Xf, Yf, Exf, Eyf, color=colors, scale=1, scale_units='xy', angles='xy')

sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])
fig.colorbar(sm, ax=ax, label='Vector Magnitude')

ax.grid()
ax.set_aspect('equal')
plt.show()