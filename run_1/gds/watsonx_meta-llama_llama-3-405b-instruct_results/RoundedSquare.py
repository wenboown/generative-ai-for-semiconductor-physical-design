import gdspy

# Define the library and cell for the GDS layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell('Square_with_Rounded_Corners')

# Define the dimensions of the square and the radius of the corner rounding
square_size = 10  # mm
r = 1  # mm

# Calculate the coordinates of the square's corners
x1, y1 = 0, 0
x2, y2 = square_size, 0
x3, y3 = square_size, square_size
x4, y4 = 0, square_size

# Create the square with rounded corners by using the Polygon class
points = [
    (x1 + r, y1),
    (x2 - r, y1),
    (x2, y1 + r),
    (x2, y3 - r),
    (x2 - r, y3),
    (x1 + r, y3),
    (x1, y3 - r),
    (x1, y1 + r)
]

# Create the polygon with the calculated points
poly = gdspy.Polygon(points, layer=0, datatype=0)

# Add the polygon to the cell
cell.add(poly)

# Create quarter circles for each corner
for x, y in [(x1, y1), (x2, y1), (x2, y3), (x1, y3)]:
    quarter_circle = gdspy.Round((x, y), r, number_of_points=100, layer=0, datatype=0, max_points=1000)
    cell.add(quarter_circle)

# Save the design to a GDS file
lib.write_gds('square_with_rounded_corners.gds')