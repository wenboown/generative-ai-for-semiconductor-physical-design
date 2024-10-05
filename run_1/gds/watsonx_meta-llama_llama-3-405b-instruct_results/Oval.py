import gdspy
import numpy as np

# Define the library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('oval')

# Define the layer
layer = 0

# Define the major and minor axes
major_axis = 20
minor_axis = 13

# Calculate the coordinates for the oval
num_points = 100
theta = np.linspace(0, 2*np.pi, num_points)
x = major_axis * np.cos(theta) / 2
y = minor_axis * np.sin(theta) / 2

# Create the oval polygon
oval = gdspy.Polygon(np.column_stack((x, y)))

# Add the oval to the cell on the specified layer
cell.add(oval.layers(layer).translate(0, 0))

# Save the design to a GDS file
lib.write_gds('oval.gds')