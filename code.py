import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# a function that calculate the value of l, given n and delta
def calculate_average_l_value(n, delta):
    result = (2 * n**2 * delta + 2 * n - 1) / (n - 1 + 2 * n * delta)
    return math.floor(result)

# range of values that we check
n_range = np.linspace(2, 19, 100)
delta_range = np.linspace(0, 10, 100)

# creating a mesh grid
n_meshgrid, delta_meshgrid = np.meshgrid(n_range, delta_range)

# calculate the l values for every value
result = np.vectorize(calculate_average_l_value)(n_meshgrid, delta_meshgrid)

# drawing the 3D graph
figure = plt.figure(figsize=(12, 8))
axis = figure.add_subplot(111, projection='3d')
surface = axis.plot_surface(delta_meshgrid, n_meshgrid, result, cmap='viridis', edgecolor='none')

# labels
axis.set_xlabel('delta')
axis.set_ylabel('n')
axis.set_zlabel('l')
axis.set_title("average minimal l value given n and delta")

# color bar, for easy reading
figure.colorbar(surface, ax=axis, label='l')

# showing the graph
plt.show()
