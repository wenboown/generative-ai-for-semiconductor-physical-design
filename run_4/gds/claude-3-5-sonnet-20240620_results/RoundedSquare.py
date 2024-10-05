import gdspy
import numpy as np

# Create a new library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('MAIN')

# Define dimensions (in micrometers)
width = 10000  # 10 mm
height = 10000  # 10 mm
corner_radius = 1000  # 1 mm

# Create the main square shape
square = gdspy.Rectangle((0, 0), (width, height))

# Create circular sectors for rounded corners
corner_points = 100  # Number of points to approximate the circular arc
corners = [
    gdspy.Round((corner_radius, corner_radius), corner_radius, number_of_points=corner_points, initial_angle=np.pi, final_angle=3*np.pi/2),
    gdspy.Round((width - corner_radius, corner_radius), corner_radius, number_of_points=corner_points, initial_angle=3*np.pi/2, final_angle=2*np.pi),
    gdspy.Round((width - corner_radius, height - corner_radius), corner_radius, number_of_points=corner_points, initial_angle=0, final_angle=np.pi/2),
    gdspy.Round((corner_radius, height - corner_radius), corner_radius, number_of_points=corner_points, initial_angle=np.pi/2, final_angle=np.pi)
]

# Perform boolean operation to create the final shape
final_shape = gdspy.boolean(square, corners, 'or')

# Add the final shape to the cell
cell.add(final_shape)

# Save the design to a GDS file
lib.write_gds('rounded_square.gds')

print("GDS file 'rounded_square.gds' has been generated successfully.")