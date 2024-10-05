import gdspy
import numpy as np

# Define the library and cell for the GDS layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell('Circle')

# Define layer 0
layer = 0
datatype = 0

# Define the circle's radius and center coordinates
radius = 10  # in mm, but GDSII uses microns, so we'll convert
radius_um = radius * 1000  # convert mm to um
center_x, center_y = 0, 0

# Create a circle using a polygon with many sides
num_points = 100  # number of points to approximate the circle
theta = np.linspace(0, 2*np.pi, num_points)
x = radius_um * np.cos(theta) + center_x
y = radius_um * np.sin(theta) + center_y
poly = gdspy.Polygon([(x[i], y[i]) for i in range(num_points)])

# Add the polygon to the cell on layer 0
cell.add(poly, layer=layer, datatype=datatype)

# Save the design to a GDS file
lib.write_gds('circle.gds')