import gdspy
import math

# Define the library and cell for the GDS layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell('heptagon')

# Calculate the coordinates for the heptagon
radius = 10 / (2 * math.sin(math.pi/7))
points = []
for i in range(7):
    angle = 2 * math.pi * i / 7
    x = radius * math.cos(angle)
    y = radius * math.sin(angle)
    points.append((x, y))

# Create the heptagon
heptagon = gdspy.Polygon(points)

# Add the heptagon to the cell
cell.add(heptagon)

# Save the design to a GDS file
lib.write_gds('heptagon.gds')