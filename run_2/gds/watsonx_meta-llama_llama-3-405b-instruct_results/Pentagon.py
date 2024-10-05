import gdspy
import math

# Define the library and cell for the GDS layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell('regular_pentagon')

# Define the edge length and center coordinates
edge_length = 10
center_x, center_y = 0, 0

# Calculate the angle between edges (in radians)
angle = 2 * math.pi / 5

# Calculate the coordinates for each vertex
vertices = []
for i in range(5):
    x = center_x + edge_length * math.cos(i * angle)
    y = center_y + edge_length * math.sin(i * angle)
    vertices.append((x, y))

# Create a polygon for the regular pentagon
poly = gdspy.Polygon(vertices, layer=1, datatype=0)

# Add the polygon to the cell
cell.add(poly)

# Save the design to a GDS file
lib.write_gds('regular_pentagon.gds')