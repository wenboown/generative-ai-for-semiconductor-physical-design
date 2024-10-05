import gdspy
import math

# Define the octagon parameters
edge_length = 10  # mm
center_x, center_y = 0, 0  # center at (0,0)

# Calculate the coordinates of the octagon vertices
angle_step = 2 * math.pi / 8  # Octagon has 8 sides
radius = edge_length / (2 * math.sin(math.pi / 8))  # Calculate the circumscribed circle radius

vertices = []
for i in range(8):
    angle = i * angle_step
    x = center_x + radius * math.cos(angle)
    y = center_y + radius * math.sin(angle)
    vertices.append((x, y))

# Create a GDSII library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('OCTAGON')

# Create the octagon polygon
octagon = gdspy.Polygon(vertices)

# Add the octagon to the cell
cell.add(octagon)

# Save the layout to a GDS file
lib.write_gds('octagon.gds')

print("Octagon GDS file 'octagon.gds' has been created successfully.")