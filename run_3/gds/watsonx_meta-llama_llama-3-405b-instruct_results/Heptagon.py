import gdspy
import math

# User design specifications
num_sides = 7
side_length = 10  # in mm
center = (0, 0)  # in mm

# Define the library and cell for the GDS layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell("heptagon")

# Function to calculate the points of the heptagon
def heptagon_points(num_sides, side_length, center):
    points = []
    for i in range(num_sides):
        angle = 2 * math.pi * i / num_sides
        x = center[0] + side_length * math.cos(angle)
        y = center[1] + side_length * math.sin(angle)
        points.append((x, y))
    return points

# Create the heptagon
points = heptagon_points(num_sides, side_length, center)
poly = gdspy.Polygon(points, layer=1, datatype=0)
cell.add(poly)

# Save the design to a GDS file
lib.write_gds("heptagon.gds")