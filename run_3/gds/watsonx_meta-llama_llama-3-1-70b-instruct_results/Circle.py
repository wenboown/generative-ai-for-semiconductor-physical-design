import gdspy

# Define the library and cell for the GDS layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell('circle')

# Define the layer for the circle
layer = 0

# Define the radius and center coordinates of the circle
radius = 10  # in microns (GDSII uses microns)
center_x, center_y = 0, 0

# Create the circle with precise coordinates
circle = gdspy.Round((center_x, center_y), radius, layer=layer, number_of_points=100)

# Add the circle to the cell
cell.add(circle)

# Save the design to a GDS file
lib.write_gds('circle.gds')