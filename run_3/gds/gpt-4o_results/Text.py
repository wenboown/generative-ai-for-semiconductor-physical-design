import gdspy

# Create a new GDSII library
lib = gdspy.GdsLibrary()

# Create a cell for the text
cell = lib.new_cell('HELLO_GDS')

# Define the text, with height 5 mm, located at (0, 0), on layer 1
text = gdspy.Text("Hello, GDS!", 5000, (0, 0), layer=1)

# Center the text at (0, 0)
bounding_box = text.get_bounding_box()
x_offset = -0.5 * (bounding_box[1][0] - bounding_box[0][0])
y_offset = -0.5 * (bounding_box[1][1] - bounding_box[0][1])
text.translate(x_offset, y_offset)

# Add the text to the cell
cell.add(text)

# Save the library to a file
lib.write_gds('hello_gds.gds')

print('GDS file "hello_gds.gds" has been created.')