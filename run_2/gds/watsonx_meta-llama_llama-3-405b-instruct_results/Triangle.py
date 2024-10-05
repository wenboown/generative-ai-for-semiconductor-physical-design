import gdspy
import math

# Define the library and cell for the GDS layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell('triangle')

# Define the center coordinates
center_x, center_y = 0, 0

# Calculate the vertex coordinates for an equilateral triangle with edge length 10 mm
edge_length = 10
angle = math.radians(60)  # internal angle of an equilateral triangle
vertex1_x = center_x
vertex1_y = center_y + edge_length / math.sqrt(3)
vertex2_x = center_x - edge_length / 2
vertex2_y = center_y - edge_length * math.sqrt(3) / 6
vertex3_x = center_x + edge_length / 2
vertex3_y = center_y - edge_length * math.sqrt(3) / 6

# Create the triangle polygon
triangle = gdspy.Polygon([(vertex1_x, vertex1_y), (vertex2_x, vertex2_y), (vertex3_x, vertex3_y)])

# Add the triangle to the cell
cell.add(triangle)

# Save the design to a GDS file
lib.write_gds('triangle.gds')