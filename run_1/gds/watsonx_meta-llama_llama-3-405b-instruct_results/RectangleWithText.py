import gdspy

# Define the library and cell for the GDS layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell('IBM_Research')

# Create the rectangle on layer 0
rectangle = gdspy.Rectangle((0, 0), (30e-3, 10e-3), layer=0)
cell.add(rectangle)

# Calculate the center of the rectangle for text placement
center_x = 15e-3
center_y = 5e-3

# Create the text "IBM Research" at the center of the rectangle on layer 1
text = gdspy.Text('IBM Research', size=1e-3, position=(center_x, center_y), layer=1)
cell.add(text)

# Save the design to a GDS file
lib.write_gds('ibm_research.gds')