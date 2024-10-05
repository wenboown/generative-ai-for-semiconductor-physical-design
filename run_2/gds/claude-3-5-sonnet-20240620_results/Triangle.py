import gdspy
import numpy as np

# Create a new library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('TRIANGLE')

# Triangle side length (in μm, as GDS units are typically in μm)
side_length = 10000  # 10 mm = 10000 μm

# Calculate triangle dimensions
height = side_length * np.sqrt(3) / 2
half_width = side_length / 2

# Calculate vertex coordinates
top = (0, height / 2)
bottom_left = (-half_width, -height / 2)
bottom_right = (half_width, -height / 2)

# Create polygon
triangle = gdspy.Polygon([top, bottom_left, bottom_right])

# Calculate centroid shift to center the triangle
centroid_shift = (0, -height / 6)

# Apply the shift to center the triangle
triangle.translate(-centroid_shift[0], -centroid_shift[1])

# Add the triangle to the cell
cell.add(triangle)

# Save the design to a GDS file
lib.write_gds('triangle.gds')

print("GDS file 'triangle.gds' has been generated.")