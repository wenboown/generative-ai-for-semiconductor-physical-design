import gdspy

# Define the library and cell for the GDS layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell('IBM_Research')

# Define the rectangle dimensions and position
rect_x = 0
rect_y = 0
rect_width = 30e3  # Convert 30 mm to microns
rect_height = 10e3  # Convert 10 mm to microns

# Create the rectangle on layer 0
rect = gdspy.Rectangle((rect_x, rect_y), (rect_x + rect_width, rect_y + rect_height), layer=0)
cell.add(rect)

# Define the text position at the center of the rectangle
text_x = rect_x + rect_width / 2
text_y = rect_y + rect_height / 2

# Create the text on layer 1
text = gdspy.Text("IBM Research", (text_x, text_y), layer=1)
cell.add(text)

# Save the design to a GDS file
lib.write_gds('IBM_Research.gds')