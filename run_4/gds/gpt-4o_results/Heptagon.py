import gdspy
import math

# Define the name of the GDSII file
gdsii_file = "heptagon.gds"

# Create a library
lib = gdspy.GdsLibrary()

# Create a cell
cell = lib.new_cell("HEPTAGON_CELL")

# Define the heptagon
num_sides = 7
side_length = 10  # mm
radius = side_length / (2 * math.sin(math.pi / num_sides))

# Calculate the vertices of the heptagon
vertices = []
for i in range(num_sides):
    angle = 2 * math.pi * i / num_sides
    x = radius * math.cos(angle)
    y = radius * math.sin(angle)
    vertices.append((x, y))

# Create the polygon
heptagon = gdspy.Polygon(vertices)

# Add the polygon to the cell
cell.add(heptagon)

# Write the GDSII file
lib.write_gds(gdsii_file)

print(f"GDSII file '{gdsii_file}' successfully created.")