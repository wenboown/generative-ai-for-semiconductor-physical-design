import gdspy

# Create a new GDSII library, which contains multiple cells.
lib = gdspy.GdsLibrary()

# Create a new cell in the library called 'ROUND_SQUARE'
cell = lib.new_cell('ROUND_SQUARE')

# Define the coordinates for the square with rounded corners
square_size = 10e3  # size of the square in micrometers (um)
radius = 1e3  # radius of corner rounding in micrometers (um)
half_size = square_size / 2

# Create the main square body with rounded corners using a polygon
rounded_square = gdspy.Round((half_size, half_size), square_size, inner_radius=(square_size / 2) - abs(2 * radius))

# Add the rounded square to the cell
cell.add(rounded_square)

# Create the roundings at each corner
for corner in [(radius, radius), (square_size - radius, radius), (square_size - radius, square_size - radius), (radius, square_size - radius)]:
    corner_rounding = gdspy.Round(corner, radius, tolerance=0.01)
    cell.add(corner_rounding)

# Save the library in a GDSII file called 'rounded_square.gds'
lib.write_gds('rounded_square.gds')

# Optionally, use the internal viewer to display the layout