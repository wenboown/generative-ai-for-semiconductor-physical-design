import gdspy

# Create a new GDSII library
gds_library = gdspy.GdsLibrary()

# Create a new cell
gds_cell = gds_library.new_cell('RECTANGLE_WITH_TEXT')

# Define the dimensions of the rectangle
rectangle_width = 30000  # in micrometers (30 mm)
rectangle_height = 10000  # in micrometers (10 mm)

# Create a rectangle on layer 0
rectangle = gdspy.Rectangle((0, 0), (rectangle_width, rectangle_height), layer=0)
gds_cell.add(rectangle)

# Define the position for the text (center of the rectangle)
text_position = (rectangle_width / 2, rectangle_height / 2)

# Create the text on layer 1
text = gdspy.Text('IBM Research', 2000, text_position, horizontal=True, layer=1)  # Text height set to 2000 um for visibility

# Add the text to the cell
gds_cell.add(text)

# Save the GDS layout to a file
gds_library.write_gds('rectangle_with_text.gds')

print("GDS file 'rectangle_with_text.gds' created successfully.")