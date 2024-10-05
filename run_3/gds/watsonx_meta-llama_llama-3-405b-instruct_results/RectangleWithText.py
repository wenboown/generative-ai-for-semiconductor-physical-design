import gdspy

# Define the library and cell for the GDS layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell('IBM_Research')

# Define the rectangle on layer 0
rectangle = gdspy.Rectangle((0, 0), (30e-3, 10e-3), layer=0)
cell.add(rectangle)

# Calculate the center of the rectangle
center_x = (30e-3) / 2
center_y = (10e-3) / 2

# Define the text "IBM Research" at the center of the rectangle on layer 1
text = gdspy.Text('IBM Research', size=1e-3, position=(center_x, center_y), layer=1, anchor='center')
cell.add(text)

# Save the design to a GDS file
lib.write_gds('IBM_Research.gds')