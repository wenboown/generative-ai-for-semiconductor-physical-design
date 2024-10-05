import gdspy
import numpy as np

# Create a new library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('TEXT_CELL')

# Define text parameters
text = "Hello, GDS!"
height = 5000  # 5 mm = 5000 µm
layer = 1

# Calculate the size of the text to center it
text_size = gdspy.Text(text, height, position=(0, 0)).get_bounding_box()
text_width = text_size[1][0] - text_size[0][0]
text_height = text_size[1][1] - text_size[0][1]

# Calculate the position to center the text at (0, 0)
position = (-text_width / 2, -text_height / 2)

# Create the text
text_elem = gdspy.Text(text, height, position=position, layer=layer)

# Add the text to the cell
cell.add(text_elem)

# Write the GDS file
lib.write_gds('hello_gds.gds')

print("GDS file 'hello_gds.gds' has been generated successfully.")