import gdspy

# Create a new GDSII library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('HELLO_GDS')

# Design specifications
text_string = "Hello, GDS!"
text_height = 5000  # Height in micrometers (5 mm)
position = (0, 0)   # Initial position
layer = 1

# Create the text as polygons
text = gdspy.Text(text_string, text_height, position, layer=layer)

# Calculate the bounding box of the text
bbox = text.get_bounding_box()
text_width = bbox[1][0] - bbox[0][0]
text_height_actual = bbox[1][1] - bbox[0][1]

# Calculate offsets to center the text at (0,0)
offset_x = - (bbox[0][0] + text_width / 2)
offset_y = - (bbox[0][1] + text_height_actual / 2)

# Translate the text to center it
text.translate(offset_x, offset_y)

# Add the text to the cell
cell.add(text)

# Add the cell to the library
lib.add(cell)

# Save the design to a GDS file
lib.write_gds('hello_gds.gds')