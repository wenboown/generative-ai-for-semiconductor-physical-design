import gdspy
import numpy as np

# Create a new library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('DONUT')

# Define parameters (converting mm to µm)
outer_radius = 10000  # 10 mm
inner_radius = 5000   # 5 mm
max_distance = 10     # 0.01 mm

# Calculate number of points for smooth circles
num_points = int(np.ceil(2 * np.pi * outer_radius / max_distance))

# Create outer circle
outer_circle = gdspy.Round((0, 0), outer_radius, number_of_points=num_points)

# Create inner circle
inner_circle = gdspy.Round((0, 0), inner_radius, number_of_points=num_points)

# Create donut by subtracting inner circle from outer circle
donut = gdspy.boolean(outer_circle, inner_circle, 'not')

# Add the donut to the cell
cell.add(donut)

# Save the design to a GDS file
lib.write_gds('donut.gds')

print("Donut shape has been generated and saved as 'donut.gds'")