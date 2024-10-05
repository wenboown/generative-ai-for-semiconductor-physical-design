import gdspy

# Define the library and cell for the GDS layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell('trapezoid')

# Define the trapezoid parameters
upper_edge = 10e-3  # Convert mm to meters (GDSII default unit)
lower_edge = 20e-3  # Convert mm to meters (GDSII default unit)
height = 8e-3      # Convert mm to meters (GDSII default unit)
center_x, center_y = 0, 0

# Calculate the trapezoid coordinates
x1 = center_x - upper_edge / 2
x2 = center_x + upper_edge / 2
x3 = center_x + lower_edge / 2
x4 = center_x - lower_edge / 2
y1 = center_y + height / 2
y2 = center_y - height / 2

# Create the trapezoid as a polygon
trapezoid = gdspy.Polygon([(x1, y1), (x2, y1), (x3, y2), (x4, y2)])

# Add the trapezoid to the cell
cell.add(trapezoid)

# Save the design to a GDS file
lib.write_gds('trapezoid.gds')