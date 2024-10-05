import gdspy

# Define the arrow dimensions
arrow_length = 10e3  # 10 mm in micrometers
head_width = 2e3  # 2 mm in micrometers
body_width = head_width / 3  # body width is 1/3 of the head width
head_length = head_width  # assuming head length is equal to head width

# Calculate the coordinates for the arrow body
body_start_x = 0
body_start_y = -body_width / 2
body_end_x = arrow_length - head_length
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

# Create a new GDS library and add a cell for the arrow
lib = gdspy.GdsLibrary()
cell = lib.new_cell('arrow')

# Add the arrow body and head to the cell
cell.add(body)
cell.add(head)

# Save the design to a GDS file
lib.write_gds('arrow.gds')