import gdspy

# Define the GDS library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('Arrow')

# Parse the user's design specifications
length = 10  # mm
headWidth = 1  # mm (assuming 1 mm head width)
bodyWidth = headWidth / 3  # mm

# Calculate coordinates for the head
head_start_x = length - headWidth
head_start_y = -headWidth / 2
head_end_x = length
head_end_y = headWidth / 2

# Calculate coordinates for the body
body_start_x = 0
body_start_y = -bodyWidth / 2
body_end_x = head_start_x
body_end_y = bodyWidth / 2

# Create each geometric element with precise coordinates
head = gdspy.Polygon([(head_start_x, head_start_y), (head_end_x, 0), (head_start_x, head_end_y)], layer=1)
body = gdspy.Rectangle((body_start_x, body_start_y), (body_end_x, body_end_y), layer=1)

# Add the head and body to the cell
cell.add(head)
cell.add(body)

# Save the design to a GDS file
lib.write_gds('arrow.gds')