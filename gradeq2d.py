import matplotlib.pyplot as plt
import numpy as np

# function definition to compute magnitude of a vector
def magnitude(vector):
    return np.sqrt(sum(pow(element, 2) for element in vector))

def fun(x, y):
    return 5*x**2 + 5*y**2 + 8*x*y - 26*x - 28 *y + 41

# function to calculate the gradient of f
def grad(a, r):
    return 2*np.matmul(np.transpose(a), r)

# function to calculate the multiplicator gamma
def gamma(M, r):
    return -1/2.0*np.matmul(np.transpose(r),r)/np.matmul(np.transpose(r),np.matmul(M,r))

ax = plt.figure().add_subplot(projection='3d')
# Customize the axis.
ax.set_xlim(-1, 5)
ax.set_ylim(-1, 5)
ax.set_zlim(0, 20)
# Make data.
x = np.arange(-1, 5, 0.01)
y = np.arange(-1, 5, 0.01)
x, y = np.meshgrid(x, y)
z = fun(x, y)

# Plot the surface.
#surf = ax.plot_surface(x, y, z, cmap=cm.coolwarm,
#                       linewidth=0, antialiased=False)
surf = ax.plot_surface(x, y, z, alpha = 0.02)

CS = ax.contour(x, y, z, 300)
ax.clabel(CS, inline=True, fontsize=10)

a = 1.0*np.array([[2, 1],
                  [1, 2]])

b = 1.0*np.array([4, 5])

# initial guess
x = 1.0*np.array([5, 2])

M = np.matmul(a, np.transpose(a))

for i in range(16):
    r = np.matmul(a, x) - b
    
    gradienten = grad(a, r)
    gam = gamma(M, r)
    g = gam*gradienten

    # draw vectors
    ax.quiver(x[0], x[1], 0, g[0], g[1], 0, length=1, color = 'r')

    x += g

    print("x = ", x)

plt.show()