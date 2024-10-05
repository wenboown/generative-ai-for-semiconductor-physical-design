import gdspy
import numpy as np

# Define the library and cell for the GDS layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell('Circle')

# Define the layer
layer = 0

# Define the radius and center of the circle
radius = 10
center = (0, 0)

# Generate the circle as a polygon
points = []
for theta in np.linspace(0, 2*np.pi, 100):
    x = center[0] + radius * np.cos(theta)
    y = center[1] + radius * np.sin(theta)
    points.append((x, y))

# Create the polygon
poly = gdspy.Polygon(points, layer=layer)

# Add the polygon to the cell
cell.add(poly)

# Save the design to a GDS file
lib.write_gds('circle.gds')