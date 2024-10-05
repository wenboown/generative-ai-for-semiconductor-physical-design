import numpy as np
import gdspy

# Define the edge length and center of the pentagon
edge_length = 10
center_x, center_y = 0, 0

# Calculate the coordinates of the pentagon vertices
angle = 2 * np.pi / 5
vertices = []
for i in range(5):
    x = center_x + edge_length * np.cos(i * angle)
    y = center_y + edge_length * np.sin(i * angle)
    vertices.append((x, y))

# Create the GDS library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('pentagon')

# Create the pentagon polygon
pentagon = gdspy.Polygon(vertices, 1)

# Add the pentagon to the cell
cell.add(pentagon)

# Save the design to a GDS file
lib.write_gds('pentagon.gds')