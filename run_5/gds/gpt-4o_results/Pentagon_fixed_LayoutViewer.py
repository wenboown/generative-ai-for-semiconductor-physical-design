import gdspy
import math

# Create a new GDSII library named 'pentagon.gds'
lib = gdspy.GdsLibrary()

# Create a new cell named 'POLYGONS'
cell = lib.new_cell('PENTAGON')

# Define the number of sides and the radius for the regular pentagon
sides = 5
edge_length = 10000  # Since GDS uses nanometers, 10 mm = 10000 µm
radius = edge_length / (2 * math.sin(math.pi / sides))

# Calculate the vertices of the regular pentagon
vertices = []
for i in range(sides):
    angle = 2 * math.pi * i / sides
    x = radius * math.cos(angle)
    y = radius * math.sin(angle)
    vertices.append((x, y))

# Create the polygon representing the pentagon
pentagon = gdspy.Polygon(vertices)

# Add the polygon to the cell
cell.add(pentagon)

# Write the GDSII file
lib.write_gds('pentagon.gds')

# Optionally, display the layout using gdspy internal viewer