import gdspy

# Create a new GDSII library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('TOP')

# Define rectangle dimensions in microns (30 mm x 10 mm)
width = 30000    # 30 mm = 30000 microns
height = 10000   # 10 mm = 10000 microns

# Create a rectangle from (0, 0) to (width, height) on layer 0
rectangle = gdspy.Rectangle((0, 0), (width, height), layer=0)
cell.add(rectangle)

# Define the text to be placed at the center
text_string = "IBM Research"

# Set the text size (height of the text)
text_height = height / 3  # Text height is one-third of the rectangle height

# Create the text at origin for initial positioning
text = gdspy.Text(text_string, size=text_height, position=(0, 0), layer=1)

# Calculate the bounding box of the text to determine its dimensions
bbox = text.get_bounding_box()
text_width = bbox[1][0] - bbox[0][0]
text_height_actual = bbox[1][1] - bbox[0][1]

# Calculate the position to center the text within the rectangle
center_x = width / 2
center_y = height / 2
text_position = (center_x - text_width / 2, center_y - text_height_actual / 2)

# Move the text to the calculated center position
text.translate(text_position[0], text_position[1])

# Add the text to the cell on layer 1
cell.add(text)

# Save the design to a GDSII file
lib.write_gds('rectangle_with_text.gds')