import gdspy
import math

# Specifications
center = (0, 0)
edge_length = 10  # in mm

# Calculate the vertices of the hexagon
vertices = []
for i in range(6):
    angle = math.pi / 3 * i  # 60 degrees in radians
    x = center[0] + edge_length * math.cos(angle)
    y = center[1] + edge_length * math.sin(angle)
    vertices.append((x, y))

# Create a new GDSII library and cell
gdsii_lib = gdspy.GdsLibrary()
cell = gdsii_lib.new_cell('HEXAGON_CELL')

# Create a polygon using the vertices and add it to the cell
hexagon = gdspy.Polygon(vertices)
cell.add(hexagon)

# Save the GDSII file
gdsii_lib.write_gds('hexagon.gds')

print("GDSII file 'hexagon.gds' has been created.")