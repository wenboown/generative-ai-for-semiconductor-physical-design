import gdspy
import math

# Define the library and cell for the GDS layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell('hexagon')

# Define the edge length of the hexagon
edge_length = 10

# Calculate the internal angles of the hexagon
internal_angle = 120

# Calculate the points of the hexagon
points = []
for i in range(6):
    angle = i * internal_angle
    x = edge_length * math.cos(math.radians(angle))
    y = edge_length * math.sin(math.radians(angle))
    points.append((x, y))

# Create the hexagon polygon
hexagon = gdspy.Polygon(points)

# Add the hexagon to the cell
cell.add(hexagon)

# Save the design to a GDS file
lib.write_gds('hexagon.gds')