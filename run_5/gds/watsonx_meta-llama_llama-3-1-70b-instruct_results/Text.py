import gdspy

# Parse the user's design specifications
text = "Hello, GDS!"
layer = 1
height = 5e6  # 5 mm in micrometers
x = 0
y = 0

# Define the library and cell for the GDS layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell('text_cell')

# Create the text with precise coordinates
text_element = gdspy.Text(text, height, (x, y), layer=layer)

# Add the text element to the cell
cell.add(text_element)

# Save the design to a GDS file
lib.write_gds('hello_gds.gds')