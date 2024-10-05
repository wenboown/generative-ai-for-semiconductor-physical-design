import gdspy
import math

# Define side length in micrometers (10 mm)
s = 10000 * 1000  # Convert mm to um

# Compute the radius to the vertices
sin_pi_over_8 = math.sin(math.pi / 8)
r = s / (2 * sin_pi_over_8)

# Generate the coordinates of the octagon vertices
vertices = []
for i in range(8):
    theta = math.pi / 8 + i * math.pi / 4
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    vertices.append((x, y))

# Create a GDSII library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('OCTAGON')

# Create the polygon
octagon = gdspy.Polygon(vertices)

# Add the polygon to the cell
cell.add(octagon)

# Save the cell in a GDSII file
lib.write_gds('octagon.gds')