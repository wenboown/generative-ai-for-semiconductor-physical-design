import gdspy
import math

# Define the library and cell for the GDS layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell('triangle')

# Define the triangle's edge length and center
edge_length = 10  # mm
center_x, center_y = 0, 0  # mm

# Calculate the triangle's vertices
vertex1_x = center_x + edge_length / 2  # mm
vertex1_y = center_y - edge_length * math.sqrt(3) / 6  # mm
vertex2_x = center_x - edge_length / 2  # mm
vertex2_y = center_y - edge_length * math.sqrt(3) / 6  # mm
vertex3_x = center_x  # mm
vertex3_y = center_y + edge_length * math.sqrt(3) / 3  # mm

# Create the triangle as a polygon with precise coordinates
triangle = gdspy.Polygon([(vertex1_x, vertex1_y), (vertex2_x, vertex2_y), (vertex3_x, vertex3_y)])

# Add the triangle to the cell
cell.add(triangle)

# Save the design to a GDS file
lib.write_gds('triangle.gds')