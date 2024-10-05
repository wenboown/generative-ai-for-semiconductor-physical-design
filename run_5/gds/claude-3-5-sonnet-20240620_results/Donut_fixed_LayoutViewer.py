import gdspy
import numpy as np

# Create a new library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('DONUT')

# Define the parameters
outer_radius = 10000  # 10 mm in nanometers
inner_radius = 5000   # 5 mm in nanometers
max_distance = 10     # 0.01 mm in nanometers

# Create the outer circle
outer_circle = gdspy.Round((0, 0), outer_radius, tolerance=max_distance)

# Create the inner circle
inner_circle = gdspy.Round((0, 0), inner_radius, tolerance=max_distance)

# Create the donut shape by subtracting the inner circle from the outer circle
donut = gdspy.boolean(outer_circle, inner_circle, 'not')

# Add the donut shape to the cell
cell.add(donut)

# Save the design to a GDS file
lib.write_gds('donut.gds')

# Optional: View the layout