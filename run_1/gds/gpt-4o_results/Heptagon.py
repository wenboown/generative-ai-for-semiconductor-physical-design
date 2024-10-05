import gdspy
import math

# Constants
num_sides = 7
side_length = 10 * 1e3  # Convert mm to microns
center = (0, 0)
angle_step = 2 * math.pi / num_sides

# Calculate coordinates of vertices
vertices = []
for i in range(num_sides):
    angle = i * angle_step
    x = center[0] + side_length * math.cos(angle)
    y = center[1] + side_length * math.sin(angle)
    vertices.append((x, y))

# Define the GDSII layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell('HEPTAGON')

# Create the polygon (heptagon) and add to the cell
heptagon = gdspy.Polygon(vertices)
cell.add(heptagon)

# Save the layout to a GDS file
lib.write_gds('heptagon.gds')

print("GDS file 'heptagon.gds' has been generated successfully.")