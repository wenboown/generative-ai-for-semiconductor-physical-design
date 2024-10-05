import gdspy

# Initialize the GDSII library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('TRAPEZOID')

# Define the dimensions of the trapezoid
upper_edge = 10.0   # Upper edge length in mm
lower_edge = 20.0   # Lower edge length in mm
height = 8.0       # Height of the trapezoid in mm

# Compute half-lengths for ease of placement
half_upper_edge = upper_edge / 2.0
half_lower_edge = lower_edge / 2.0

# Define the coordinates of the trapezoid vertices
# Upper vertices (centered at origin, so left and right on the top edge)
upper_left = [-half_upper_edge, height / 2]
upper_right = [half_upper_edge, height / 2]

# Lower vertices (centered at origin, so left and right on the bottom edge)
lower_left = [-half_lower_edge, -height / 2]
lower_right = [half_lower_edge, -height / 2]

# List of vertices in order
vertices = [upper_left, upper_right, lower_right, lower_left]

# Create the trapezoid as a polygon
trapezoid = gdspy.Polygon(vertices)

# Add the polygon to the cell
cell.add(trapezoid)

# Save the library to a GDSII file
lib.write_gds('trapezoid.gds')

print("Trapezoid GDS file 'trapezoid.gds' created successfully.")