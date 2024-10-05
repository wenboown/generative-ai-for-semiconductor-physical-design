import gdspy

# Define the size of the square in GDS units (microns)
square_size = 10000  # 10 mm = 10000 microns

# Create a new GDSII library
lib = gdspy.GdsLibrary()

# Create a new cell named 'SQUARE'
cell = lib.new_cell('SQUARE')

# Define the coordinates of the square
# Lower right corner at (0, 0)
# Lower left corner at (-square_size, 0)
# Upper right corner at (0, square_size)
# Upper left corner at (-square_size, square_size)
square = gdspy.Rectangle((-square_size, 0), (0, square_size))

# Add the square to the cell
cell.add(square)

# Save the design to a GDS file
lib.write_gds('square_design.gds')

print("GDS file 'square_design.gds' created successfully with a square having its lower-right corner at (0, 0).")