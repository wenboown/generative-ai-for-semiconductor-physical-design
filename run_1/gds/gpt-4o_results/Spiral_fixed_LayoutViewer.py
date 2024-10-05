import gdspy
import numpy as np

# Create a new GDSII library
lib = gdspy.GdsLibrary()

# Create a new cell in the library
cell = lib.new_cell('SPIRAL')

# Define the parameters for the parametric spiral
t = np.linspace(0, 6 * np.pi, 1000)
r = np.exp(-0.1 * t)
theta = t

# Convert polar coordinates (theta, r) to Cartesian coordinates (x, y)
x = r * np.cos(theta)
y = r * np.sin(theta)

# Create the path for the spiral
path = gdspy.Path(1, (x[0], y[0]))

for x_point, y_point in zip(x, y):
    path.segment([(x_point, y_point)], width=1, relative=False)

# Add the spiral path to the cell
cell.add(path)

# Save the library in a GDSII file
lib.write_gds('parametric_spiral.gds')

# Optionally display it using the internal viewer (only if viewer is available)

print("GDS file 'parametric_spiral.gds' generated successfully.")