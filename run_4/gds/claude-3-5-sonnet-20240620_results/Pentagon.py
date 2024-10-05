import gdspy
import numpy as np

# Create a new library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('PENTAGON')

# Pentagon edge length
edge_length = 10  # mm

# Calculate the radius of the circumscribed circle
radius = edge_length / (2 * np.sin(np.pi / 5))

# Calculate vertex coordinates
vertices = []
for i in range(5):
    angle = 2 * np.pi * i / 5 - np.pi / 2  # Start from the top vertex
    x = radius * np.cos(angle)
    y = radius * np.sin(angle)
    vertices.append((x, y))

# Create the pentagon polygon
pentagon = gdspy.Polygon(vertices)

# Calculate the center of the pentagon
center_x = sum(v[0] for v in vertices) / 5
center_y = sum(v[1] for v in vertices) / 5

# Translate the pentagon to center it at (0, 0)
pentagon.translate(-center_x, -center_y)

# Add the pentagon to the cell
cell.add(pentagon)

# Save the design to a GDS file
lib.write_gds('regular_pentagon.gds')

print("Regular pentagon with 10 mm edges centered at (0, 0) has been created and saved as 'regular_pentagon.gds'.")