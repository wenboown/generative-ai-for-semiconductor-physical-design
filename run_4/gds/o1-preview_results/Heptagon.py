import gdspy
import math

# Create a new GDSII library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('HEPTAGON')

# Parameters for the heptagon
sides = 7
side_length = 10000  # 10 mm in micrometers since GDSII units are in micrometers

# Calculate the radius of the circumcircle
# side_length = 2 * R * sin(pi / n)
R = side_length / (2 * math.sin(math.pi / sides))

# Generate the vertex coordinates
points = []
for i in range(sides):
    theta = (2 * math.pi / sides) * i
    x = R * math.cos(theta)
    y = R * math.sin(theta)
    points.append((x, y))

# Create the polygon
heptagon = gdspy.Polygon(points)

# Add the polygon to the cell
cell.add(heptagon)

# Save the library in a GDSII file
lib.write_gds('heptagon.gds')