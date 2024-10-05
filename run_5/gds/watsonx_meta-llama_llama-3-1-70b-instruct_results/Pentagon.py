import gdspy
import numpy as np

# Define the GDS library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('pentagon')

# Calculate the coordinates of the pentagon
angle = 2 * np.pi / 5
points = []
for i in range(5):
    x = 10 * np.cos(i * angle)
    y = 10 * np.sin(i * angle)
    points.append((x, y))

# Create the polygon
poly = gdspy.Polygon(points)

# Add the polygon to the cell
cell.add(poly)

# Save the GDS file
lib.write_gds('pentagon.gds')