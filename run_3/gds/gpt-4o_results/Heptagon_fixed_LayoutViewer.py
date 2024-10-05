import gdspy
import math

# Define the heptagon specifics
center_x, center_y = 0, 0
number_of_sides = 7
side_length = 10e3  # 10 mm in microns
radius = side_length / (2 * math.sin(math.pi / number_of_sides))  # Calculate radius of the heptagon

# Create a GDSII library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('HEPTAGON_CELL')

# Define the heptagon vertices
vertices = []
angle_step = 2 * math.pi / number_of_sides
for i in range(number_of_sides):
    angle = i * angle_step
    x = center_x + radius * math.cos(angle)
    y = center_y + radius * math.sin(angle)
    vertices.append((x, y))

# Create the heptagon
heptagon = gdspy.Polygon(vertices)

# Add the heptagon to the cell
cell.add(heptagon)

# Save the layout to a GDS file
lib.write_gds('heptagon_layout.gds')

# View layout using internal viewer (optional, only if viewer is supported in your environment)