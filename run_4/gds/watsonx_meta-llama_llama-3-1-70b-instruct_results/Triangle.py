import gdspy

# Create a new GDS library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell("triangle")

# Define the triangle coordinates
x = 0
y = 0
side_length = 10
height = side_length * 0.8660254037844386  # Using 30-60-90 triangle properties

triangle_points = [
    (x - side_length/2, y - height/3),
    (x + side_length/2, y - height/3),
    (x, y + 2*height/3)
]

# Create the triangle polygon
triangle = gdspy.Polygon(triangle_points)

# Add the triangle to the cell
cell.add(triangle)

# Save the design to a GDS file
lib.write_gds('triangle.gds')