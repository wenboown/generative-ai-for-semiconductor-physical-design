import gdspy

# Define the library and cell for the GDS layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell('HelloGDS')

# Create a text element with the specified properties
text = gdspy.Text('Hello, GDS!', 5, (0, 0), layer=1, font='Roman')

# Add the text element to the cell
cell.add(text)

# Save the design to a GDS file
lib.write_gds('HelloGDS.gds')