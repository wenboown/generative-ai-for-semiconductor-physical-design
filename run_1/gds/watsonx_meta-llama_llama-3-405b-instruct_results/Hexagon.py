import gdspy
import math

# Define the library and cell for the GDS layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell('hexagon')

# Define the parameters for the hexagon
edge_length = 10  # mm
center = (0, 0)

# Calculate the coordinates for the hexagon
points = []
for i in range(6):
    angle = i * math.pi / 3
    x = center[0] + edge_length * math.cos(angle)
    y = center[1] + edge_length * math.sin(angle)
    points.append((x, y))

# Create the hexagon polygon
polygon = gdspy.Polygon(points, layer=0, datatype=0)

# Add the polygon to the cell
cell.add(polygon)

# Save the design to a GDS file
lib.write_gds('hexagon.gds')