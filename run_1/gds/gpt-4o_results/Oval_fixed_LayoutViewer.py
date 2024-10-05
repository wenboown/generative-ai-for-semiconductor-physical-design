import gdspy
import numpy as np

# Initialize GDSII library
lib = gdspy.GdsLibrary()

# Create a cell to contain the design
cell = lib.new_cell('OVAL')

# Parameters for the oval
center = (0, 0)
major_axis = 20.0  # mm
minor_axis = 13.0  # mm
layer = 0

# Generate points for the oval
num_points = 200
theta = np.linspace(0, 2 * np.pi, num_points)
x_points = center[0] + (major_axis / 2) * np.cos(theta)
y_points = center[1] + (minor_axis / 2) * np.sin(theta)
oval_points = np.column_stack((x_points, y_points))

# Create the polygon representing the oval
oval = gdspy.FlexPath([oval_points, oval_points[-1]], 0, layer=layer, datatype=0)

# Add the oval to the cell
cell.add(oval)

# Save the design to a GDS file
lib.write_gds('oval_design.gds')

# Optionally, display all cells using the internal viewer