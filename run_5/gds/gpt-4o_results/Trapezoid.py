import gdspy

# Define the GDSII library
gdsii_lib = gdspy.GdsLibrary()

# Create a new cell
cell = gdsii_lib.new_cell("TRAPEZOID")

# Trapezoid specifications
upper_edge = 10.0  # in mm
lower_edge = 20.0  # in mm
height = 8.0       # in mm
center_x = 0.0     # center x-coordinate
center_y = 0.0     # center y-coordinate

# Compute the coordinates of the trapezoid
half_upper = upper_edge / 2.0
half_lower = lower_edge / 2.0
half_height = height / 2.0

# Trapezoid vertices
vertices = [
    (center_x - half_upper, center_y + half_height),  # Upper left
    (center_x + half_upper, center_y + half_height),  # Upper right
    (center_x + half_lower, center_y - half_height),  # Lower right
    (center_x - half_lower, center_y - half_height)   # Lower left
]

# Create the trapezoid as a polygon
trapezoid = gdspy.Polygon(vertices, layer=1)

# Add the trapezoid to the cell
cell.add(trapezoid)

# Save the layout to a GDSII file
gdsii_lib.write_gds('trapezoid.gds')

print("Trapezoid GDS layout generated successfully.")