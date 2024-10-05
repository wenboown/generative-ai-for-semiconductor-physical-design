import gdspy

# Define the square dimensions
square_width = 10000  # microns (10 mm)

# Create a new GDSII library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('SQUARE')

# Create the square with lower right corner at (0, 0)
square = gdspy.Rectangle((0, 0), (-square_width, square_width))

# Add the square to the cell
cell.add(square)

# Save the design to a GDS file
lib.write_gds('square_10mm.gds')

print("GDS file 'square_10mm.gds' has been generated.")