import numpy as np
import gdspy

# Define the spiral parameters
def spiral_points(num_points):
    # Parameter t range
    t = np.linspace(0, 6 * np.pi, num_points)
    # Radius as a function of t
    r = np.exp(-0.1 * t)
    # Parametric equations for the spiral
    x = r * np.cos(t)
    y = r * np.sin(t)
    return x, y

# GDSII Library and Cell Definition
lib = gdspy.GdsLibrary()
cell = lib.new_cell('SPIRAL')

# Number of points to approximate the spiral
num_points = 500
x, y = spiral_points(num_points)

# Convert spiral points to path
path = gdspy.Path(1, (x[0], y[0]))
for i in range(1, num_points):
    path.segment((x[i], y[i]), relative=False)

# Add the path to the cell
cell.add(path)

# Save the layout to a GDS file
lib.write_gds('spiral.gds')

print("Spiral GDS file 'spiral.gds' has been created.")