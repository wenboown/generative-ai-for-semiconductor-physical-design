import gdspy
import math

# Define the side length of the octagon
side_length = 10

# Calculate the radius of the circumscribed circle
radius = side_length / (2 * math.sin(math.pi / 8))

# Define the points of the octagon
points = []
for i in range(8):
    angle = 2 * math.pi * i / 8
    x = radius * math.cos(angle)
    y = radius * math.sin(angle)
    points.append((x, y))

# Create a new GDSII library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('OCTAGON')

# Add the octagon to the cell
octagon = gdspy.Polygon(points)
cell.add(octagon)

# Save the library in a file
lib.write_gds('octagon.gds')

print("Octagon GDS file generated successfully.")