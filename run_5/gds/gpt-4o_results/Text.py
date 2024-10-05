import gdspy

# Create a GDSII library
lib = gdspy.GdsLibrary()

# Define a cell in the library
cell = lib.new_cell('HELLO_GDS')

# Define the text and its properties
text_string = "Hello, GDS!"
text_height = 5000  # 5 mm in GDS units (1 unit = 1 nanometer)
layer = 1

# Create text at the origin (0,0) centered
text = gdspy.Text(text_string, text_height, (0, 0), horizontal=True, layer=layer)

# Get the bounding box of the text to center it at (0,0)
bbox = text.get_bounding_box()
text_center_x = (bbox[0][0] + bbox[1][0]) / 2
text_center_y = (bbox[0][1] + bbox[1][1]) / 2
text.translate(-text_center_x, -text_center_y)

# Add the text to the cell
cell.add(text)

# Write the GDSII file to disk
lib.write_gds('hello_gds.gds')

print("GDS file 'hello_gds.gds' has been created.")