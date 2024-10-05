import gdspy

# Constants
text_string = "Hello, GDS!"
text_height = 5.0  # Text height in mm
layer = 1  # Layer number

# Convert mm to microns (1 mm = 1000 microns)
text_height_microns = text_height * 1000

# Create a new library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('TEXT_CELL')

# Generate the text
text = gdspy.Text(text_string, text_height_microns, (0, 0), layer=layer, horizontal=True)

# Calculate the center shift
bounding_box = text.get_bounding_box()
center_shift_x = (bounding_box[1][0] - bounding_box[0][0]) / 2
center_shift_y = (bounding_box[1][1] - bounding_box[0][1]) / 2

# Shift the text to be centered at (0,0)
text.translate(-center_shift_x, -center_shift_y)

# Add the text to the cell
cell.add(text)

# Save the GDS file
lib.write_gds('hello_gds.gds')

# Optionally, you can view the created GDS file using a suitable GDS viewer here
print("GDS file 'hello_gds.gds' with text 'Hello, GDS!' has been created.")