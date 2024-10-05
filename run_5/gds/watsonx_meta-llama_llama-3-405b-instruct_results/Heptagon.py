import gdspy
import math

# Define the library and cell for the GDS layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell('heptagon')

# Calculate the coordinates for the heptagon
num_sides = 7
edge_length = 10
center_x, center_y = 0, 0
angle_step = 2 * math.pi / num_sides
vertices = []
for i in range(num_sides):
    angle = i * angle_step
    x = center_x + edge_length * math.cos(angle)
    y = center_y + edge_length * math.sin(angle)
    vertices.append((x, y))

# Create the heptagon as a polygon
heptagon = gdspy.Polygon(vertices)

# Add the heptagon to the cell
cell.add(heptagon)

# Save the design to a GDS file
lib.write_gds('heptagon.gds')