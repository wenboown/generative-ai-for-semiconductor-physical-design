import gdspy

# Create a new GDSII library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('HEXAGON')

# Define the edge length of the hexagon
edge_length = 10.0  # in mm

# Calculate the vertices of the hexagon
vertices = []
for i in range(6):
    angle = math.pi / 3 * i
    x = edge_length * math.cos(angle)
    y = edge_length * math.sin(angle)
    vertices.append((x, y))

# Create a polygon using the vertices and add it to the cell
hexagon = gdspy.Polygon(vertices)
cell.add(hexagon)

# Save the GDSII file
lib.write_gds('regular_hexagon.gds')

print("GDSII file 'regular_hexagon.gds' has been created.")