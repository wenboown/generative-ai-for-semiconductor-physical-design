import gdspy
import numpy as np

# Parse the design specifications
edge_length = 10  # mm
center_x, center_y = 0, 0  # mm

# Define the library and cell for the GDS layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell('Octagon')

# Calculate the coordinates of the octagon
angle = np.linspace(0, 2*np.pi, 9, endpoint=False)
x = center_x + edge_length / np.sqrt(2) * np.cos(angle)
y = center_y + edge_length / np.sqrt(2) * np.sin(angle)

# Create the polygons
octagon = gdspy.Polygon([(x[i], y[i]) for i in range(8)], layer=1)

# Add the octagon to the cell
cell.add(octagon)

# Save the design to a GDS file
lib.write_gds('octagon.gds')