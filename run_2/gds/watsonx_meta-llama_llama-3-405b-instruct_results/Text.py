import gdspy

# Define the library and cell for the GDS layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell('hello_gds')

# Define the text elements
text = gdspy.Text('Hello, GDS!', 5, (-12.5, 2.5), layer=1, font='standard')

# Add the text to the cell
cell.add(text)

# Save the design to a GDS file
lib.write_gds('hello_gds.gds')