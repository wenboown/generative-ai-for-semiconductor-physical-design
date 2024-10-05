import gdspy

# Create a new GDSII library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('SQUARE_CELL')

# Define the square dimensions
square_size = 10.0  # size in mm

# Define the coordinates of the square
# Since we're placing the lower-right corner at (0,0), we need to
# define the bottom-left as (-square_size, 0) and top-right as (0, square_size)
square = gdspy.Rectangle((-square_size, 0), (0, square_size))

# Add the square to the cell
cell.add(square)

# Save the library to a GDSII file
lib.write_gds('square.gds')

print("The GDS file 'square.gds' has been created successfully.")