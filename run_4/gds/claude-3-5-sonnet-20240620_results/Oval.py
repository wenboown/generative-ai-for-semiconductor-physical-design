import gdspy
import numpy as np

# Create a new library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('OVAL')

# Define ellipse parameters
major_axis = 20000  # 20 mm in nanometers
minor_axis = 13000  # 13 mm in nanometers
center = (0, 0)
layer = 0

# Create the ellipse
# We'll use 64 points to approximate the ellipse
theta = np.linspace(0, 2*np.pi, 65)
x = center[0] + 0.5 * major_axis * np.cos(theta)
y = center[1] + 0.5 * minor_axis * np.sin(theta)
points = np.column_stack((x, y))

ellipse = gdspy.Polygon(points, layer=layer)

# Add the ellipse to the cell
cell.add(ellipse)

# Save the design to a GDS file
lib.write_gds('oval_design.gds')

print("GDS file 'oval_design.gds' has been created successfully.")