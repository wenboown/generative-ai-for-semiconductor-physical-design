import gdspy

# Define the library and cell for the GDS layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell('Trapezoid')

# Parse the user's design specifications
upper_edge = 10  # mm
lower_edge = 20  # mm
height = 8  # mm
center_x = 0  # mm
center_y = 0  # mm

# Calculate the coordinates of the trapezoid's vertices
point1 = (center_x - (upper_edge / 2), center_y + (height / 2))
point2 = (center_x + (upper_edge / 2), center_y + (height / 2))
point3 = (center_x + (lower_edge / 2), center_y - (height / 2))
point4 = (center_x - (lower_edge / 2), center_y - (height / 2))

# Create the trapezoid polygon
trap = gdspy.Polygon([point1, point2, point3, point4])

# Add the trapezoid to the cell
cell.add(trap)

# Save the design to a GDS file
lib.write_gds('trapezoid.gds')