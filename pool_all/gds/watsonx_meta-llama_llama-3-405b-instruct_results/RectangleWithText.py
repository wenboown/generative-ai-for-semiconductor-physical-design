import gdspy

# Define the library and cell for the GDS layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell('IBM_Research')

# Define the rectangle dimensions
rect_width = 30e3  # Convert 30 mm to microns
rect_height = 10e3  # Convert 10 mm to microns

# Create the rectangle on layer 0
rect = gdspy.Rectangle((0, 0), (rect_width, rect_height), layer=0)
cell.add(rect)

# Define the text
text = "IBM Research"
text_size = 1000  # Text size in microns
text_position = (rect_width / 2, rect_height / 2)  # Center of the rectangle

# Create the text on layer 1
text = gdspy.Text(text, text_size, text_position, layer=1)
cell.add(text)

# Save the design to a GDS file
lib.write_gds('ibm_research.gds')