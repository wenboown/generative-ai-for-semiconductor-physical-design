import gdspy

# Parse the user's design specifications
text = "Hello, GDS!"
x_center, y_center = 0, 0
height = 5e-3  # Convert mm to meters for gdspy
layer = 1

# Define the library and cell for the GDS layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell("Hello_GDS")

# Create the text element
text_element = gdspy.Text(text, height, (x_center, y_center), layer=layer, Center=True)

# Add the text element to the cell
cell.add(text_element)

# Save the design to a GDS file
lib.write_gds("Hello_GDS.gds")