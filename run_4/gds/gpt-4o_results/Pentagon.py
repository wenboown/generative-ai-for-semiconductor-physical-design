import gdspy
import math

# Create a new library and cell for the design
lib = gdspy.GdsLibrary()
cell = lib.new_cell('PENTAGON')

# Constants for the regular pentagon
num_sides = 5
side_length = 10  # in mm
radius = side_length / (2 * math.sin(math.pi / num_sides))

# Calculate the vertices of the pentagon
vertices = []
for i in range(num_sides):
    angle = 2 * math.pi * i / num_sides
    x = radius * math.cos(angle)
    y = radius * math.sin(angle)
    vertices.append((x, y))

# Create the pentagon as a polygon
pentagon = gdspy.Polygon(vertices)

# Add the pentagon to the cell
cell.add(pentagon)

# Save the layout to a GDS file
lib.write_gds('pentagon.gds')

print("GDS file with a regular pentagon has been created.")