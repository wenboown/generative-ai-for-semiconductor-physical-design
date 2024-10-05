import gdspy
import numpy as np

# Define the library and cell for the GDS layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell('circle')

# Define the circle parameters
layer = 0
radius = 10  # in um (1 mm = 1000 um)
center = (0, 0)

# Generate the circle as a polygon
circle = gdspy.Round(center, radius, layer=layer)

# Add the circle to the cell
cell.add(circle)

# Save the design to a GDS file
lib.write_gds('circle.gds')