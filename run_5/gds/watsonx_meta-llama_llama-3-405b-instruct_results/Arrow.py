import gdspy

# Define the library and cell for the GDS layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell('arrow')

# Define the arrow dimensions
arrow_length = 10  # mm
head_width = 1  # mm
body_width = head_width / 3  # mm

# Calculate the coordinates for the arrow body
body_start_x = 0
body_start_y = -body_width / 2
body_end_x = arrow_length - head_width
body_end_y = body_start_y

# Calculate the coordinates for the arrow head
head_start_x = body_end_x
head_start_y = -head_width / 2
head_end_x = arrow_length
head_end_y = 0
head_top_x = body_end_x
head_top_y = head_width / 2

# Create the arrow body as a rectangle
body = gdspy.Rectangle((body_start_x, body_start_y), (body_end_x, -body_start_y))

# Create the arrow head as a triangle (polygon)
head = gdspy.Polygon([(head_start_x, head_start_y), (head_end_x, head_end_y), (head_top_x, head_top_y)])

# Add the arrow body and head to the cell
cell.add(body)
cell.add(head)

# Save the design to a GDS file
lib.write_gds('arrow.gds')