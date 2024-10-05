import gdspy
import math

# Define the library and cell for the GDS layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell('octagon')

# Define the octagon's parameters
edge_length = 10
center = (0, 0)
num_sides = 8

# Calculate the internal angle of a regular octagon
internal_angle = 180 - (360 / num_sides)

# Calculate the radii of the circles that circumscribe and inscribe the octagon
circumscribe_radius = edge_length / (2 * math.sin(math.radians(180 / num_sides)))
inscribe_radius = edge_length / (2 * math.tan(math.radians(180 / num_sides)))

# Create a list to store the points of the octagon
points = []

# Generate the points of the octagon
for i in range(num_sides):
    angle = i * 360 / num_sides
    x = center[0] + circumscribe_radius * math.cos(math.radians(angle))
    y = center[1] + circumscribe_radius * math.sin(math.radians(angle))
    points.append((x, y))

# Create a polygon for the octagon
octagon = gdspy.Polygon(points, layer=0, datatype=0)

# Add the octagon to the cell
cell.add(octagon)

# Save the design to a GDS file
lib.write_gds('octagon.gds')