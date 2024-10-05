import gdspy
import numpy as np

# Define the major and minor axes
major_axis = 20.0
minor_axis = 13.0
center = (0, 0)  # Center of the oval
layer = 0  # GDS layer

# Number of points to approximate an oval
num_points = 200

# Angle step to create the oval
theta = np.linspace(0, 2 * np.pi, num_points)

# Parametric equations for the oval
x = (major_axis / 2) * np.cos(theta) + center[0]
y = (minor_axis / 2) * np.sin(theta) + center[1]

# Combine x and y into a single array of points
points = np.array([x, y]).T

# Create a polygon with the points
oval = gdspy.Polygon(points, layer=layer)

# Create a GDS library and add the polygon to a cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('OVAL')
cell.add(oval)

# Save the library to a GDSII file
lib.write_gds('oval_design.gds')

print("Oval design saved to 'oval_design.gds'")