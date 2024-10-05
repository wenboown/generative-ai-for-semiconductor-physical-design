import gdspy
import numpy as np

# Define the library and cell for the GDS layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell('donut')

# Define the outer and inner radii of the donut
outer_radius = 10
inner_radius = 5

# Define the max distance between points for smooth circle
max_distance = 0.01

# Generate the outer circle
outer_circle = gdspy.Round((0, 0), outer_radius, number_of_points=int(2*np.pi*outer_radius/max_distance))

# Generate the inner circle
inner_circle = gdspy.Round((0, 0), inner_radius, number_of_points=int(2*np.pi*inner_radius/max_distance))

# Subtract the inner circle from the outer circle to create the donut shape
donut = gdspy.boolean(outer_circle, inner_circle, 'not')

# Add the donut shape to the cell
cell.add(donut)

# Save the design to a GDS file
lib.write_gds('donut.gds')