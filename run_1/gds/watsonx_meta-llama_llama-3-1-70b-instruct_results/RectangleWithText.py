import gdspy

# Parse the user's design specifications
rectangle_size = (30, 10)  # in mm
text_string = "IBM Research"
text_layer = 1
rectangle_layer = 0

# Define the library and cell for the GDS layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell("IBM Research Cell")

# Create a rectangle with precise coordinates
rectangle = gdspy.Rectangle((-rectangle_size[0]/2, -rectangle_size[1]/2), 
                            (rectangle_size[0]/2, rectangle_size[1]/2), 
                            layer=rectangle_layer)

# Add the rectangle to the cell
cell.add(rectangle)

# Create a text label at the center of the rectangle
text = gdspy.Text(text_string, 
                  size=1,  # in mm
                  position=(0, 0),  # at the center of the rectangle
                  layer=text_layer)

# Add the text to the cell
cell.add(text)

# Save the design to a GDS file
lib.write_gds("ibm_research_layout.gds")