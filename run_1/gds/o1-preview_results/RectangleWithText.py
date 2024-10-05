import gdspy

# Create a new GDSII library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('IBM_RESEARCH_CELL')

# Define the rectangle dimensions in micrometers (since default units are micrometers)
rect_width = 30000  # 30 mm = 30000 µm
rect_height = 10000  # 10 mm = 10000 µm

# Create the rectangle from (0, 0) to (rect_width, rect_height) on layer 0
rectangle = gdspy.Rectangle((0, 0), (rect_width, rect_height), layer=0)

# Add the rectangle to the cell
cell.add(rectangle)

# Define the text
text_string = "IBM Research"
text_size = 2000  # Text size in micrometers, adjust as needed

# Define the position at the center of the rectangle
rect_center = (rect_width / 2, rect_height / 2)

# Create the text centered at rect_center using anchor 'cc' (center-center) on layer 1
text = gdspy.Text(text_string, text_size, position=rect_center, anchor='cc', layer=1)

# Add the text to the cell
cell.add(text)

# Save the GDSII file
lib.write_gds('ibm_research.gds')