import gdspy

# Define the GDS library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('Oval')

# Define the oval with major and minor axes
major_axis = 20
minor_axis = 13
center = (0, 0)
layer = 0

# Create an oval shape using the gdspy.Round function
oval = gdspy.Round(center, [major_axis/2, minor_axis/2], layer=layer)

# Add the oval shape to the cell
cell.add(oval)

# Save the design to a GDS file
lib.write_gds('oval.gds')