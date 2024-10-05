import gdspy

# Define the library and cell for the GDS layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell('Trapezoid')

# Define the dimensions of the trapezoid
upper_edge = 10
lower_edge = 20
height = 8
center_x, center_y = 0, 0

# Calculate the coordinates of the trapezoid vertices
x1 = center_x - upper_edge / 2
y1 = center_y + height / 2
x2 = center_x + upper_edge / 2
y2 = center_y + height / 2
x3 = center_x + lower_edge / 2
y3 = center_y - height / 2
x4 = center_x - lower_edge / 2
y4 = center_y - height / 2

# Create the trapezoid as a polygon
trap = gdspy.Polygon([(x1, y1), (x2, y2), (x3, y3), (x4, y4)], layer=0, datatype=0)

# Add the trapezoid to the cell
cell.add(trap)

# Save the design to a GDS file
lib.write_gds('trapezoid.gds')