import gdspy

# Create a new GDS library and cell
lib = gdspy.Library()
cell = lib.new_cell("square")

# Define the square's dimensions and coordinates
square_width = 10  # mm
square_x = 0  # Lower right corner's x-coordinate
square_y = 0  # Lower right corner's y-coordinate

# Create the square
square = gdspy.Rectangle(
    (square_x, square_y),  # Lower right corner
    (square_x + square_width, square_y + square_width)  # Upper left corner
)

# Add the square to the cell
cell.add(square)

# Save the design to a GDS file
lib.write_gds("square.gds")