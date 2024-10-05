import gdspy
import numpy as np

# Create a new GDSII library
lib = gdspy.GdsLibrary()

# Create a cell to add the polygon
cell = lib.new_cell('PENTAGON')

# Number of sides
n = 5

# Side length in micrometers (since GDSII units are in micrometers)
s = 10000.0  # 10 mm = 10000 micrometers

# Compute the radius R required for the given side length
# s = 2 * R * sin(pi / n)
R = s / (2 * np.sin(np.pi / n))

# Compute the angles for each vertex
angles = np.linspace(np.pi / 2, np.pi / 2 + 2 * np.pi, n, endpoint=False)

# Compute the coordinates of the vertices
x = R * np.cos(angles)
y = R * np.sin(angles)

# Create the polygon
pentagon = gdspy.Polygon(list(zip(x, y)))

# Add the polygon to the cell
cell.add(pentagon)

# Write the GDSII file
lib.write_gds('pentagon.gds')