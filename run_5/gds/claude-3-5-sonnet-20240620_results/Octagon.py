import gdspy
import numpy as np

# Create a new library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('OCTAGON')

# Octagon parameters
side_length = 10000  # 10 mm in nanometers
angle = np.pi / 4  # 45 degrees in radians

# Calculate the radius of the circumscribed circle
radius = side_length / (2 * np.sin(np.pi / 8))

# Generate vertex coordinates
vertices = []
for i in range(8):
    x = radius * np.cos(i * angle)
    y = radius * np.sin(i * angle)
    vertices.append((x, y))

# Create the octagon polygon
octagon = gdspy.Polygon(vertices)

# Add the octagon to the cell
cell.add(octagon)

# Save the design to a GDS file
lib.write_gds('octagon.gds')

print("Octagon GDS file has been generated successfully.")