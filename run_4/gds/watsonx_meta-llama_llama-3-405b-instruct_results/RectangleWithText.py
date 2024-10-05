import gdspy

# Define the library and cell for the GDS layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell('IBM_Research')

# Define the rectangle
rect = gdspy.Rectangle((0, 0), (30e3, 10e3), layer=0)
cell.add(rect)

# Define the text
text = gdspy.Text('IBM Research', 500, (15e3, 5e3), layer=1)
cell.add(text)

# Save the design to a GDS file
lib.gdsii.write_gds('IBM_Research.gds')