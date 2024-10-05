# Import the gdspy library
import gdspy

# Define the library and cell for the GDS layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell('triangle')

# Define the coordinates for the triangle
x, y = 0, 0  # Center of the triangle
edge_length = 10e3  # Length of each edge in units of microns

# Calculate the coordinates of the triangle vertices
x1, y1 = x - edge_length/2, y - edge_length*3**0.5/6
x2, y2 = x + edge_length/2, y - edge_length*3**0.5/6
x3, y3 = x, y + edge_length*3**0.5/3

# Create a polygon with the triangle vertices
triangle = gdspy.Polygon([(x1, y1), (x2, y2), (x3, y3)])

# Add the triangle to the cell
cell.add(triangle)

# Save the design to a GDS file
lib.write_gds('triangle.gds')