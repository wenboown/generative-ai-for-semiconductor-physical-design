import gdspy

# Parse the user's design specifications
width = 10  # mm

# Define the library and cell for the GDS layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell('square')

# Create the square with precise coordinates
lower_right_corner = (0, 0)
upper_left_corner = (-width, width)
square = gdspy.Rectangle(lower_right_corner, upper_left_corner, layer=0, datatype=0)

# Add the square to the cell
cell.add(square)

# Save the design to a GDS file
lib.write_gds('square.gds')