import gdspy
import math

# Initialize the GDSII library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('HEPTAGON')

# Heptagon parameters
num_sides = 7
radius = 10 / (2 * math.sin(math.pi / num_sides))  # Calculate the radius

# Generate heptagon points
vertices = []
for i in range(num_sides):
    angle = 2 * math.pi * i / num_sides
    x = radius * math.cos(angle)
    y = radius * math.sin(angle)
    vertices.append((x, y))

# Create a polygon with the calculated vertices
polygon = gdspy.Polygon(vertices)

# Add the polygon to the cell
cell.add(polygon)

# Save the library in a GDSII file
lib.write_gds('heptagon.gds')

print("Heptagon GDS file has been created: heptagon.gds")