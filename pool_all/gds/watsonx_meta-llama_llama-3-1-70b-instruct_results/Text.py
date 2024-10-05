import gdspy

# Create a new library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('TEXT_CELL')

# Define text parameters
text = "Hello, GDS!"
text_height = 5000  # 5 mm = 5000 μm
layer = 1

# Create the text
text_element = gdspy.Text(text, text_height, (0, 0), layer=layer)

# Get the bounding box of the text to center it at (0,0)
bbox = text_element.get_bounding_box()
x_offset = -0.5 * abs(bbox[1][0] - bbox[0][0])
y_offset = -0.5 * abs(bbox[1][1] - bbox[0][1])

# Shift the text to be centered at (0,0)
text_element.translate(x_offset, y_offset)

# Add the text to the cell
cell.add(text_element)

# Save the design to a GDS file
lib.write_gds('hello_gds.gds')

print("GDS file 'hello_gds.gds' has been generated successfully.")