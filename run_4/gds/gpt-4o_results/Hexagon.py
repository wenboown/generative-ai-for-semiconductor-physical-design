import gdspy
import math

# Function to create a regular hexagon
def create_regular_hexagon(center, edge_length):
    cx, cy = center
    points = []
    for i in range(6):
        angle = math.radians(60 * i)
        x = cx + edge_length * math.cos(angle)
        y = cy + edge_length * math.sin(angle)
        points.append((x, y))
    return points

# Specifications
center = (0, 0)
edge_length = 10  # in mm

# Create the hexagon points
hexagon_points = create_regular_hexagon(center, edge_length)

# Create a new GDSII library and add a cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('HEXAGON_CELL')

# Create a polygon and add it to the cell
hexagon = gdspy.Polygon(hexagon_points)
cell.add(hexagon)

# Define the layout file name
gds_file = 'hexagon.gds'

# Write the GDS file
lib.write_gds(gds_file)

print(f"GDS file '{gds_file}' created with a regular hexagon.")