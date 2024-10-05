import gdspy
import numpy as np

# Create a new library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('MAIN')

# Define the square dimensions
width = 10000  # 10 mm in nanometers
height = 10000  # 10 mm in nanometers

# Define the corner radius
corner_radius = 1000  # 1 mm in nanometers

# Create the main square
square = gdspy.Rectangle((0, 0), (width, height))

# Create rounded corners
corner_positions = [
    (0, 0),  # Bottom-left
    (width, 0),  # Bottom-right
    (width, height),  # Top-right
    (0, height)  # Top-left
]

rounded_corners = gdspy.boolean(
    gdspy.Round(
        (corner_positions[0][0], corner_positions[0][1]),
        corner_radius,
        number_of_points=32,
        layer=0
    ),
    gdspy.Round(
        (corner_positions[1][0], corner_positions[1][1]),
        corner_radius,
        number_of_points=32,
        layer=0
    ),
    'or'
)

rounded_corners = gdspy.boolean(
    rounded_corners,
    gdspy.Round(
        (corner_positions[2][0], corner_positions[2][1]),
        corner_radius,
        number_of_points=32,
        layer=0
    ),
    'or'
)

rounded_corners = gdspy.boolean(
    rounded_corners,
    gdspy.Round(
        (corner_positions[3][0], corner_positions[3][1]),
        corner_radius,
        number_of_points=32,
        layer=0
    ),
    'or'
)

# Combine the square with rounded corners
final_shape = gdspy.boolean(square, rounded_corners, 'not')

# Add the final shape to the cell
cell.add(final_shape)

# Save the design to a GDS file
lib.write_gds('rounded_square.gds')

print("GDS file 'rounded_square.gds' has been generated.")