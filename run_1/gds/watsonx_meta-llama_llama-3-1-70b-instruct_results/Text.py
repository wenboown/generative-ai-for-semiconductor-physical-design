import gdspy

# Parse the user's design specifications
text = "Hello, GDS!"
layer = 1
x = 0
y = 0
height = 5e3  # Convert mm to um

# Define the library and cell for the GDS layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell('text_cell')

# Create the text element
text_element = gdspy.Text(text, size=height, position=(x, y), layer=layer)

# Add the text element to the cell
cell.add(text_element)

# Save the design to a GDS file
lib.write_gds('hello_gds.gds')