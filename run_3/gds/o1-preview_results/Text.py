import gdspy

# Create a new GDSII library with units in millimeters (mm)
lib = gdspy.GdsLibrary(unit=1e-3, precision=1e-6)

# Create a new cell
cell = lib.new_cell('TEXT_CELL')

# Create the text "Hello, GDS!" with a height of 5 mm at position (0, 0) on layer 1
text_polygons = gdspy.Text('Hello, GDS!', 5, position=(0, 0), layer=1)

# Get the bounding box of the text polygons
bbox = text_polygons.get_bounding_box()

# Calculate the center of the bounding box
center_x = (bbox[0][0] + bbox[1][0]) / 2
center_y = (bbox[0][1] + bbox[1][1]) / 2

# Translate the text polygons to center at (0, 0)
text_polygons = gdspy.translate(text_polygons, -center_x, -center_y)

# Add the text polygons to the cell
cell.add(text_polygons)

# Write the GDS file
lib.write_gds('hello_gds.gds')