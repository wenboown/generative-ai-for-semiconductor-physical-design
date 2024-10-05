import gdspy
import math

# Create a new GDSII library with units in millimeters
lib = gdspy.GdsLibrary(unit=1e-3, precision=1e-6)

# Create a new cell where the geometry will be placed
cell = lib.new_cell('HEXAGON')

# Edge length of the hexagon in millimeters
edge_length = 10.0

# Calculate the coordinates of the hexagon vertices
coords = []
for i in range(6):
    angle_deg = 60 * i
    angle_rad = math.radians(angle_deg)
    x = edge_length * math.cos(angle_rad)
    y = edge_length * math.sin(angle_rad)
    coords.append((x, y))

# Create the hexagon polygon
hexagon = gdspy.Polygon(coords)

# Add the hexagon to the cell
cell.add(hexagon)

# Write the library to a GDSII file
lib.write_gds('hexagon.gds')