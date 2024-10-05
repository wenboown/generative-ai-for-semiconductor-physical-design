import gdspy
import numpy as np

# Define ellipse parameters
major_axis = 20.0  # mm
minor_axis = 13.0  # mm
layer = 0
center = (0.0, 0.0)

# Number of points to approximate the ellipse
num_points = 100

# Generate the coordinates for the ellipse
theta = np.linspace(0, 2 * np.pi, num_points)
x = (major_axis / 2) * np.cos(theta) + center[0]
y = (minor_axis / 2) * np.sin(theta) + center[1]
points = np.column_stack((x, y))

# Create the GDS library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('OVAL')

# Create the polygon for the ellipse
ellipse = gdspy.Polygon(points, layer=layer)
cell.add(ellipse)

# Save the design to a GDSII file
lib.write_gds('oval_design.gds')

print("GDS file 'oval_design.gds' has been created containing the oval layout.")