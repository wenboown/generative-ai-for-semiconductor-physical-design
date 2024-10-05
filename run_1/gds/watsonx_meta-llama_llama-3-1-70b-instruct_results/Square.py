import gdspy

# Define the GDS library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell("square")

# Define the square's dimensions in micrometers (1 mm = 1000 um)
square_width = 10000  # um

# Create the square with the lower right corner at (0, 0)
square = gdspy.Rectangle((0, 0), (square_width, square_width))

# Add the square to the cell
cell.add(square)

# Save the design to a GDS file
lib.write_gds('square.gds')