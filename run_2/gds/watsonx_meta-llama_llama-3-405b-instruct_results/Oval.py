import gdspy

# Define the library and cell for the GDS layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell('oval')

# Define the major and minor axes of the oval
major_axis = 20
minor_axis = 13

# Create the oval as a polygon with precise coordinates
oval = gdspy.Round((0, 0), [major_axis/2, minor_axis/2], layer=0)

# Add the oval to the cell
cell.add(oval)

# Save the design to a GDS file
lib.write_gds('oval.gds')