import gdspy

# Define the GDSII library, name and unit (1 unit = 1e-6 meter) and precision (1e-9 meter)
lib = gdspy.GdsLibrary(name='CircleDesign')

# Create a new cell where the circle will be added
cell = lib.new_cell('CIRCLE_CELL')

# Parameters for the circle
radius = 10000  # in micrometers (10 mm = 10000 micrometers)
center = (0, 0)

# Create the circle polygon
circle = gdspy.Round(center, radius, number_of_points=128, layer=0)

# Add the circle to the cell
cell.add(circle)

# Save to a GDSII file
lib.write_gds('circle_design.gds')

print("GDSII file 'circle_design.gds' has been created successfully.")