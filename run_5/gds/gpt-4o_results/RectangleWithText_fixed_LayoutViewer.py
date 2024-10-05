import gdspy

# Create a GDSII library, which will contain the layout.
lib = gdspy.GdsLibrary()

# Create a new cell.
cell = lib.new_cell('RECTANGLE_WITH_TEXT')

# Define the rectangle dimensions and coordinates.
width = 30000.0  # 30 mm in microns
height = 10000.0  # 10 mm in microns

# Create a rectangle on layer 0.
rectangle = gdspy.Rectangle((0, 0), (width, height), layer=0)
cell.add(rectangle)

# Define the text to be added and its coordinates.
text = "IBM Research"
text_position = (width / 2, height / 2)  # Center of the rectangle
text_size = 2000  # Size of the text

# Create the text on layer 1.
text_element = gdspy.Text(text, text_size, position=text_position, layer=1, anchor='cc')
cell.add(text_element)

# Save the layout to a GDSII file.
lib.write_gds('rectangle_with_text.gds')

# Optionally, you can view the layout using an external tool.