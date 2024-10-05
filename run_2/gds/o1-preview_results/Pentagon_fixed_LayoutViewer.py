import gdspy
import math

# Create a new GDSII library
lib = gdspy.GdsLibrary()

# Create a cell where the shapes will be added
cell = lib.new_cell('PENTAGON')

# Side length of the pentagon in mm
s = 10.0

# Compute the circumradius R of the pentagon
R = s / (2 * math.sin(math.pi / 5))

# Center of the pentagon
center_x = 0
center_y = 0

# Compute the coordinates of the pentagon vertices
vertices = []
for i in range(5):
    theta = 2 * math.pi * i / 5  # angle for each vertex
    x = center_x + R * math.cos(theta)
    y = center_y + R * math.sin(theta)
    vertices.append((x, y))

# Create the pentagon polygon
pentagon = gdspy.Polygon(vertices)

# Add the pentagon to the cell
cell.add(pentagon)

# Save the library in a GDSII file
lib.write_gds('pentagon.gds')

# Optionally, view the layout using the internal viewer (if needed)