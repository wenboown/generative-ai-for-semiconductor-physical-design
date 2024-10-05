import gdspy
import numpy as np

# Define the library and cell for the GDS layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell("hexagon")

# Define the center of the hexagon
center = (0, 0)

# Define the edge length of the hexagon
edge_length = 10

# Calculate the coordinates of the hexagon vertices
angle = np.linspace(0, 2*np.pi, 6, endpoint=False)
vertices = np.column_stack((np.cos(angle), np.sin(angle))) * edge_length / 2
vertices = vertices + center

# Create the hexagon polygon
hexagon = gdspy.Polygon(vertices, layer=1, datatype=[0, 0])

# Add the hexagon to the cell
cell.add(hexagon)

# Save the design to a GDS file
lib.write_gds("hexagon.gds")