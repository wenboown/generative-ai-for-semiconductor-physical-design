import gdspy

# Define the library and cell for the GDS layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell('trapezoid')

# Define the trapezoid's dimensions
upper_edge = 10
lower_edge = 20
height = 8
center_x = 0
center_y = 0

# Calculate the coordinates of the trapezoid
p1 = [center_x - upper_edge/2, center_y + height/2]
p2 = [center_x + upper_edge/2, center_y + height/2]
p3 = [center_x + lower_edge/2, center_y - height/2]
p4 = [center_x - lower_edge/2, center_y - height/2]

# Create the trapezoid polygon
trapezoid = gdspy.Polygon([p1, p2, p3, p4])

# Add the trapezoid to the cell
cell.add(trapezoid)

# Save the design to a GDS file
lib.write_gds('trapezoid.gds')