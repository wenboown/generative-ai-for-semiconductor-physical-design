import gdspy
import math

# Create a new GDSII library
lib = gdspy.GdsLibrary()

# Create a cell for the heptagon
cell = lib.new_cell('HEPTAGON_CELL')

# Number of sides for a heptagon
num_sides = 7

# Edge length in millimeters
edge_length_mm = 10.0

# Convert edge length to micrometers (since GDSII works with micrometers)
edge_length = edge_length_mm * 1000.0  # in micrometers

# Calculate the radius of the circumscribed circle
theta = math.pi / num_sides
radius = edge_length / (2 * math.sin(theta))

# Generate the vertices of the heptagon
vertices = []
for i in range(num_sides):
    angle = (2 * math.pi * i) / num_sides
    x = radius * math.cos(angle)
    y = radius * math.sin(angle)
    vertices.append((x, y))

# Create the heptagon polygon
heptagon = gdspy.Polygon(vertices)

# Add the heptagon to the cell
cell.add(heptagon)

# Save the GDSII file
lib.write_gds('heptagon.gds')