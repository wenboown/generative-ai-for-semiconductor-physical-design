import gdspy

# Create a GDSII library
lib = gdspy.GdsLibrary()

# Create a cell
cell = lib.new_cell('TOP')

# Define rectangle dimensions (in micrometers, since GDSII units are typically in microns)
width = 30000  # 30 mm
height = 10000  # 10 mm

# Create a rectangle on layer 0
rectangle = gdspy.Rectangle((0, 0), (width, height), layer=0)
cell.add(rectangle)

# Calculate the center of the rectangle
center_x = width / 2
center_y = height / 2

# Define text properties
text_string = "IBM Research"
text_size = 2000  # Size of the text
text_layer = 1

# Create the text at an initial position
text = gdspy.Text(text_string, text_size, position=(0, 0), layer=text_layer)

# Get the bounding box of the text to calculate its dimensions
text_bbox = text.get_bounding_box()
text_width = text_bbox[1][0] - text_bbox[0][0]
text_height = text_bbox[1][1] - text_bbox[0][1]

# Calculate the position to center the text within the rectangle
text_position_x = center_x - text_width / 2
text_position_y = center_y - text_height / 2

# Move the text to the calculated position
text.translate(text_position_x, text_position_y)

# Add the text to the cell
cell.add(text)

# Write the GDSII file
lib.write_gds('layout.gds')