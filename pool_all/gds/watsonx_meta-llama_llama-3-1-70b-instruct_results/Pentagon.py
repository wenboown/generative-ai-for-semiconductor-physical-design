import gdspy
import math

# Create a new GDSII library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('PENTAGON')

# Define the edge length and center coordinates
edge_length = 10000  # 10 mm in micrometers
center_x, center_y = 0, 0

# Calculate the radius of the circumscribed circle
radius = edge_length / (2 * math.sin(math.pi / 5))

# Calculate the vertices of the regular pentagon
vertices = []
for i in range(5):
    angle = 2 * math.pi * i / 5
    x = center_x + radius * math.cos(angle)
    y = center_y + radius * math.sin(angle)
    vertices.append((x, y))

# Create the polygon representing the pentagon
pentagon = gdspy.Polygon(vertices, layer=1)

# Add the polygon to the cell
cell.add(pentagon)

# Save the design to a GDS file
lib.write_gds('pentagon.gds')

print("Regular pentagon with each edge 10 mm has been generated.")