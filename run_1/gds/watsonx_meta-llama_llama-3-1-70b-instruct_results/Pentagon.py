import gdspy
import numpy as np

# Define the library and cell for the GDS layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell('regular_pentagon')

# Define the edge length and center coordinates
edge_length = 10
center_x, center_y = 0, 0

# Calculate the coordinates of the pentagon's vertices
angle = 2 * np.pi / 5
vertices = []
for i in range(5):
    vertex_x = center_x + edge_length / (2 * np.tan(angle/2)) * np.cos(i * angle)
    vertex_y = center_x + edge_length / (2 * np.tan(angle/2)) * np.sin(i * angle)
    vertices.append((vertex_x, vertex_y))

# Create the polygon with the calculated vertices
polygon = gdspy.Polygon(vertices)

# Add the polygon to the cell
cell.add(polygon)

# Save the design to a GDS file
lib.write_gds('pentagon.gds')