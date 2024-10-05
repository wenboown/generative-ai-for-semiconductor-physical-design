import gdspy
import math

# Define the library and cell for the GDS layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell('triangle')

# Define the triangle parameters
edge_length = 10  # mm
center = (0, 0)  # coordinates of the center

# Calculate the apex coordinates of the equilateral triangle
height = edge_length * math.sqrt(3) / 2
apex1 = (center[0] - edge_length / 2, center[1] - height / 3)
apex2 = (center[0] + edge_length / 2, center[1] - height / 3)
apex3 = (center[0], center[1] + 2 * height / 3)

# Create the triangle polygon with precise coordinates
triangle = gdspy.Polygon([apex1, apex2, apex3], layer=1)

# Add the triangle to the cell
cell.add(triangle)

# Save the design to a GDS file
lib.write_gds('triangle.gds')