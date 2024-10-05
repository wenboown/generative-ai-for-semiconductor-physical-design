import gdspy
import math

# Create a new GDSII library
lib = gdspy.GdsLibrary()

# Create a new cell in the library
cell = lib.new_cell('OCTAGON')

# Design parameters
side_length_mm = 10.0  # Side length in millimeters
num_sides = 8          # Number of sides for an octagon

# Convert millimeters to micrometers (GDSII units)
side_length = side_length_mm * 1000.0  # Convert to micrometers

# Calculate the radius to the vertices
radius = side_length / (2 * math.sin(math.pi / num_sides))

# Calculate the coordinates of the vertices
vertices = []
for k in range(num_sides):
    theta = (math.pi / num_sides) + k * (2 * math.pi / num_sides)
    x = radius * math.cos(theta)
    y = radius * math.sin(theta)
    vertices.append((x, y))

# Create the octagon polygon
octagon = gdspy.Polygon(vertices)

# Add the polygon to the cell
cell.add(octagon)

# Save the layout to a GDSII file
lib.write_gds('octagon.gds')