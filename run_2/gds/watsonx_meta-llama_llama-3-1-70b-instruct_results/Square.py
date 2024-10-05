import gdspy

# Define the GDS library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('square_design')

# Define the layer for the square (layer 1, datatype 0)
layer = (1, 0)

# Create the square with width 10 mm, placing the lower right corner at (0, 0)
square = gdspy.Rectangle((0, 0), (10, 10), layer=layer)

# Add the square to the cell
cell.add(square)

# Save the design to a GDS file
lib.write_gds('square_design.gds', unit=1.0e-6, precision=1.0e-9)