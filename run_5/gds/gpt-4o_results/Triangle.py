import gdspy
import numpy as np

# Convert from mm to micrometers (1 mm = 1000 micrometers)
scale_factor = 1000

# Functions to calculate the vertices of the equilateral triangle
def calculate_triangle_vertices(center, side_length):
    height = np.sqrt(3) / 2 * side_length
    
    # Vertices of the triangle centered at the origin
    vertices = [
        (0, 2 / 3 * height),
        (-side_length / 2, -1 / 3 * height),
        (side_length / 2, -1 / 3 * height)
    ]
    
    # Translate vertices to the center
    vertices = [(v[0] + center[0], v[1] + center[1]) for v in vertices]
    return vertices

# Define the side length in micrometers
side_length_um = 10 * scale_factor

# Center of the triangle at (0, 0)
center = (0, 0)

# Calculate the vertices of the triangle
vertices = calculate_triangle_vertices(center, side_length_um)

# Create a GDSII library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('TRIANGLE_CELL')

# Create the triangle as a polygon
triangle = gdspy.Polygon(vertices, layer=0)
cell.add(triangle)

# Save the cell to a GDSII file
output_file = 'triangle.gds'
lib.write_gds(output_file)

print(f"GDSII file '{output_file}' generated successfully.")