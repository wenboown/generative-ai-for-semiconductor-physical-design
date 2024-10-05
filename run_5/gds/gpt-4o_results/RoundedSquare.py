import gdspy

# Create a new GDSII library, name it 'library1'.
lib = gdspy.GdsLibrary()

# Create a new cell named 'FIRST'.
cell = lib.new_cell('FIRST')

# Parameters for the main square
square_size = 10.0  # size of the square
corner_radius = 1.0  # radius for the rounded corners

# Helper function to create a rounded corner
def create_rounded_corner(center, radius, start_angle, end_angle):
    """ Helper function to create a rounded corner
    center: a tuple (x, y) that represents the center of the arc
    radius: the radius of the arc
    start_angle: the starting angle of the arc in degrees
    end_angle: the ending angle of the arc in degrees
    """
    return gdspy.Round(center, radius, initial_angle=start_angle, final_angle=end_angle, number_of_points=64)

# Define the four corners with rounding
corners = [
    create_rounded_corner((corner_radius, corner_radius), corner_radius, 180, 270),  # Bottom-left
    create_rounded_corner((square_size - corner_radius, corner_radius), corner_radius, 270, 360),  # Bottom-right
    create_rounded_corner((square_size - corner_radius, square_size - corner_radius), corner_radius, 0, 90),  # Top-right
    create_rounded_corner((corner_radius, square_size - corner_radius), corner_radius, 90, 180)  # Top-left
]

# Create the main body of the square without the corners
body = gdspy.Rectangle(
    (corner_radius, 0),
    (square_size - corner_radius, square_size)
)
body = gdspy.boolean(
    body,
    gdspy.Rectangle(
        (0, corner_radius),
        (square_size, square_size - corner_radius)
    ),
    'or'
)

# Combine the body with the rounded corners
total_area = gdspy.boolean(
    body,
    corners[0],
    'or'
)
for corner in corners[1:]:
    total_area = gdspy.boolean(
        total_area,
        corner,
        'or'
    )

# Add the final shape to the cell
cell.add(total_area)

# Save the library in a file called 'rounded_square.gds'.
lib.write_gds('rounded_square.gds')