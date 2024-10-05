import gdspy
import math

# Create a GDSII library with units in millimeters
lib = gdspy.GdsLibrary(unit=1e-3, precision=1e-6)

# Create a cell to contain the hexagon
cell = lib.new_cell('HEXAGON')

# Define the side length of the hexagon in millimeters
side_length = 10.0  # Edge length in mm

# Calculate the radius of the circumcircle (distance from center to a vertex)
radius = side_length

# Calculate the vertices of the hexagon
vertices = []
for i in range(6):
    angle = i * (math.pi / 3)  # 60-degree increments in radians
    x = radius * math.cos(angle)
    y = radius * math.sin(angle)
    vertices.append((x, y))

# Create the hexagon polygon
hexagon = gdspy.Polygon(vertices)

# Add the hexagon to the cell
cell.add(hexagon)

# Write the GDSII file
lib.write_gds('hexagon.gds')