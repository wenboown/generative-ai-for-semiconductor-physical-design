import gdspy
import numpy as np

# Define the library and cell for the GDS layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell('Circle')

# Define the circle's parameters
radius = 10  # mm
center = (0, 0)  # mm
num_points = 100  # Number of points for the circle's polygon approximation
layer = 0  # Layer number

# Calculate the circle's points
theta = np.linspace(0, 2*np.pi, num_points, endpoint=False)
x = center[0] + radius * np.cos(theta)
y = center[1] + radius * np.sin(theta)

# Create the circle as a polygon
circle = gdspy.Polygon([(xi, yi) for xi, yi in zip(x, y)], layer=layer)

# Add the circle to the cell
cell.add(circle)

# Save the design to a GDS file
lib.write_gds('circle.gds')