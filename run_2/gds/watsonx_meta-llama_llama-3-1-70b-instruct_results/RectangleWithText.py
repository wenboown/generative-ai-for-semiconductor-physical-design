import gdspy

# Define the library and cell for the GDS layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell('ibm_research_layout')

# Define the rectangle dimensions and coordinates
rect_width = 30e3  # 30 mm to micron conversion
rect_height = 10e3  # 10 mm to micron conversion
rect_x = -rect_width/2
rect_y = -rect_height/2

# Create the rectangle on layer 0
rect = gdspy.Rectangle((rect_x, rect_y), (rect_x + rect_width, rect_y + rect_height), layer=0)
cell.add(rect)

# Define the text properties
text_string = 'IBM Research'
text_layer = 1
text_size = 5e3  # 5 mm to micron conversion
text_x = -text_size * len(text_string) / 4
text_y = -text_size / 2 + rect_y + rect_height/2

# Create the text on layer 1
text = gdspy.Text(text_string, (text_x, text_y), size=text_size, layer=text_layer, font='ROMAN')
cell.add(text)

# Save the design to a GDS file
lib.write_gds('ibm_research_layout.gds')