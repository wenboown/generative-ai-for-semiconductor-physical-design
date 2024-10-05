import gdspy
import math

# Helper function to calculate the vertices of a regular hexagon
def hexagon_points(center, edge_length):
    cx, cy = center
    points = []
    for i in range(6):
        angle = math.pi / 3 * i  # 60 degrees in radians
        x = cx + edge_length * math.cos(angle)
        y = cy + edge_length * math.sin(angle)
        points.append((x, y))
    return points

# Create a new GDSII library
lib = gdspy.GdsLibrary()

# Create a cell in the library
cell = lib.new_cell('HEXAGON')

# Center of the hexagon
center = (0, 0)
edge_length = 10  # mm

# Calculate the coordinates of the hexagon vertices
points = hexagon_points(center, edge_length)

# Create the polygon representing the hexagon
hexagon = gdspy.Polygon(points)

# Add the hexagon to the cell
cell.add(hexagon)

# Save the library in a GDSII file
lib.write_gds('hexagon.gds')

print("Hexagon GDS file 'hexagon.gds' created successfully.")