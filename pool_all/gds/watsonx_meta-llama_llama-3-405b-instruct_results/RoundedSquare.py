import gdspy

# Create a new GDSII library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('ROUNDED_SQUARE')

# Define the square's dimensions and corner radius
square_size = 10.0
corner_radius = 1.0

# Define the coordinates for the square with rounded corners
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

# Create the main body of the square (without the rounded corners)
polygon = gdspy.Polygon(points)

# Create the rounded corners
corner1 = gdspy.Round((corner_radius, corner_radius), corner_radius, number_of_points=64, inner_radius=0, initial_angle=-0.5*3.141592653589793, final_angle=0)
corner2 = gdspy.Round((square_size - corner_radius, corner_radius), corner_radius, number_of_points=64, inner_radius=0, initial_angle=0, final_angle=0.5*3.141592653589793)
corner3 = gdspy.Round((square_size - corner_radius, square_size - corner_radius), corner_radius, number_of_points=64, inner_radius=0, initial_angle=0.5*3.141592653589793, final_angle=3.141592653589793)
corner4 = gdspy.Round((corner_radius, square_size - corner_radius), corner_radius, number_of_points=64, inner_radius=0, initial_angle=3.141592653589793, final_angle=1.5*3.141592653589793)

# Add all elements to the cell
cell.add(polygon)
cell.add(corner1)
cell.add(corner2)
cell.add(corner3)
cell.add(corner4)

# Save the library in a file
lib.write_gds('rounded_square.gds')