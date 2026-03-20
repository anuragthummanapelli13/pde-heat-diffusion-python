import numpy as np
import matplotlib.pyplot as plt

# Grid parameters
nx, ny = 50, 50
dx = dy = 1.0
alpha = 0.01  # thermal diffusivity
dt = 0.1
steps = 100

# Initialize temperature grid
u = np.zeros((nx, ny))

# Initial condition (hot center)
u[nx//2, ny//2] = 100

def update(u):
    u_new = u.copy()
    for i in range(1, nx-1):
        for j in range(1, ny-1):
            u_new[i, j] = u[i, j] + alpha * dt * (
                (u[i+1, j] - 2*u[i, j] + u[i-1, j]) / dx**2 +
                (u[i, j+1] - 2*u[i, j] + u[i, j-1]) / dy**2
            )
    return u_new

# Time stepping
for _ in range(steps):
    u = update(u)

# Plot result
plt.imshow(u, cmap='hot')
plt.colorbar()
plt.title("2D Heat Diffusion")
plt.show()
