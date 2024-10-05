import gdspy

# Create a new library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('CIRCLE')

# Define circle parameters
radius = 10 * 1000  # Convert 10 mm to μm
center = (0, 0)
layer = 0

# Create the circle
circle = gdspy.Round(center, radius, layer=layer, number_of_points=128)

# Add the circle to the cell
cell.add(circle)

# Save the design to a GDSII file
lib.write_gds('circle.gds')

print("GDSII file 'circle.gds' has been generated successfully.")