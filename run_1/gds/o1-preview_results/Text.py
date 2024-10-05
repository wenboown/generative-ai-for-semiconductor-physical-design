import gdspy

# Create a new GDSII library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('HELLO_GDS')

# Define the text parameters
text_string = "Hello, GDS!"
text_size = 5000  # Height in microns (5 mm)
layer_number = 1

# Create the text at position (0, 0)
text = gdspy.Text(text_string, text_size, position=(0, 0), horizontal=True, layer=layer_number)

# Calculate the bounding box to center the text at (0, 0)
(xmin, ymin), (xmax, ymax) = text.get_bounding_box()
text_center_x = (xmin + xmax) / 2
text_center_y = (ymin + ymax) / 2

# Calculate the offset needed to center the text
offset_x = -text_center_x
offset_y = -text_center_y

# Move the text to be centered at (0, 0)
text.translate(offset_x, offset_y)

# Add the text to the cell
cell.add(text)

# Save the library in a GDSII file called 'hello_gds.gds'
lib.write_gds('hello_gds.gds')