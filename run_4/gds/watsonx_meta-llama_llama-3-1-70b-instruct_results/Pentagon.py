import gdspy
import math

# Define the library and cell for the GDS layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell("Pentagon")

# Define the parameters
edge_length = 10  # in mm
center_x, center_y = 0, 0

# Calculate the coordinates of the vertices
angle = 2 * math.pi / 5  # internal angle of a pentagon
vertices = []
for i in range(5):
    angle_i = i * angle
    x = center_x + edge_length / 2 * math.cos(angle_i)
    y = center_y + edge_length / 2 * math.sin(angle_i)
    vertices.append((x, y))

# Create the polygon
pentagon = gdspy.Polygon(vertices, layer=1)

# Add the polygon to the cell
cell.add(pentagon)

# Save the design to a GDS file
lib.write_gds("pentagon.gds")