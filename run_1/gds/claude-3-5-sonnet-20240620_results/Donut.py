import gdspy
import numpy as np

# Create a new library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('DONUT')

# Set the units to millimeters (1000 units = 1mm)
unit = 1000

# Define the donut parameters
outer_radius = 10 * unit  # 10mm
inner_radius = 5 * unit   # 5mm
max_distance = 0.01 * unit  # 0.01mm between points for smoothness

# Calculate the number of points needed for the desired smoothness
num_points = int(2 * np.pi * outer_radius / max_distance)

# Generate points for the outer circle
theta = np.linspace(0, 2*np.pi, num_points, endpoint=False)
outer_x = outer_radius * np.cos(theta)
outer_y = outer_radius * np.sin(theta)
outer_points = np.column_stack((outer_x, outer_y))

# Generate points for the inner circle (in reverse order)
inner_x = inner_radius * np.cos(theta)
inner_y = inner_radius * np.sin(theta)
inner_points = np.column_stack((inner_x, inner_y))[::-1]

# Combine outer and inner points to form the donut
donut_points = np.vstack((outer_points, inner_points))

# Create the donut polygon
donut = gdspy.Polygon(donut_points, layer=0)

# Add the donut to the cell
cell.add(donut)

# Save the design to a GDS file
lib.write_gds('donut.gds')

print("Donut shape has been generated and saved as 'donut.gds'")