import gdspy
import numpy as np

# Create a new library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('CIRCLE')

# Define circle parameters
layer = 0
radius = 10000  # 10 mm = 10000 µm (GDSII units are in micrometers)
center = (0, 0)

# Create the circle
circle = gdspy.Round(center, radius, layer=layer)

# Add the circle to the cell
cell.add(circle)

# Save the design to a GDSII file
lib.write_gds('circle.gds')

print("GDSII file 'circle.gds' has been generated successfully.")