import gdspy

# Create a new library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('MAIN')

# Define text parameters
text = "Hello, GDS!"
height = 5000  # 5 mm = 5000 µm
layer = 1

# Create the text
text_elem = gdspy.Text(text, height, (0, 0), layer=layer)

# Get the text's bounding box
bbox = text_elem.get_bounding_box()

# Calculate the offset to center the text
offset_x = -(bbox[1][0] + bbox[0][0]) / 2
offset_y = -(bbox[1][1] + bbox[0][1]) / 2

# Move the text to center it at (0, 0)
text_elem.translate(offset_x, offset_y)

# Add the text to the cell
cell.add(text_elem)

# Write the GDS file
lib.write_gds('hello_gds.gds')

print("GDS file 'hello_gds.gds' has been created successfully.")