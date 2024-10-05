import gdspy

# Define the dimensions of the square
square_width = 10000  # microns (10 mm)

# Define the coordinates of the square
# Lower right corner at (0, 0)
lower_right_corner = (0, 0)
upper_left_corner = (-square_width, square_width)

# Create a GDSII library
lib = gdspy.GdsLibrary()

# Create a new cell to contain the design
cell = lib.new_cell('SQUARE_CELL')

# Create the square as a polygon
# Coordinates defined in a clockwise fashion starting from the lower right corner
square = gdspy.Rectangle(lower_right_corner, upper_left_corner)

# Add the square to the cell
cell.add(square)

# Save the design in a GDSII file
lib.write_gds('square_design.gds')

print("GDS file 'square_design.gds' created successfully.")