import gdspy
import math

# Calculate triangle dimensions
side_length = 10000  # 10 mm in nanometers
height = (math.sqrt(3) / 2) * side_length
half_width = side_length / 2

# Calculate vertex coordinates (centered at 0,0)
p1 = (-half_width, -height/2)
p2 = (half_width, -height/2)
p3 = (0, height/2)

# Create a new library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('TRIANGLE')

# Create a polygon for the triangle
triangle = gdspy.Polygon([p1, p2, p3])

# Add the triangle to the cell
cell.add(triangle)

# Save the design to a GDS file
lib.write_gds('triangle.gds')

print("Triangle GDS file has been generated successfully.")