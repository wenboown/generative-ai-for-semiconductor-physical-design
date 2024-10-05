import gdspy
import numpy as np

# Define the library and cell for the GDS layout
lib = gdspy.Library()
cell = lib.new_cell("hexagon")

# Define the parameters of the hexagon
edge_length = 10  # in mm
center_x, center_y = 0, 0

# Calculate the coordinates of the vertices of the hexagon
angle = np.linspace(0, 2*np.pi, 6, endpoint=False)
vertices_x = center_x + edge_length * np.cos(angle)
vertices_y = center_y + edge_length * np.sin(angle)

# Create the hexagon polygon
hexagon = gdspy.Polygon(vertices=[(x, y) for x, y in zip(vertices_x, vertices_y)])

# Add the hexagon to the cell
cell.add(hexagon)

# Save the design to a GDS file
lib.write_gds("hexagon.gds")