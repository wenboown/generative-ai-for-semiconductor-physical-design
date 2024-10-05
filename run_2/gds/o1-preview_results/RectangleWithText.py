import gdspy

# Create a new GDSII library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('CELL')

# Define the rectangle (30 mm x 10 mm) on layer 0
rectangle = gdspy.Rectangle((0, 0), (30000, 10000), layer=0)
cell.add(rectangle)

# Define the text "IBM Research" at the center of the rectangle on layer 1
text = gdspy.Text(
    'IBM Research',
    size=2000,
    position=(15000, 5000),
    horizontal='center',
    vertical='center',
    layer=1
)
cell.add(text)

# Write the GDSII file
lib.write_gds('output.gds')