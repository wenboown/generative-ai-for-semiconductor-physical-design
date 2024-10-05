import gdspy

# Create a new GDSII library.
gdsii_lib = gdspy.GdsLibrary()

# Create a new cell where the circle will be added.
cell = gdsii_lib.new_cell('CIRCLE_CELL')

# Define the circle parameters.
radius = 10000  # in micrometers (10 mm = 10000 micrometers)
center = (0, 0)  # Circle center at origin
layer = 0  # Specify layer

# Create the circle using gdspy.Round.
circle = gdspy.Round(center, radius, layer=layer, number_of_points=128)

# Add the circle to the cell.
cell.add(circle)

# Save the GDSII library to a file.
gdsii_lib.write_gds('circle.gds')

print("GDSII file 'circle.gds' created successfully.")