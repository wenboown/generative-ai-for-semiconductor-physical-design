import gdspy
import math

# Create a new GDSII library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('HEXAGON_CELL')

# Define the side length of the hexagon
side_length = 10

# Calculate the vertices of the hexagon
vertices = []
for i in range(6):
    angle_deg = 60 * i + 30
    angle_rad = math.pi / 180 * angle_deg
    x = side_length * math.cos(angle_rad)
    y = side_length * math.sin(angle_rad)
    vertices.append((x, y))

# Create the hexagon as a polygon
hexagon = gdspy.Polygon(vertices)

# Add the hexagon to the cell
cell.add(hexagon)

# Save the design to a GDS file
lib.write_gds('hexagon.gds')

print("Hexagon GDS file created successfully.")