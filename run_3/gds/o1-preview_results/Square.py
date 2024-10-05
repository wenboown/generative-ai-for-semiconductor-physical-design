import gdspy

# Create a GDSII library named 'square_lib'
lib = gdspy.GdsLibrary('square_lib')

# Create a cell named 'SQUARE'
cell = lib.new_cell('SQUARE')

# Define the square dimensions in micrometers (10 mm = 10,000 µm)
square_size = 10000  # 10 mm in micrometers

# Coordinates for the square
# Lower right corner at (0, 0)
# The square extends to the left (negative x) and upwards (positive y)
lower_right = (0, 0)
upper_left = (-square_size, square_size)

# Create the square polygon
square = gdspy.Rectangle(upper_left, lower_right)

# Add the square to the cell
cell.add(square)

# Save the library in a GDSII file named 'square.gds'
lib.write_gds('square.gds')