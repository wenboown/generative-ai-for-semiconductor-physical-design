import gdspy

# Define the library and cell for the GDS layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell('square_with_rounded_corners')

# Define the square's dimensions
square_size = 10
corner_radius = 1

# Create the square with rounded corners
square = gdspy.Round(
    [(0, 0), (square_size, 0), (square_size, square_size), (0, square_size)],
    corner_radius,
    number_of_points=128,
    layer=0,
    datatype=0
)

# Add the square to the cell
cell.add(square)

# Save the design to a GDS file
lib.write_gds('square_with_rounded_corners.gds')