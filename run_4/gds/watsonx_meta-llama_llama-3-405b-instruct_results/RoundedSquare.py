import gdspy

# Define the library and cell for the GDS layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell('square_with_rounded_corners')

# Define the square's dimensions and corner radius
square_size = 10  # mm
corner_radius = 1  # mm

# Create the square with rounded corners
square = gdspy.Round(
    center=(0, 0),
    size=(square_size, square_size),
    inner_radius=corner_radius,
    layer=0,
    datatype=0
)

# Add the square to the cell
cell.add(square)

# Save the design to a GDS file
lib.write_gds('square_with_rounded_corners.gds')