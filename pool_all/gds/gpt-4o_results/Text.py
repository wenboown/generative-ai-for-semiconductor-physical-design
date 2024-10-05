import gdspy

# Create a GDSII library
lib = gdspy.GdsLibrary()

# Create a cell for the design
cell = lib.new_cell('HELLO_GDS_TEXT')

# Define the text properties
text = "Hello, GDS!"
height = 5000  # 5 mm in micrometers
layer = 1

# Create the text geometry centered at (0, 0)
text_element = gdspy.Text(text, height, (0, 0), layer=layer)

# Calculate the bounding box of the text to center it at (0, 0)
bounding_box = text_element.get_bounding_box()
x_offset = -0.5 * (bounding_box[1][0] + bounding_box[0][0])
y_offset = -0.5 * (bounding_box[1][1] + bounding_box[0][1])
text_element.translate(x_offset, y_offset)

# Add the text element to the cell
cell.add(text_element)

# Save the layout to a GDS file
lib.write_gds('hello_gds.gds')

print("GDS file 'hello_gds.gds' has been created.")