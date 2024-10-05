import gdspy

# Create a GDSII library
library = gdspy.GdsLibrary()

# Create a new cell in the library
cell = library.new_cell('RECTANGLE_WITH_TEXT')

# Create a rectangle of 30 mm x 10 mm on layer 0
rectangle = gdspy.Rectangle((0, 0), (30000, 10000), layer=0)
cell.add(rectangle)

# Create text "IBM Research" at the center of the rectangle
text = gdspy.Text('IBM Research', 500, (15000, 5000), horizontal=True, layer=1)
cell.add(text)

# Write the cell to a GDSII file
library.write_gds('rectangle_with_text.gds')

# Optionally, visualize using gdspy's internal viewer (if you are running in an environment that supports it)