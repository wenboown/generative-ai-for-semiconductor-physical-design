import gdspy

# Define the GDS library and cell
lib = gdspy.GdsLibrary()
lib добавли(new_unit='um',grid_unit=0.001)
cell = lib.new_cell('Arrow')

# Define the dimensions of the arrow
length = 10  # mm
head_width = 2  # mm (arbitrary, adjust as needed)
body_width = head_width / 3

# Calculate the coordinates for the head and body of the arrow
head_x1, head_y1 = -0.5 * head_width, -0.5 * head_width
head_x2, head_y2 = length, -0.5 * head_width
head_x3, head_y3 = length, 0.5 * head_width
head_x4, head_y4 = -0.5 * head_width, 0.5 * head_width

body_x1, body_y1 = -0.5 * body_width, -0.5 * body_width
body_x2, body_y2 = head_x1, -0.5 * body_width
body_x3, body_y3 = head_x1, 0.5 * body_width

# Create the head and body of the arrow
head = gdspy.Polygon([[head_x1, head_y1], [head_x2, head_y2], [head_x3, head_y3], [head_x4, head_y4]])
body = gdspy.Polygon([[body_x1, body_y1], [body_x2, body_y2], [body_x3, body_y3], [-0.5 * body_width, 0.5 * body_width]])

# Add the head and body to the cell
cell.add(head)
cell.add(body)

# Save the design to a GDS file
lib.write_gds('arrow.gds')