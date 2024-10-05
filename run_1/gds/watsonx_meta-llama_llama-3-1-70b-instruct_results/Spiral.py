import numpy as np
import gdspy

# Create a new library and cell
lib = gdspy.Library()
cell = lib.new_cell('Spiral')

# Define the spiral parameters
t = np.linspace(0, 6 * np.pi, 1000)
r = np.exp(-0.1 * t)

# Create a new polygon for the spiral
spiral = gdspy.Polygon(zip(r * np.cos(t), r * np.sin(t)), 1)

# Add the spiral to the cell
cell.add(spiral)

# Save the design to a GDS file
lib.write_gds('spiral.gds', unit=1.0e-6, precision=1.0e-9)