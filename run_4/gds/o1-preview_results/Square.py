import gdspy

# Create a new GDSII library
lib = gdspy.GdsLibrary()

# Create a new cell in the library
cell = lib.new_cell('SQUARE_CELL')

# Define the coordinates of the square
# Side length is 10,000 micrometers (10 mm)
# Lower right corner at (0, 0)
square = gdspy.Rectangle(
    (-10000, 0),  # Lower left corner
    (0, 10000)    # Upper right corner
)

# Add the square to the cell
cell.add(square)

# Save the library to a GDSII file
lib.write_gds('square.gds')