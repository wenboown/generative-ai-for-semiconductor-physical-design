import gdspy

# Create a new GDSII library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('HELLO_GDS')

# Define the text parameters
text_string = "Hello, GDS!"
text_height = 5000  # 5 mm in micrometers

# Create the text at position (0, 0)
text = gdspy.Text(text_string, text_height, (0, 0), layer=1)

# Get the bounding box of the text to calculate centering offset
(xmin, ymin), (xmax, ymax) = text.get_bounding_box()

# Calculate the center offset
offset_x = - (xmin + xmax) / 2
offset_y = - (ymin + ymax) / 2

# Move the text to center at (0, 0)
text.translate(offset_x, offset_y)

# Add the text to the cell
cell.add(text)

# Save the library in a GDSII file
lib.write_gds('hello_gds.gds')