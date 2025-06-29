import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-2, 2, 0.2)
y = np.arange(-2, 2, 0.2)

X, Y = np.meshgrid(x, y)

Ex = np.cos(X)*np.arcsin(x)  
Ey = X * np.sin(X)*np.cos(X)*np.tan(x)


plt.figure(figsize=(10, 10))
# plt.streamplot(X, Y, Ex, Ey, density=5, linewidth=None, color='#A23BEC')
plt.quiver(X, Y, Ex, Ey, linewidth=None, color='#A23BEC')

plt.grid()
plt.show()
