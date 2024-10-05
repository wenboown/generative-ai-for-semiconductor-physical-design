import gdspy

# Create a new GDSII library
lib = gdspy.GdsLibrary()

# Define the cell for our layout
cell = lib.new_cell('SQUARE_WITH_ROUNDED_CORNERS')

# Define the size of the square and radius for corner rounding
square_size = 10.0
corner_radius = 1.0

# Define the main square as a polygon with rounded corners
points = [
    (corner_radius, 0),
    (square_size - corner_radius, 0),
    (square_size, corner_radius),
    (square_size, square_size - corner_radius),
    (square_size - corner_radius, square_size),
    (corner_radius, square_size),
    (0, square_size - corner_radius),
    (0, corner_radius)
]

# Create arcs for each corner
corner_1 = gdspy.Round((corner_radius, corner_radius), corner_radius, inner_radius=0, initial_angle=1.5 * 3.141592653589793, final_angle=2 * 3.141592653589793)
corner_2 = gdspy.Round((square_size - corner_radius, corner_radius), corner_radius, inner_radius=0, initial_angle=0, final_angle=0.5 * 3.141592653589793)
corner_3 = gdspy.Round((square_size - corner_radius, square_size - corner_radius), corner_radius, inner_radius=0, initial_angle=0.5 * 3.141592653589793, final_angle=3.141592653589793)
corner_4 = gdspy.Round((corner_radius, square_size - corner_radius), corner_radius, inner_radius=0, initial_angle=3.141592653589793, final_angle=1.5 * 3.141592653589793)

# Combine the main polygon and the corners
polygon = gdspy.Polygon(points)
polygon_with_corners = gdspy.boolean(polygon, [corner_1, corner_2, corner_3, corner_4], 'or')

# Add the structure to the cell
cell.add(polygon_with_corners)

# Write the GDSII file
lib.write_gds('rounded_square.gds')

# Optional: Visualize the result using gdspy's internal viewer