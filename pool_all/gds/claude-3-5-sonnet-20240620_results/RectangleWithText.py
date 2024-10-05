import gdspy

# Create a new library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('RECTANGLE_WITH_TEXT')

# Define rectangle dimensions (in micrometers)
width = 30000  # 30 mm
height = 10000  # 10 mm

# Create rectangle on layer 0
rectangle = gdspy.Rectangle((0, 0), (width, height), layer=0)
cell.add(rectangle)

# Create text "IBM Research" at the center of the rectangle on layer 1
text = "IBM Research"
text_size = 1000  # Adjust this value to change text size
text_position = (width / 2, height / 2)

text_element = gdspy.Text(text, text_size, text_position, layer=1)
cell.add(text_element)

# Save the design to a GDS file
lib.write_gds('rectangle_with_text.gds')

print("GDS file 'rectangle_with_text.gds' has been generated successfully.")