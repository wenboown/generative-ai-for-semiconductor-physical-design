import gdspy

# Create a new GDSII library
lib = gdspy.GdsLibrary()

# Create a new cell where the geometry will be placed
cell = lib.new_cell('CIRCLE_CELL')

# Define the radius and center of the circle in micrometers
radius = 10000  # 10 mm = 10,000 micrometers
center = (0, 0)

# Create the circle on layer 0
circle = gdspy.Round(center, radius, number_of_points=256, layer=0)

# Add the circle to the cell
cell.add(circle)

# Save the library in a GDSII file
lib.write_gds('circle.gds')

print("GDSII file 'circle.gds' has been created with a circle of radius 10 mm at the center (0,0) on layer 0.")