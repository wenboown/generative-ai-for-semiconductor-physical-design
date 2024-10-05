import gdspy

# Create a new GDSII library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('IBM_RESEARCH')

# Rectangle dimensions in micrometers (1 mm = 1000 um)
rect_width = 30000  # 30 mm
rect_height = 10000  # 10 mm

# Create the rectangle on layer 0 from (0, 0) to (rect_width, rect_height)
rectangle = gdspy.Rectangle((0, 0), (rect_width, rect_height), layer=0)

# Add the rectangle to the cell
cell.add(rectangle)

# Text content
text_content = 'IBM Research'

# Text parameters
text_size = 2000  # Text height in um
text_layer = 1

# Create the text at position (0, 0) to calculate its size
text = gdspy.Text(text_content, text_size, position=(0, 0), layer=text_layer)

# Get the bounding box of the text
bbox = text.get_bounding_box()

# Calculate the width and height of the text
text_width = bbox[1][0] - bbox[0][0]
text_height = bbox[1][1] - bbox[0][1]

# Calculate the position to center the text
text_x = (rect_width - text_width) / 2
text_y = (rect_height - text_height) / 2

# Create the text at the centered position
text = gdspy.Text(text_content, text_size, position=(text_x, text_y), layer=text_layer)

# Add the text to the cell
cell.add(text)

# Save the GDS file
lib.write_gds('ibm_research.gds')