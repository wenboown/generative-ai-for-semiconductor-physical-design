import gdspy

# Define the GDS library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('oval')

# Create the oval shape
oval = gdspy.ellipse(0, 0, 20/2, 13/2, layer=0, number_of_points=64)

# Add the shape to the cell
cell.add(oval)

# Save the design to a GDS file
lib.write_gds('oval.gds')