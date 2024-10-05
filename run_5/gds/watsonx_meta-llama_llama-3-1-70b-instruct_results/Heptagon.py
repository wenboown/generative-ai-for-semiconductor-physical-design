import gdspy
import math

# Parse the user's design specifications
edge_length = 10
num_sides = 7

# Define the library and cell for the GDS layout
lib = gdspy.Library()
cell = lib.new_cell('heptagon')

# Calculate the coordinates of the heptagon
angle_step = 2 * math.pi / num_sides
points = []
for i in range(num_sides):
    angle = i * angle_step
    x = edge_length / 2 * math.cos(angle)
    y = edge_length / 2 * math.sin(angle)
    points.append((x, y))

# Create a polygon for the heptagon
heptagon = gdspy.Polygon(points)

# Add the heptagon to the cell
cell.add(heptagon)

# Save the design to a GDS file
lib.write_gds('heptagon.gds')