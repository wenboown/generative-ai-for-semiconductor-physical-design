import numpy as np
import gdspy

# Define the spiral parameters
def r(t):
    return np.exp(-0.1*t)

# Create the GDS library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('spiral')

# Generate the spiral points
t = np.linspace(0, 6*np.pi, 1000)
x = r(t) * np.cos(t)
y = r(t) * np.sin(t)

# Create the spiral path
path = gdspy.FlexPath(np.column_stack((x, y)), 1, layer=0, datatype=0)

# Add the path to the cell
cell.add(path)

# Save the GDS file
lib.write_gds('spiral.gds')