import gdspy
import numpy as np

# Define the library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('donut')

# Define the outer and inner radii
outer_radius = 10
inner_radius = 5

# Set the maximum distance between points for smooth curves
max_distance = 0.01

# Calculate the number of points needed for the outer circle
num_outer_points = int(2 * np.pi * outer_radius / max_distance)

# Calculate the number of points needed for the inner circle
num_inner_points = int(2 * np.pi * inner_radius / max_distance)

# Generate the outer circle points
outer_angles = np.linspace(0, 2 * np.pi, num_outer_points, endpoint=False)
outer_points = np.column_stack((outer_radius * np.cos(outer_angles), outer_radius * np.sin(outer_angles)))

# Generate the inner circle points
inner_angles = np.linspace(0, 2 * np.pi, num_inner_points, endpoint=False)
inner_points = np.column_stack((inner_radius * np.cos(inner_angles), inner_radius * np.sin(inner_angles)))

# Create the donut shape
donut = gdspy.Polygon(outer_points)
donut_hole = gdspy.Polygon(inner_points)
donut = gdspy.boolean(donut, donut_hole, 'not')

# Add the donut shape to the cell
cell.add(donut)

# Save the design to a GDS file
lib.write_gds('donut.gds')