import gdspy

# Define the library and cell for the GDS layout
lib = gdspy.Library()
cell = lib.new_cell('square')

# Parse the user's design specifications
width = 10.0  # width of the square in mm
x = 0.0  # x-coordinate of the lower right corner
y = 0.0  # y-coordinate of the lower right corner

# Create a rectangle (square) with precise coordinates
# The coordinates are in the format (x, y), where (0, 0) is the lower right corner
rect = gdspy.Rectangle((x, y), (x + width, y + width))

# Add the rectangle to the cell
cell.add(rect)

# Save the design to a GDS file
lib.write_gds('square.gds')