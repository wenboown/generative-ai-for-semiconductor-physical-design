import gdspy

# Define the GDS library and cell
gds_lib = gdspy.Library()
gds_cell = gds_lib.new_cell('Trapezoid')

# Define the geometric parameters
upper_edge = 10
lower_edge = 20
height = 8
center_x = 0
center_y = 0

# Calculate the x-coordinates of the trapezoid's vertices
x1 = center_x - (upper_edge / 2)
x2 = center_x + (upper_edge / 2)
x3 = center_x + (lower_edge / 2)
x4 = center_x - (lower_edge / 2)

# Calculate the y-coordinates of the trapezoid's vertices
y1 = center_y + (height / 2)
y2 = center_y + (height / 2)
y3 = center_y - (height / 2)
y4 = center_y - (height / 2)

# Create the trapezoid's vertices
vertices = [(x1, y1), (x2, y2), (x3, y3), (x4, y4)]

# Create the trapezoid polygon
trapezoid = gdspy.Polygon(vertices, 1)

# Add the trapezoid to the cell
gds_cell.add(trapezoid)

# Save the GDS layout
gds_lib.write_gds('trapezoid.gds')