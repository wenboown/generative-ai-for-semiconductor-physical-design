import gdspy
import numpy as np

# Create a new library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('OVAL')

# Define oval parameters
major_axis = 20000  # 20 mm in nanometers
minor_axis = 13000  # 13 mm in nanometers
center = (0, 0)
layer = 0

# Number of points to approximate the oval
num_points = 200

# Generate points for the oval
theta = np.linspace(0, 2*np.pi, num_points)
x = center[0] + (major_axis/2) * np.cos(theta)
y = center[1] + (minor_axis/2) * np.sin(theta)
points = np.column_stack((x, y))

# Create the oval polygon
oval = gdspy.Polygon(points, layer=layer)

# Add the oval to the cell
cell.add(oval)

# Save the design to a GDS file
lib.write_gds('oval_design.gds')

print("GDS file 'oval_design.gds' has been created successfully.")