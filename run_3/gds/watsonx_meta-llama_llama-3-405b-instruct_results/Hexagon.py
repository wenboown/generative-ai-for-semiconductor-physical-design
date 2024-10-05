import gdspy
import math

# Define the library and cell for the GDS layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell('hexagon')

# Define the parameters of the hexagon
edge_length = 10  # mm
center = (0, 0)

# Calculate the vertices of the hexagon
vertices = []
for i in range(6):
    angle = i * math.pi / 3  # 60 degrees in radians
    x = center[0] + edge_length * math.cos(angle)
    y = center[1] + edge_length * math.sin(angle)
    vertices.append((x, y))

# Create the hexagon as a polygon
hexagon = gdspy.Polygon(vertices)

# Add the hexagon to the cell
cell.add(hexagon)

# Save the design to a GDS file
lib.write_gds('hexagon.gds')