import gdspy

# Create a new library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('SQUARE')

# Create a square with width 10 mm, lower right corner at (0, 0)
square = gdspy.Rectangle((0, 0), (-10, 10))

# Add the square to the cell
cell.add(square)

# Save the design to a GDS file
lib.write_gds('square_layout.gds')

print("GDS file 'square_layout.gds' has been generated.")