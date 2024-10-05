import gdspy
import math

# Create a new GDSII library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('PENTAGON')

# Define the edge length and center coordinates
edge_length = 10  # in mm
center_x, center_y = 0, 0

# Calculate the radius of the circumscribed circle
radius = edge_length / (2 * math.sin(math.pi / 5))

# Calculate the vertices of the regular pentagon
num_sides = 5
vertices = []
for i in range(num_sides):
    angle = 2 * math.pi * i / num_sides
    x = center_x + radius * math.cos(angle)
    y = center_y + radius * math.sin(angle)
    # Convert coordinates from mm to micrometers
    vertices.append((x * 1000, y * 1000))

# Create the polygon
pentagon = gdspy.Polygon(vertices)

# Add the polygon to the cell
cell.add(pentagon)

# Save the design to a GDS file
lib.write_gds('pentagon.gds')