import gdspy

# Define the oval parameters
major_axis = 20  # in mm
minor_axis = 13  # in mm
layer = 0
center = (0, 0)

# Define the GDS library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('oval_cell')

# Create the oval shape
oval = gdspy.ellipse(center, major_axis/2, minor_axis/2, layer=layer)

# Add the oval to the cell
cell.add(oval)

# Save the design to a GDS file
lib.write_gds('oval.gds')