import gdspy

# Create a new library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell("triangle")

# Define the coordinates of the triangle vertices
vertex1 = (-5, -4.33)  # coordinates for a 10mm equilateral triangle
vertex2 = (5, -4.33)
vertex3 = (0, 8.66)

# Create the triangle using the gdspy.Polygon function
triangle = gdspy.Polygon([vertex1, vertex2, vertex3], layer=1, datatype=0)

# Add the triangle to the cell
cell.add(triangle)

# Save the design to a GDS file
lib.write_gds("triangle.gds")