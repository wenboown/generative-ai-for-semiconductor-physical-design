import gdspy
import math

# Define the library and cell for the GDS layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell('pentagon')

# Define the edge length of the pentagon
edge_length = 10

# Calculate the coordinates of the pentagon's vertices
angle = 2 * math.pi / 5
points = []
for i in range(5):
    x = edge_length * math.cos(i * angle)
    y = edge_length * math.sin(i * angle)
    points.append((x, y))

# Create the pentagon as a polygon with precise coordinates
pentagon = gdspy.Polygon(points, layer=1, datatype=0)

# Add the pentagon to the cell
cell.add(pentagon)

# Save the design to a GDS file
lib.write_gds('pentagon.gds')