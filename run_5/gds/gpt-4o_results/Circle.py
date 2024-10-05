import gdspy

# Define the GDSII library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('CIRCLE')

# Define the parameters for the circle
radius = 10000  # 10 mm in microns
num_points = 100  # Number of points to approximate the circle
layer = 0

# Create a circle using a polygon approximation
circle = gdspy.Round((0, 0), radius, number_of_points=num_points, layer=layer)

# Add the circle to the cell
cell.add(circle)

# Save the library to a GDS file
lib.write_gds('circle.gds')

print("GDSII file 'circle.gds' has been created.")