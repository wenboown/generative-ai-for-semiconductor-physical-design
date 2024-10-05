import gdspy

# Create a GDSII library
lib = gdspy.GdsLibrary()

# Create a cell to add elements
cell = lib.new_cell('CIRCLE_CELL')

# Define the circle parameters
radius = 10000  # 10 mm in micrometers
center = (0, 0)
number_of_points = 128  # Number of points to approximate the circle

# Create the circle
circle = gdspy.Round(center, radius, number_of_points=number_of_points, layer=0)

# Add the circle to the cell
cell.add(circle)

# Save the library in a GDSII file
lib.write_gds('circle.gds')