import gdspy

# Define the library and cell for the GDS layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell('Arrow')

# Define the dimensions
length = 10  # mm
head_width = 2  # mm (assuming 2mm head width, adjust according to design specs)
body_width = head_width / 3  # mm

# Calculate the coordinates for the arrow body
body_x1, body_y1 = 0, -body_width/2
body_x2, body_y2 = length * 2/3, -body_width/2
body_x3, body_y3 = length * 2/3, body_width/2
body_x4, body_y4 = 0, body_width/2

# Create the arrow body rectangle
arrow_body = gdspy.Rectangle((body_x1, body_y1), (body_x4, body_y4))
cell.add(arrow_body)

# Calculate the coordinates for the arrow head
head_x1, head_y1 = length * 2/3, body_width/2
head_x2, head_y2 = length, body_width
head_x3, head_y3 = length * 2/3, body_width/2 + head_width
head_x4, head_y4 = length * 2/3 - head_width, body_width/2

# Create the arrow head polygon
arrow_head = gdspy.Polygon([(head_x1, head_y1), (head_x2, head_y2), (head_x3, head_y3), (head_x4, head_y4)])
cell.add(arrow_head)

# Save the design to a GDS file
lib.write_gds('arrow.gds')