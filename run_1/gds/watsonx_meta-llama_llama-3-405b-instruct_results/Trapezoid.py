import gdspy

# Define the library and cell for the GDS layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell('trapezoid')

# Define the trapezoid parameters
upper_edge = 10
lower_edge = 20
height = 8
center = (0, 0)

# Calculate the trapezoid coordinates
upper_left = (center[0] - upper_edge / 2, center[1] + height / 2)
upper_right = (center[0] + upper_edge / 2, center[1] + height / 2)
lower_left = (center[0] - lower_edge / 2, center[1] - height / 2)
lower_right = (center[0] + lower_edge / 2, center[1] - height / 2)

# Create the trapezoid as a polygon
trap = gdspy.Polygon([upper_left, upper_right, lower_right, lower_left])

# Add the trapezoid to the cell
cell.add(trap)

# Save the design to a GDS file
lib.write_gds('trapezoid.gds')