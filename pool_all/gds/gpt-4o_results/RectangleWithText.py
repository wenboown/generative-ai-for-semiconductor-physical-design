import gdspy

# Create a new GDSII library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('RECTANGLE_WITH_TEXT')

# Define rectangle (30mm x 10mm)
rectangle = gdspy.Rectangle((0, 0), (30000, 10000), layer=0)
cell.add(rectangle)

# Define and position the text at the center of the rectangle
text_size = 2000  # Adjust this value to change text size
text_string = "IBM Research"
text_position = (15000 - (len(text_string) * text_size / 4), 5000 - text_size / 2)  # Rough adjustment for centering
text = gdspy.Text(text_string, text_size=text_size, position=text_position, layer=1)
cell.add(text)

# Save the design to a GDS file
lib.write_gds('rectangle_with_text.gds')