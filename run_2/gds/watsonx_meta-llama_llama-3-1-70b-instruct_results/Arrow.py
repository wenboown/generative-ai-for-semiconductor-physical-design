import gdspy

# Create a new GDS library
lib = gdspy.GdsLibrary()

# Create a new cell for the arrow
cell = lib.new_cell('Arrow')

# Define the coordinates for the arrow
x1, y1 = 0, 0  # starting point
length = 10  # length of the arrow
head_width = 2  # width of the head
head_length = 2  # length of the head
body_width = head_width / 3  # width of the body

# Create the arrow head
head_poly = gdspy.Polygon([(x1, y1), (x1 + head_length, y1 - head_width/2), (x1 + head_length, y1 + head_width/2)], layer=0)
cell.add(head_poly)

# Create the arrow body
body_poly = gdspy.Polygon([(x1 + head_length, y1 - body_width/2), (x1 + head_length, y1 + body_width/2),
                           (x1 + length - head_length, y1 + body_width/2), (x1 + length - head_length, y1 - body_width/2)],
                           layer=0)
cell.add(body_poly)

# Save the design to a GDS file
lib.write_gds('arrow.gds')