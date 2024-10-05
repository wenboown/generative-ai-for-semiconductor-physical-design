import gdspy

# Create a new GDSII library
lib = gdspy.GdsLibrary()

# Create a new cell in the library
cell = lib.new_cell('ROUNDED_SQUARE')

# Define the size of the square and the corner radius in micrometers (µm)
square_size = 10000  # 10 mm = 10000 µm
corner_radius = 1000  # 1 mm = 1000 µm

# Create the inner rectangle (offset by the corner radius)
inner_rectangle = gdspy.Rectangle(
    (corner_radius, corner_radius),
    (square_size - corner_radius, square_size - corner_radius)
)

# Offset the rectangle outward by the corner radius with rounded corners
rounded_square = gdspy.offset(
    inner_rectangle,
    distance=corner_radius,
    join_first=True,
    join='round'
)

# Add the rounded square to the cell
cell.add(rounded_square)

# Save the library to a GDSII file
lib.write_gds('rounded_square.gds')