import gdspy

# Define the GDSII library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('CIRCLE')

# Define the circle parameters
radius = 10000  # in micrometers (10 mm = 10000 micrometers)
center = (0, 0)  # Center of the circle
layer = 0  # GDSII layer number

# Create the circle
circle = gdspy.Round(center, radius, number_of_points=128, layer=layer)

# Add the circle to the cell
cell.add(circle)

# Save the design to a GDSII file
lib.write_gds('circle_design.gds')

print("GDSII file 'circle_design.gds' has been created successfully.")