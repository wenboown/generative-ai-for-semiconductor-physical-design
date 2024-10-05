import gdspy

# Create a new GDSII library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('SQUARE')

# Define the coordinates for the square
# Lower right corner at (0, 0)
# Lower left corner at (-10000, 0)
# Upper left corner at (-10000, 10000)
# Upper right corner at (0, 10000)

# Create the square as a rectangle shape
square = gdspy.Rectangle((-10000, 0), (0, 10000))

# Add the square to the cell
cell.add(square)

# Save the library to a GDSII file
lib.write_gds('square.gds')