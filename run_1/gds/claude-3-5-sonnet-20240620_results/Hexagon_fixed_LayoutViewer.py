import gdspy
import numpy as np

# Calculate the coordinates of the hexagon vertices
side_length = 10000  # 10 mm in nanometers
angle = np.pi / 3  # 60 degrees in radians
radius = side_length / np.sqrt(3)

vertices = []
for i in range(6):
    x = radius * np.cos(i * angle)
    y = radius * np.sin(i * angle)
    vertices.append((x, y))

# Create a gdspy library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('HEXAGON')

# Create the hexagon polygon
hexagon = gdspy.Polygon(vertices, layer=0)
cell.add(hexagon)

# Save the design to a GDS file
lib.write_gds('hexagon.gds')

# Optional: View the layout