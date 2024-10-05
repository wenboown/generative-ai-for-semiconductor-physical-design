import gdspy

# Create a new library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('TEXT_CELL')

# Define text parameters
text_content = "Hello, GDS!"
text_position = (0, 0)  # Center position
text_height = 5000  # 5 mm = 5000 µm
text_layer = 1

# Create the text
text = gdspy.Text(
    text_content,
    text_height,
    text_position,
    layer=text_layer,
    horizontal=True,
    anchor='cc'  # Center the text both horizontally and vertically
)

# Add the text to the cell
cell.add(text)

# Save the design to a GDS file
lib.write_gds('hello_gds.gds')

print("GDS file 'hello_gds.gds' has been generated successfully.")