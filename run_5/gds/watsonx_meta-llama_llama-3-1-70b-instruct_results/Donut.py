import gdspy
import numpy as np

# Define the library and cell for the GDS layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell('donut_shape')

# Define the outer and inner radii
outer_radius = 10  # mm
inner_radius = 5  # mm

# Define the max distance between points
max_distance = 0.01  # mm

# Calculate the number of points for the circles
n_points_outer = int(np.ceil(2 * np.pi * outer_radius / max_distance))
n_points_inner = int(np.ceil(2 * np.pi * inner_radius / max_distance))

# Create the outer circle
outer_angle = np.linspace(0, 2 * np.pi, n_points_outer)
outer_x = outer_radius * np.cos(outer_angle)
outer_y = outer_radius * np.sin(outer_angle)
outer_points = np.column_stack((outer_x, outer_y))

# Create the inner circle
inner_angle = np.linspace(0, 2 * np.pi, n_points_inner)
inner_x = inner_radius * np.cos(inner_angle)
inner_y = inner_radius * np.sin(inner_angle)
inner_points = np.column_stack((inner_x, inner_y))

# Create the donut shape by combining the outer and inner circles
donut_points = np.vstack((outer_points, inner_points[::-1]))

# Add the donut shape to the cell
cell.add(gdspy.Polygon(donut_points, layer=1))

# Save the design to a GDS file
lib.write_gds('donut_shape.gds')