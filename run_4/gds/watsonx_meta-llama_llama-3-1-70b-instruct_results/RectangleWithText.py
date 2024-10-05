import gdspy

# Define the library and cell for the GDS layout
lib = gdspy.Library()
cell = lib.new_cell('rectangle_with_text')

# Define the rectangle dimensions
rect_width = 30
rect_height = 10

# Create the rectangle on layer 0
rectangle = gdspy.Rectangle(
    (0, 0), 
    (rect_width, rect_height), 
    layer=0
)
cell.add(rectangle)

# Calculate the text coordinates to center it within the rectangle
text_x = rect_width / 2
text_y = rect_height / 2

# Create the text on layer 1
text = gdspy.Text(
    'IBM Research', 
    (text_x, text_y), 
    1, 
    layer=1
)
cell.add(text)

# Save the design to a GDS file
lib.write_gds('rectangle_with_text.gds')