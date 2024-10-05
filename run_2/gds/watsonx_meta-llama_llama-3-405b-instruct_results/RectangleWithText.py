import gdspy

# Define the library and cell for the GDS layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell('top')

# Define the rectangle dimensions
rect_width = 30e3  # 30 mm in microns
rect_height = 10e3  # 10 mm in microns

# Create the rectangle
rect = gdspy.Rectangle((0, 0), (rect_width, rect_height), layer=0)
cell.add(rect)

# Define the text
text = gdspy.Text("IBM Research", 1000, (rect_width/2, rect_height/2), layer=1)
cell.add(text)

# Save the design to a GDS file
lib.write_gds('example.gds')