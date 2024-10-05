import gdspy

# Create a new GDSII library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('HELLO_GDS')

# Define text parameters
text = "Hello, GDS!"
height = 5.0  # height in mm
position = (0, 0)  # centered at origin
layer = 1

# Add text to the cell
text_label = gdspy.Text(text, height, position, layer=layer, anchor='o')

# Ensure the text is centered
bbox = text_label.get_bounding_box()
center_shift = ((bbox[1][0] - bbox[0][0]) / 2, (bbox[1][1] - bbox[0][1]) / 2)
text_label.translate(-center_shift[0], -center_shift[1])

# Add the text label to the cell
cell.add(text_label)

# Save the library to a GDS file
lib.write_gds('hello_gds.gds')

print("GDS file 'hello_gds.gds' has been created with the text 'Hello, GDS!' centered at (0,0).")