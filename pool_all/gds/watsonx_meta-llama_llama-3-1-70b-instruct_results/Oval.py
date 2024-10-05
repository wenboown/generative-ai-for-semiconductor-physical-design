import gdspy
import numpy as np

# Define the library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('oval')

# Set the layer and oval parameters
layer = 0
major_axis = 20e3  # Convert mm to microns
minor_axis = 13e3  # Convert mm to microns
center = (0, 0)

# Calculate the number of points for the polygon approximation
num_points = 100

# Generate the points for the oval using parametric equations
theta = np.linspace(0, 2*np.pi, num_points)
x = center[0] + major_axis / 2 * np.cos(theta)
y = center[1] + minor_axis / 2 * np.sin(theta)

# Create the oval polygon
oval = gdspy.Polygon(np.column_stack((x, y)), layer)

# Add the oval to the cell
cell.add(oval)

# Save the design to a GDS file
lib.write_gds('oval_design.gds')

print("GDS file 'oval_design.gds' has been created successfully.")