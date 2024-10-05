import gdspy
import numpy as np

# Define the ellipse parameters
major_axis = 20.0
minor_axis = 13.0
center = (0, 0)
layer = 0

# Create a new GDSII library
library = gdspy.GdsLibrary()

# Create a new cell
cell = library.new_cell('EllipseCell')

# Define number of points to create the ellipse
num_points = 100  # More points for smoother ellipse

# Calculate the points of the ellipse
ellipse_points = [
    (center[0] + (major_axis / 2.0) * np.cos(2 * np.pi * i / num_points),
     center[1] + (minor_axis / 2.0) * np.sin(2 * np.pi * i / num_points))
    for i in range(num_points)
]

# Create the polygon for the ellipse
ellipse_polygon = gdspy.Polygon(ellipse_points, layer)

# Add the polygon to the cell
cell.add(ellipse_polygon)

# Save to a GDSII file
library.write_gds('ellipse.gds')

print('GDS file "ellipse.gds" has been created successfully.')