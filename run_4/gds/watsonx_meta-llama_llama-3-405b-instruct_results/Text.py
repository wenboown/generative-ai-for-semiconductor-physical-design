import gdspy

# Parse user's design specifications
text = "Hello, GDS!"
center = (0, 0)
height = 5  # mm
layer = 1

# Define the library and cell for the GDS layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell('hello_gds')

# Create the text element with precise coordinates
text_element = gdspy.Text(text, height=height, center=center, layer=layer)

# Add the text element to the cell
cell.add(text_element)

# Save the design to a GDS file
lib.write_gds('hello_gds.gds')