import gdspy
import math

# Create a new GDSII library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('PENTAGON_CELL')

# Design parameters
side_length = 10.0  # in mm
num_sides = 5
center = (0, 0)

# Calculate the radius of the circumscribed circle
sin_pi_n = math.sin(math.pi / num_sides)
radius = side_length / (2 * sin_pi_n)

# Starting angle to position one vertex at the top
theta0 = math.pi / 2

# Calculate the coordinates of the pentagon vertices
vertices = []
for k in range(num_sides):
    theta = theta0 + 2 * math.pi * k / num_sides
    x = center[0] + radius * math.cos(theta)
    y = center[1] + radius * math.sin(theta)
    vertices.append((x, y))

# Create the pentagon polygon
pentagon = gdspy.Polygon(vertices)

# Add the polygon to the cell
cell.add(pentagon)

# Save the layout to a GDS file
lib.write_gds('pentagon.gds')