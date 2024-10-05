import gdspy

# Define the library and cell for the GDS layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell('IBM_Research_Cell')

# Parse the user's design specifications and create the rectangle
rectangle = gdspy.Rectangle(
    (0, -5), (30, 5), 
    layer = 0
)

# Add the rectangle to the cell
cell.add(rectangle)

# Create the text at the center of the rectangle
text = gdspy.Text(
    'IBM Research', 
    10, 
    (15, 0), 
    layer = 1
)

# Add the text to the cell
cell.add(text)

# Save the design to a GDS file
lib.write_gds('IBM_Research.gds')