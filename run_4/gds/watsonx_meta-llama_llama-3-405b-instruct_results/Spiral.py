import gdspy
import numpy as np

# Define the library and cell for the GDS layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell('spiral')

# Define the parametric spiral
def r(t):
    return np.exp(-0.1 * t)

# Generate the spiral curve
t = np.linspace(0, 6 * np.pi, 1000)
x = r(t) * np.cos(t)
y = r(t) * np.sin(t)

# Create the polygon for the spiral
spiral = gdspy.FlexPath((x, y), 1, layer=0, datatype=0)

# Add the spiral to the cell
cell.add(spiral)

# Save the design to a GDS file
lib.write_gds('spiral.gds')