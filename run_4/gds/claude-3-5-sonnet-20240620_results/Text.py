import gdspy
import numpy as np

# Create a new library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('MAIN')

# Define text parameters
text = "Hello, GDS!"
height = 5000  # 5 mm in um
layer = 1

# Calculate the text size and position
text_size = gdspy.text(text, height, position=(0, 0))
text_width = text_size[1][0] - text_size[0][0]
text_height = text_size[1][1] - text_size[0][1]

# Calculate the center position
center_x = -text_width / 2
center_y = -text_height / 2

# Create the text
text_poly = gdspy.text(text, height, position=(center_x, center_y), layer=layer)

# Add the text to the cell
cell.add(text_poly)

# Write the GDS file
lib.write_gds('hello_gds.gds')

print("GDS file 'hello_gds.gds' has been created successfully.")