import gdspy

# Define the library and cell for the GDS layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell('square_with_rounded_corners')

# Define the square's dimensions and corner radius
square_size = 10  # mm
corner_radius = 1  # mm

# Calculate the coordinates for the square with rounded corners
points = [
    (corner_radius, 0),
    (square_size - corner_radius, 0),
    (square_size, corner_radius),
    (square_size, square_size - corner_radius),
    (square_size - corner_radius, square_size),
    (corner_radius, square_size),
    (0, square_size - corner_radius),
    (0, corner_radius)
]

# Create the square with rounded corners using the Polygon class
square = gdspy.Polygon(points)

# Add circular arcs for each corner
for x, y in [(0, 0), (square_size, 0), (square_size, square_size), (0, square_size)]:
    quarter_circle = gdspy.Round(x, y, corner_radius, corner_radius, number_of_points=100, layer=0, datatype=0)
    square = gdspy.boolean(square, quarter_circle, operation='or', layer=0, datatype=0)

# Add the square to the cell and save the design to a GDS file
cell.add(square)
lib.write_gds('square_with_rounded_corners.gds')