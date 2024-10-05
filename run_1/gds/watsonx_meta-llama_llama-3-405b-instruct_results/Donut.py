import gdspy
import numpy as np

# Define the library and cell for the GDS layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell('donut')

# Define the outer and inner radii
outer_radius = 10
inner_radius = 5

# Define the maximum distance between points for a smooth circle
max_distance = 0.01

# Calculate the number of points required for the circle
num_points_outer = int(np.ceil(2 * np.pi * outer_radius / max_distance))
num_points_inner = int(np.ceil(2 * np.pi * inner_radius / max_distance))

# Generate the outer and inner circle points
theta = np.linspace(0, 2 * np.pi, num_points_outer, endpoint=False)
outer_x = outer_radius * np.cos(theta)
outer_y = outer_radius * np.sin(theta)

theta = np.linspace(0, 2 * np.pi, num_points_inner, endpoint=False)
inner_x = inner_radius * np.cos(theta)
inner_y = inner_radius * np.sin(theta)

# Create the outer circle
outer_polygon = gdspy.Polygon([(x, y) for x, y in zip(outer_x, outer_y)])

# Create the inner circle
inner_polygon = gdspy.Polygon([(x, y) for x, y in zip(inner_x, inner_y)])

# Create the donut shape by subtracting the inner circle from the outer circle
donut = gdspy.boolean([outer_polygon], [inner_polygon], 'subtract')

# Add the donut shape to the cell
cell.add(donut)

# Save the design to a GDS file
lib.write_gds('donut.gds')