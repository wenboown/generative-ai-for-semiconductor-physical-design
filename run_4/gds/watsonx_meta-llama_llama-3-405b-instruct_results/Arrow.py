import gdspy

# Define the design specifications
head_length = 3  # 1/3 of total length for the head
body_length = 7  # 2/3 of total length for the body
head_width = 2   # width of the head
body_width = head_width / 3  # width of the body

# Create a new GDS library and add a cell for the arrow
lib = gdspy.GdsLibrary()
cell = lib.new_cell('arrow')

# Create the head of the arrow
head = gdspy.Rectangle((-head_width/2, 0), (head_width/2, head_length))
cell.add(head)

# Create the body of the arrow
body = gdspy.Rectangle((-body_width/2, head_length), (body_width/2, head_length + body_length))
cell.add(body)

# Save the design to a GDS file
lib.write_gds('arrow.gds')