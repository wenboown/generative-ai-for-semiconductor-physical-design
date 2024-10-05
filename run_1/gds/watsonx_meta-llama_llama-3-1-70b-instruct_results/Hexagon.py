import gdspy
import math

# Define the library and cell for the GDS layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell('regular_hexagon')

# Calculate the coordinates for a regular hexagon with each edge of 10 mm
center_x, center_y = 0, 0
edge_length = 10
points = []
for i in range(6):
    angle = math.pi / 3 * i
    x = center_x + edge_length * math.cos(angle)
    y = center_y + edge_length * math.sin(angle)
    points.append((x, y))

# Create a polygon for the regular hexagon
hexagon = gdspy.Polygon(points, layer=1)

# Add the hexagon to the cell
cell.add(hexagon)

# Save the design to a GDS file
lib.write_gds('regular_hexagon.gds')