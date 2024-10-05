import gdspy
import numpy as np

# Define the library and cell for the GDS layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell('oval')

# Define the major and minor axes of the oval
major_axis = 20e-3  # Convert mm to meters (1e-3)
minor_axis = 13e-3  # Convert mm to meters (1e-3)

# Calculate the center coordinates
center_x, center_y = (0, 0)

# Calculate the number of points for the oval
num_points = 100

# Generate the points of the oval
theta = np.linspace(0, 2 * np.pi, num_points)
x = major_axis * np.cos(theta) + center_x
y = minor_axis * np.sin(theta) + center_y

# Create the oval as a polygon
oval = gdspy.Polygon(list(zip(x, y)), layer=0)

# Add the oval to the cell
cell.add(oval)

# Save the design to a GDS file
lib.write_gds('oval.gds')