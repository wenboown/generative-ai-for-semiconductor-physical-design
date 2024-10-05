import gdspy
import numpy as np

# Define the library and cell for the GDS layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell('donut')

# Define the outer and inner radii
outer_radius = 10
inner_radius = 5

# Create the outer circle
outer_circle = gdspy.Round((0, 0), outer_radius, number_of_points=int(2*np.pi*outer_radius/0.01), max_points=1000)

# Create the inner circle
inner_circle = gdspy.Round((0, 0), inner_radius, number_of_points=int(2*np.pi*inner_radius/0.01), max_points=1000)

# Create the donut shape by subtracting the inner circle from the outer circle
donut = gdspy.boolean(outer_circle, inner_circle, 'not')

# Add the donut shape to the cell
cell.add(donut)

# Save the design to a GDS file
lib.write_gds('donut.gds')