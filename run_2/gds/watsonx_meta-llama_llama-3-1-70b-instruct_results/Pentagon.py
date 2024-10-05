import gdspy
import math

# Define the library and cell for the GDS layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell("Pentagon")

# Calculate the coordinates of the pentagon vertices
n_sides = 5
side_length = 10
angle = 2 * math.pi / n_sides
vertices = []
for i in range(n_sides):
    x = side_length * math.cos(i * angle)
    y = side_length * math.sin(i * angle)
    vertices.append((x, y))

# Create the polygon
pentagon = gdspy.Polygon(vertices)

# Add the polygon to the cell
cell.add(pentagon)

# Save the design to a GDS file
lib.write_gds("pentagon.gds")