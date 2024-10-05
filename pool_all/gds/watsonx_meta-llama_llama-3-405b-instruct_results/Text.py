import gdspy

# Define the text parameters
text_string = "Hello, GDS!"
text_height = 5.0  # in mm
layer = 1

# Convert mm to microns
text_height_microns = text_height * 1000

# Create a new GDSII library and a cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('HELLO_GDS')

# Generate the text
text = gdspy.Text(text_string, text_height_microns, (0, 0), layer=layer)

# Calculate the center shift
bbox = text.get_bounding_box()
center_shift_x = (bbox[1][0] - bbox[0][0]) / 2
center_shift_y = (bbox[1][1] - bbox[0][1]) / 2

# Shift the text to be centered at (0,0)
text.translate(-center_shift_x, -center_shift_y)

# Add the text to the cell
cell.add(text)

# Save the library to a GDS file
lib.write_gds('hello_gds.gds')