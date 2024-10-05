import gdspy
import numpy as np

# Create a GDSII library
lib = gdspy.GdsLibrary()

# Create a cell to hold the design
cell = lib.new_cell('OVAL_DESIGN')

# Oval parameters
major_axis = 20.0   # in mm
minor_axis = 13.0   # in mm
center_x, center_y = 0, 0  # center of the oval

# Convert dimensions from mm to μm (since GDS typically uses μm units)
major_axis_um = major_axis * 1000
minor_axis_um = minor_axis * 1000

# Define the number of points for the polygon approximation of the oval
num_points = 200
theta = np.linspace(0, 2 * np.pi, num_points)
x = center_x + (major_axis_um / 2) * np.cos(theta)
y = center_y + (minor_axis_um / 2) * np.sin(theta)

points = np.vstack((x, y)).T

# Create the polygon representing the oval
oval = gdspy.Polygon(points, layer=0)

# Add the polygon to the cell
cell.add(oval)

# Save the library to a GDSII file
lib.write_gds('oval_design.gds')

print("Oval GDSII design saved as 'oval_design.gds'")