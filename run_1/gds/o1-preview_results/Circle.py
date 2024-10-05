import gdspy

# Create a new GDSII library with units in millimeters
lib = gdspy.GdsLibrary(unit=1e-3, precision=1e-9)

# Create a new cell
cell = lib.new_cell('CIRCLE_CELL')

# Define circle parameters
radius = 10  # Radius in mm
center = (0, 0)  # Center at (0, 0)
layer = 0  # GDSII layer number

# Create the circle
circle = gdspy.Round(center, radius, number_of_points=256, layer=layer)

# Add the circle to the cell
cell.add(circle)

# Write the GDSII file
lib.write_gds('circle.gds')