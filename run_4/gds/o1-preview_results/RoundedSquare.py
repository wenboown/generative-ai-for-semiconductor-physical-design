import gdspy

# Create a new GDSII library with default unit (1 micron) and precision
lib = gdspy.GdsLibrary()

# Create a cell to contain the layout
cell = lib.new_cell('ROUNDED_SQUARE')

# Define the size of the square in microns (10 mm = 10000 microns)
size = 10000  # square size in microns
radius = 1000  # corner rounding radius in microns

# Create a rectangle from (0, 0) to (size, size)
square = gdspy.Rectangle((0, 0), (size, size))

# Apply fillet to round the corners with the specified radius
square.fillet(radius)

# Add the rounded square to the cell
cell.add(square)

# Save the library to a GDSII file
lib.write_gds('rounded_square.gds')