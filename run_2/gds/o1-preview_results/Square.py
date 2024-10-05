import gdspy

# Create a new GDSII library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('SQUARE_CELL')

# Define the square dimensions (10 mm converted to micrometers)
square_width = 10000  # in micrometers

# Coordinates of the square (lower right corner at (0, 0))
square_points = [
    (0, 0),                       # Lower right corner
    (-square_width, 0),           # Lower left corner
    (-square_width, square_width),# Upper left corner
    (0, square_width)             # Upper right corner
]

# Create the square polygon
square = gdspy.Polygon(square_points, layer=1)

# Add the square to the cell
cell.add(square)

# Save the GDSII file
lib.write_gds('square.gds')