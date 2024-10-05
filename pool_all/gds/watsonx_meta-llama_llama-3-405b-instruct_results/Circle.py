import gdspy

# Define the GDSII library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('CIRCLE')

# Define the circle parameters
radius = 10000  # 10 mm in micrometers
center = (0, 0)
layer = 0

# Create the circle
circle = gdspy.Round(center, radius, layer=layer)

# Add the circle to the cell
cell.add(circle)

# Save the design to a GDSII file
lib.write_gds('circle.gds')

print("GDSII file 'circle.gds' has been created.")