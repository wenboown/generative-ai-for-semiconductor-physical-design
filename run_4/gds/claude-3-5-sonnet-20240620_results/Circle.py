import gdspy
import numpy as np

# Create a new library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('CIRCLE')

# Create a circle
# Convert 10 mm to µm
radius = 10 * 1000
circle = gdspy.Round((0, 0), radius, layer=0, number_of_points=128)

# Add the circle to the cell
cell.add(circle)

# Save the design to a GDS file
lib.write_gds('circle.gds')

print("GDS file 'circle.gds' has been generated successfully.")