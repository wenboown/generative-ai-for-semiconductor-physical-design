import gdspy

# Create a new GDSII library with units in millimeters
lib = gdspy.GdsLibrary(unit=1e-3, precision=1e-9)

# Create a cell to hold the geometry
cell = lib.new_cell('SQUARE')

# Define the coordinates for the square
# Lower right corner at (0, 0)
# Square width is 10 mm
# Therefore, lower left corner is at (-10, 0)
# Upper left corner is at (-10, 10)
# Upper right corner is at (0, 10)
square = gdspy.Rectangle((-10, 0), (0, 10))

# Add the square to the cell
cell.add(square)

# Write the layout to a GDSII file
lib.write_gds('square.gds')