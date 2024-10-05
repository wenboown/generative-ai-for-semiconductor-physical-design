import gdspy

# Create a new library
lib = gdspy.GdsLibrary()

# Define the cell for the layout
cell = lib.new_cell('RECTANGLE_WITH_TEXT')

# Rectangle dimensions
width = 30000
height = 10000

# Create a rectangle on layer 0
rectangle = gdspy.Rectangle((0, 0), (width, height), layer=0)
cell.add(rectangle)

# Text properties
text_string = "IBM Research"
text_size = 2000  # Adjust text size as needed to fit within the rectangle
text_layer = 1

# Calculate text position to center it in the rectangle
bbox = gdspy.Label(text_string, (0, 0), layer=text_layer).get_bounding_box()
text_width = bbox[1][0] - bbox[0][0]
text_height = bbox[1][1] - bbox[0][1]
text_position = (width / 2 - text_width / 2, height / 2 - text_height / 2)

# Create the text label
text = gdspy.Text(text_string, text_size, position=text_position, layer=text_layer)
cell.add(text)

# Save the layout to a GDS file
lib.write_gds('rectangle_with_text.gds')

# Optionally, display the layout using the internal viewer