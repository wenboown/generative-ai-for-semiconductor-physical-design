import gdspy
import math

# Define the library and cell for the GDS layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell('Octagon')

# Define the parameters for the octagon
edge_length = 10  # mm
center_x, center_y = 0, 0  # mm

# Calculate the points for the octagon
points = []
for i in range(8):
    angle = i * math.pi / 4  # 45 degrees in radians
    x = center_x + edge_length / 2 * math.cos(angle)
    y = center_y + edge_length / 2 * math.sin(angle)
    points.append((x, y))

# Create the octagon shape
octagon = gdspy.Polygon(points, layer=1, datatype=0)

# Add the octagon to the cell
cell.add(octagon)

# Save the design to a GDS file
lib.write_gds('octagon.gds')