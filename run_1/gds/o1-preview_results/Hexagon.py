import gdspy
import math

# Create a new GDSII library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('HEXAGON')

# Side length of the hexagon (in micrometers)
s = 10000  # 10 mm = 10,000 μm

# Radius of the hexagon from center to vertex
R = s  # For a regular hexagon, R = side length

# Calculate the vertices of the hexagon
vertices = []
for i in range(6):
    angle = math.pi / 3 * i  # 0 to 2π in steps of π/3
    x = R * math.cos(angle)
    y = R * math.sin(angle)
    vertices.append((x, y))

# Create the polygon and add it to the cell
hexagon = gdspy.Polygon(vertices)
cell.add(hexagon)

# Write the GDSII file
lib.write_gds('hexagon.gds')