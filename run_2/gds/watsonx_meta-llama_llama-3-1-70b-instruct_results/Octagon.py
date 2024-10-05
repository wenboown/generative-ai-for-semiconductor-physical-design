import gdspy
import math

# Define the library and cell for the GDS layout
lib = gdspy.GdsLibrary()  # Create a new library
cell = lib.new_cell("octagon")  # Create a new cell in the library

# Define the octagon parameters
edge_length = 10
num_edges = 8
center_x, center_y = 0, 0

# Calculate the coordinates of the octagon
angle_step = 2 * math.pi / num_edges
points = []
for i in range(num_edges):
    angle = i * angle_step
    x = center_x + edge_length / 2 * math.cos(angle)
    y = center_y + edge_length / 2 * math.sin(angle)
    points.append((x, y))

# Create the octagon polygon
octagon = gdspy.Polygon(points)

# Add the octagon to the cell
cell.add(octagon)

# Save the design to a GDS file
lib.write_gds("octagon.gds")