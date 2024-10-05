import gdspy
import numpy as np

# Define the library and cell for the GDS layout
lib = gdspy.GdsLibrary(unit=1e-6, precision=1e-10)
cell = lib.new_cell('oval')

# Set the layer
layer = 0

# Define the major and minor axes
major_axis = 20e3  # convert to microns
minor_axis = 13e3  # convert to microns

# Create the oval
theta = np.linspace(0, 2*np.pi, 100)
x = major_axis / 2 * np.cos(theta)
y = minor_axis / 2 * np.sin(theta)

# Create a polygon from the oval coordinates
polygon = gdspy.Polygon([(x_i, y_i) for x_i, y_i in zip(x, y)], layer=layer)

# Add the polygon to the cell
cell.add(polygon)

# Save the design to a GDS file
lib.write_gds('oval.gds')