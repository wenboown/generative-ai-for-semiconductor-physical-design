import gdspy

# Create a new GDSII library
lib = gdspy.GdsLibrary()

# Define the name of the cell
cell = lib.new_cell('RECTANGLE_WITH_TEXT')

# Define the dimensions of the rectangle
rectangle_width = 30000  # 30 mm in microns
rectangle_height = 10000  # 10 mm in microns

# Create a rectangle
rectangle = gdspy.Rectangle((0, 0), (rectangle_width, rectangle_height), layer=0)

# Add rectangle to the cell
cell.add(rectangle)

# Define the text and its position at the center of the rectangle
text = "IBM Research"
text_x = rectangle_width / 2
text_y = rectangle_height / 2

# Create the text (text is usually quite small, so we scale it up)
text_label = gdspy.Text(text, 2000, position=(text_x, text_y), layer=1, anchor='cc')

# Add text to the cell
cell.add(text_label)

# Save the library as a GDS file
lib.write_gds('rectangle_with_text.gds')

# Optionally, view layout using the viewer provided by gdspy