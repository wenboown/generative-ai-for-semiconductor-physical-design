import gdspy
import math

# Create a new GDSII library, name it 'pentagon_lib', and a cell called 'pentagon_cell'
lib = gdspy.GdsLibrary()
cell = lib.new_cell('pentagon_cell')

# Constants for the pentagon
radius = 10 / (2 * math.sin(math.pi / 5)) # Radius of the circle circumscribing the pentagon
theta = 2 * math.pi / 5 # Angle between vertices in radians

# Calculate the coordinates of the vertices of the pentagon
vertices = []
for i in range(5):
    angle = theta * i - math.pi / 2 # Rotate by -90 degrees to center at (0, 0)
    x = radius * math.cos(angle)
    y = radius * math.sin(angle)
    vertices.append((x, y))

# Create the pentagon as a polygon
pentagon = gdspy.Polygon(vertices)

# Add the pentagon to the cell
cell.add(pentagon)

# Save the library to a GDSII file
lib.write_gds('pentagon.gds')

# Optionally display the layout using the internal viewer 
sh
pip install gdspy