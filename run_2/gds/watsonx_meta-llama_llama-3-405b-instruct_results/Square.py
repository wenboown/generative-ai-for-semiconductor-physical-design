import gdspy

# Define the library and cell for the GDS layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell('square')

# Define the square dimensions
width = 10  # mm
x_ur = 0  # x-coordinate of upper-right corner
y_ur = width  # y-coordinate of upper-right corner

# Create the square element
square = gdspy.Rectangle((x_ur - width, y_ur - width), (x_ur, y_ur), layer=1)

# Add the square to the cell
cell.add(square)

# Save the design to a GDS file
lib.write_gds('square.gds')