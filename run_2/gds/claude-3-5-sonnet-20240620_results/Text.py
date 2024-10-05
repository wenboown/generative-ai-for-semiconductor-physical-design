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

# Create the text
text_elem = gdspy.Text(
    text,
    height,
    (0, 0),
    layer=layer,
    horizontal=True,
    anchor="cc"  # Center the text both horizontally and vertically
)

# Add the text to the cell
cell.add(text_elem)

# Write the GDS file
lib.write_gds('hello_gds.gds')

print("GDS file 'hello_gds.gds' has been generated successfully.")