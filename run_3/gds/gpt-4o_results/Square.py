import gdspy

# Define the unit (in meters) for a 10 mm square
unit = 1e-6  # GDSII unit in meters (1 micron)
width = 10 / 1000  # Convert 10 mm to meters

# Create a new GDSII library
lib = gdspy.GdsLibrary()

# Create a new cell for our square
cell = lib.new_cell('SQUARE_CELL')

# Define the coordinates for the square: lower right corner at (0, 0)
# Lower left corner: (-width, 0)
# Lower right corner: (0, 0)
# Upper right corner: (0, width)
# Upper left corner: (-width, width)
square = gdspy.Rectangle((-width, 0), (0, width))

# Add the square to the cell
cell.add(square)

# Save the library in a GDSII file called 'square.gds'
lib.write_gds('square.gds')

print("GDS file 'square.gds' with a 10mm square generated successfully.")