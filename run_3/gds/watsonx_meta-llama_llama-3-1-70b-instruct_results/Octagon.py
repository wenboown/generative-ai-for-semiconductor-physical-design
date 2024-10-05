import gdspy
import numpy as np

# Define the library and cell for the GDS layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell('Octagon')

# Define the Octagon parameters
edge_length = 10  # mm
center = (0, 0)  # mm

# Calculate the coordinates of the Octagon
angle = np.linspace(0, 2*np.pi, 9, endpoint=False)[1:]  # 8 edges, starting from 1st point (not 0)
points = [(center[0] + edge_length/2*np.cos(a), center[1] + edge_length/2*np.sin(a)) for a in angle]

# Add the Octagon to the cell
octagon = gdspy.Polygon(points, layer=1)
cell.add(octagon)

# Save the design to a GDS file
lib.write_gds('octagon.gds')