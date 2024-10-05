import gdspy
import numpy as np

# Create a new GDSII library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('PENTAGON')

# Define the pentagon parameters
edge_length = 10000  # 10 mm in micrometers
num_sides = 5

# Calculate the radius of the circumscribed circle
radius = edge_length / (2 * np.sin(np.pi / num_sides))

# Calculate the coordinates of the pentagon vertices
vertices = []
for i in range(num_sides):
    angle = 2 * np.pi * i / num_sides - np.pi / 2  # Start from the top vertex
    x = radius * np.cos(angle)
    y = radius * np.sin(angle)
    vertices.append((x, y))

# Create the pentagon polygon
pentagon = gdspy.Polygon(vertices)

# Add the pentagon to the cell
cell.add(pentagon)

# Save the design to a GDS file
lib.write_gds('pentagon.gds')

print("Regular pentagon with 10 mm edges centered at (0, 0) has been created and saved as 'pentagon.gds'.")