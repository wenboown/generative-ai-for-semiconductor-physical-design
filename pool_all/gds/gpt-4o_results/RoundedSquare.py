import gdspy

# Create a new GDSII library
lib = gdspy.GdsLibrary()

# Create a cell for our design
cell = lib.new_cell('SQUARE_WITH_ROUNDED_CORNERS')

# Define parameters in micrometers (1 mm = 1000 μm)
width = 10000  # 10 mm
corner_radius = 1000  # 1 mm

# Define points for the square with rounded corners
points = [
    (corner_radius, 0),
    (width - corner_radius, 0),
    (width, corner_radius),
    (width, width - corner_radius),
    (width - corner_radius, width),
    (corner_radius, width),
    (0, width - corner_radius),
    (0, corner_radius)
]

# Create the main polygon without rounded corners
polygon = gdspy.Polygon(points)

# Create arcs for each corner
corner_1 = gdspy.Round((corner_radius, corner_radius), corner_radius, inner_radius=0, initial_angle=1.5 * gdspy.pi, final_angle=2.0 * gdspy.pi)
corner_2 = gdspy.Round((width - corner_radius, corner_radius), corner_radius, inner_radius=0, initial_angle=0, final_angle=0.5 * gdspy.pi)
corner_3 = gdspy.Round((width - corner_radius, width - corner_radius), corner_radius, inner_radius=0, initial_angle=0.5 * gdspy.pi, final_angle=gdspy.pi)
corner_4 = gdspy.Round((corner_radius, width - corner_radius), corner_radius, inner_radius=0, initial_angle=gdspy.pi, final_angle=1.5 * gdspy.pi)

# Use a boolean operation to combine the polygon and the corners
rounded_square = gdspy.boolean(polygon, [corner_1, corner_2, corner_3, corner_4], 'or')

# Add the final shape to the cell
cell.add(rounded_square)

# Write the layout to a GDSII file
lib.write_gds('rounded_square.gds')