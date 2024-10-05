import gdspy

# Create a new GDSII library
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
text_position = (width / 2, height / 2)

# Create the text label
text = gdspy.Text(text_string, text_size, text_position, layer=text_layer)
cell.add(text)

# Save the layout to a GDS file
lib.write_gds('rectangle_with_text.gds')