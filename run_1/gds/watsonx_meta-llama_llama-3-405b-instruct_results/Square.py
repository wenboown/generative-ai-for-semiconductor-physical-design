import gdspy

# Define the library and cell for the GDS layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell('square')

# Define the square with width 10 mm
square_width = 10
square = gdspy.Rectangle(-square_width, -square_width, 0, 0)

# Add the square to the cell
cell.add(square)

# Save the design to a GDS file
lib.write_gds('square.gds')