import gdspy

# Define the size of the square in microns (GDSII units)
# 10 mm = 10,000,000 microns
square_size = 10000

# Create a new GDSII library
lib = gdspy.GdsLibrary()

# Create a new cell named 'SQUARE'
cell = lib.new_cell('SQUARE')

# Coordinates for the bottom-left corner (placing bottom-right at (0,0))
x0, y0 = -square_size, 0
x1, y1 = 0, square_size

# Create a rectangle as Polygon
square = gdspy.Rectangle((x0, y0), (x1, y1))

# Add the square to the cell
cell.add(square)

# Write the GDSII file to disk
lib.write_gds('square_design.gds')