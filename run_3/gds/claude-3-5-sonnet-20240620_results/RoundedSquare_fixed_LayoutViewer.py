import gdspy
import numpy as np

# Create a new library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('SQUARE_WITH_ROUNDED_CORNERS')

# Define square dimensions and corner radius (in micrometers)
square_size = 10000  # 10 mm = 10000 µm
corner_radius = 1000  # 1 mm = 1000 µm

# Create the main square shape
square = gdspy.Rectangle((0, 0), (square_size, square_size))

# Create rounded corners
corner_points = 50  # Number of points to approximate the circular corner

# Top-right corner
corner1 = gdspy.Round((square_size - corner_radius, square_size - corner_radius),
                      corner_radius, number_of_points=corner_points,
                      initial_angle=0, final_angle=np.pi/2)

# Top-left corner
corner2 = gdspy.Round((corner_radius, square_size - corner_radius),
                      corner_radius, number_of_points=corner_points,
                      initial_angle=np.pi/2, final_angle=np.pi)

# Bottom-left corner
corner3 = gdspy.Round((corner_radius, corner_radius),
                      corner_radius, number_of_points=corner_points,
                      initial_angle=np.pi, final_angle=3*np.pi/2)

# Bottom-right corner
corner4 = gdspy.Round((square_size - corner_radius, corner_radius),
                      corner_radius, number_of_points=corner_points,
                      initial_angle=3*np.pi/2, final_angle=2*np.pi)

# Combine all shapes using boolean operations
final_shape = gdspy.boolean(square, [corner1, corner2, corner3, corner4], 'or')

# Add the final shape to the cell
cell.add(final_shape)

# Save the design to a GDS file
lib.write_gds('square_with_rounded_corners.gds')

# Optional: View the layout