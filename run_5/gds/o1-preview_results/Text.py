import gdspy

# Create a new GDSII library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('TEXT_CELL')

# Define the text parameters
text = 'Hello, GDS!'
height = 5000  # Height in micrometers (5 mm)

# Create the text at origin first
text_element = gdspy.Text(text, height, (0, 0), layer=1)

# Calculate the bounding box to find the size of the text
bbox = text_element.get_bounding_box()
text_width = bbox[1][0] - bbox[0][0]
text_height = bbox[1][1] - bbox[0][1]

# Calculate the shift needed to center the text at (0, 0)
dx = - (bbox[0][0] + text_width / 2)
dy = - (bbox[0][1] + text_height / 2)

# Create the text centered at (0, 0)
text_element = gdspy.Text(text, height, (dx, dy), layer=1)

# Add the text to the cell
cell.add(text_element)

# Write the GDS file
lib.write_gds('hello_gds.gds')