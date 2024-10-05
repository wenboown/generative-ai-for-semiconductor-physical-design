import gdspy

# Define the library and cell for the GDS layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell('square')

# Define the square's dimensions and position
width = 10  # mm
x = 0  # mm, x-coordinate of lower right corner
y = 0  # mm, y-coordinate of lower right corner

# Create the square as a rectangle
square = gdspy.Rectangle((x - width, y), (x, y + width))

# Add the square to the cell
cell.add(square)

# Save the design to a GDS file
lib.write_gds('square.gds')