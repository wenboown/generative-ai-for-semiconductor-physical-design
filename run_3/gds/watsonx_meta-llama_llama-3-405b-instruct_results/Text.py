import gdspy

# Parse the user's design specifications
text = "Hello, GDS!"
center = (0, 0)
height = 5  # in mm
layer = 1

# Define the library and cell for the GDS layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell('Hello_GDS')

# Create the text element with precise coordinates
text_path = gdspy.Path(layer=layer)
text_path.text(text, height, position=center, fontname='standard', horizontal=True)

# Add the text element to the cell
cell.add(text_path)

# Save the design to a GDS file
lib.write_gds('hello_gds.gds')