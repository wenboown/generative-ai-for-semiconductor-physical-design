import gdspy
import numpy as np

# Calculate the radius of the circumscribed circle
edge_length = 10  # mm
radius = edge_length / (2 * np.sin(np.pi / 8))

# Calculate the coordinates of the octagon vertices
angles = np.linspace(0, 2*np.pi, 9)[:-1]  # 8 equally spaced angles
vertices = radius * np.column_stack((np.cos(angles), np.sin(angles)))

# Create a new library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('OCTAGON')

# Create the octagon polygon
octagon = gdspy.Polygon(vertices)

# Add the octagon to the cell
cell.add(octagon)

# Save the design to a GDS file
lib.write_gds('octagon.gds')