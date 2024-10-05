import gdspy
import numpy as np

# Define the library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('Circle')

# Define the layer
layer = 0
datatype = 0

# Define the circle parameters
center = (0, 0)
radius = 10  # in um (1 mm = 1000 um)

# Generate the circle points
npoints = 100  # increasing this will make the circle smoother
theta = np.linspace(0, 2*np.pi, npoints+1)
x = center[0] + radius * np.cos(theta)
y = center[1] + radius * np.sin(theta)

# Create a polygon for the circle
poly = gdspy.Polygon(np.array([x, y]).T, layer=layer, datatype=datatype)

# Add the polygon to the cell
cell.add(poly)

# Save the design to a GDS file
lib.write_gds('circle.gds')