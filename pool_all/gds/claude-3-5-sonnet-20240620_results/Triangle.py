import gdspy
import numpy as np

# Create a new library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('TRIANGLE')

# Define triangle parameters
side_length_mm = 10
side_length_um = side_length_mm * 1000  # Convert mm to μm

# Calculate triangle dimensions
height = side_length_um * np.sqrt(3) / 2
half_width = side_length_um / 2

# Calculate vertex coordinates (centered at 0,0)
vertices = [
    (0, height / 3),  # Top vertex
    (-half_width, -height / 3),  # Bottom-left vertex
    (half_width, -height / 3)  # Bottom-right vertex
]

# Create the triangle polygon
triangle = gdspy.Polygon(vertices, layer=0)

# Add the triangle to the cell
cell.add(triangle)

# Save the design to a GDS file
lib.write_gds('triangle.gds')

print("GDS file 'triangle.gds' has been generated.")