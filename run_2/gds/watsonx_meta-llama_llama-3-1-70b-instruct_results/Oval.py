import gdspy

# Define the GDS library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('Oval')

# Create the oval shape
oval = gdspy.Round((0, 0), 20/2, num_points=128, layer=0)

# Add the oval shape to the cell
cell.add(oval)

# Scale the oval to achieve the desired minor axis
scale_x = 1
scale_y = 13/20  # scaling to 13 mm minor axis
cell.add(gdspy.Polygon(oval.polygons, layer=0).scale((scale_x, scale_y)))

# Save the design to a GDS file
lib.write_gds('oval.gds')