import gdspy

# Define the GDS library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('Circle_Cell')

# Define the layer and radius of the circle
layer = 0
radius = 10  # in microns, not millimeters

# Create the circle
circle = gdspy.Round((0, 0), radius, layer=layer, datatype=0)

# Add the circle to the cell
cell.add(circle)

# Save the layout to a GDS file
lib.write_gds('circle.gds')

# Display the layout