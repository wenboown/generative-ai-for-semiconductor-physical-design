import gdspy

# Define the library and cell for the GDS layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell("Circle")

# Define the circle with precise coordinates
circle = gdspy.Round((0, 0), 10, layer=0)

# Add the circle to the cell
cell.add(circle)

# Save the design to a GDS file
lib.write_gds('circle.gds')