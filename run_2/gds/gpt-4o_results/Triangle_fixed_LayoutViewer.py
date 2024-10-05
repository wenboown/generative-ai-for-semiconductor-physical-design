import gdspy
import numpy as np

# Function to generate an equilateral triangle centered at the origin
def create_equilateral_triangle(side_length):
    # Height of equilateral triangle
    height = (np.sqrt(3) / 2) * side_length
    # Vertices of the equilateral triangle
    vertices = [
        (-side_length / 2, -height / 3),
        (side_length / 2, -height / 3),
        (0, 2 * height / 3)
    ]
    return vertices

# Define GDSII library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('EQUILATERAL_TRIANGLE')

# Create the triangle
side_length = 10_000  # 10 mm in micrometers (GDSII unit is micrometer)
triangle_vertices = create_equilateral_triangle(side_length)
triangle = gdspy.Polygon(triangle_vertices, layer=1)

# Add the triangle to the cell
cell.add(triangle)

# Save the layout to a GDS file
lib.write_gds('equilateral_triangle.gds')

# Export to SVG for visualization (optional)