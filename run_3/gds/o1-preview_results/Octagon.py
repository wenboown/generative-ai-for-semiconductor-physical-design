import gdspy
import numpy as np

# Define the side length in micrometers (1 mm = 1000 micrometers)
side_length = 10000  # 10 mm = 10,000 micrometers

# Calculate the radius (distance from the center to each vertex)
# For a regular octagon: R = side_length / (2 * sin(pi / 8))
radius = side_length / (2 * np.sin(np.pi / 8))

# Compute the vertices of the octagon
vertices = []
for k in range(8):
    angle = (2 * k + 1) * np.pi / 8  # Angles in radians
    x = radius * np.cos(angle)  # X-coordinate
    y = radius * np.sin(angle)  # Y-coordinate
    vertices.append((x, y))

# Create a new GDSII library and cell
gdsii_lib = gdspy.GdsLibrary()
cell = gdsii_lib.new_cell('OCTAGON')

# Create the octagon polygon
octagon = gdspy.Polygon(vertices)

# Add the octagon to the cell
cell.add(octagon)

# Save the GDSII file
gdsii_lib.write_gds('octagon.gds')