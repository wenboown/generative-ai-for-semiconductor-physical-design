import gdspy
import math

# Define the edge length of the hexagon
edge_length = 10.0  # in mm

# Calculate the radius of the circumscribed circle
radius = edge_length

# Calculate the vertices of the hexagon
vertices = []
for i in range(6):
    angle = math.pi / 3 * i
    x = radius * math.cos(angle)
    y = radius * math.sin(angle)
    vertices.append((x, y))

# Create a new GDSII library and cell
gdsii_lib = gdspy.GdsLibrary()
cell = gdsii_lib.new_cell('HEXAGON_CELL')

# Create a polygon using the vertices and add it to the cell
hexagon = gdspy.Polygon(vertices)
cell.add(hexagon)

# Save the GDSII file
gdsii_lib.write_gds('regular_hexagon.gds')

print("GDSII file 'regular_hexagon.gds' has been created.")