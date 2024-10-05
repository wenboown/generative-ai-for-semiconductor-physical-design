import gdspy

# Design specifications
square_width = 10e3  # in microns (10 mm = 10000 microns)

# Define the library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('SQUARE_DESIGN')

# Create the square
square_corners = [
    (0, 0),  # Lower right corner at (0, 0)
    (-square_width, 0),  # Lower left corner
    (-square_width, square_width),  # Upper left corner
    (0, square_width)  # Upper right corner
]

square = gdspy.Polygon(square_corners)

# Add the square to the cell
cell.add(square)

# Save the design to a GDS file
lib.write_gds('square_design.gds')

print('GDS file "square_design.gds" has been created with a square of width 10 mm.')