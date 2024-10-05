import gdspy

# Parse the user's design specifications
text = "Hello, GDS!"
center = (0, 0)
height = 5  # mm
layer = 1

# Define the library and cell for the GDS layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell('text_cell')

# Create the text element
gdspy.current_library = lib
gdspy.default_layer = layer
gdspy.default_datatype = 0
text_element = gdspy.Text(text, center, size=height, align='center')

# Add the text element to the cell
cell.add(text_element)

# Save the design to a GDS file
lib.write_gds('hello_gds.gds')