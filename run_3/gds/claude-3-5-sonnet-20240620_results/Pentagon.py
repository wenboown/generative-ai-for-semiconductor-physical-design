import gdspy
import numpy as np

# Create a new library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('PENTAGON')

# Calculate the coordinates of the pentagon vertices
edge_length = 10000  # 10 mm in nanometers
angle = 2 * np.pi / 5  # Internal angle of the pentagon in radians

vertices = []
for i in range(5):
    x = edge_length / (2 * np.sin(angle/2)) * np.cos(i * angle - np.pi/2)
    y = edge_length / (2 * np.sin(angle/2)) * np.sin(i * angle - np.pi/2)
    vertices.append((x, y))

# Create the pentagon polygon
pentagon = gdspy.Polygon(vertices)

# Add the pentagon to the cell
cell.add(pentagon)

# Save the design to a GDS file
lib.write_gds('pentagon.gds')

print("Pentagon GDS file has been generated.")