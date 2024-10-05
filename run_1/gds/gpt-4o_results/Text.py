import gdspy

# Create a GDSII library
lib = gdspy.GdsLibrary()

# Create a cell for the design
cell = lib.new_cell("HELLO_GDS_TEXT")

# Define the text properties
text = "Hello, GDS!"
height = 5.0  # Text height in mm
layer = 1

# Create the text geometry centered at (0, 0)
text_element = gdspy.Text(text, height, (0, 0), horizontal=True, vertical='center', layer=layer)

# Add the text element to the cell
cell.add(text_element)

# Save the layout
lib.write_gds('hello_gds.gds')

print("GDS file 'hello_gds.gds' with text has been created.")