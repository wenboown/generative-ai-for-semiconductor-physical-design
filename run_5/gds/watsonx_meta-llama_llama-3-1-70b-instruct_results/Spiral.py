import numpy as np
import gdspy

# Define the GDS library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('spiral')

# Define the spiral parameters
t = np.linspace(0, 6*np.pi, 1000)
r = np.exp(-0.1*t)
x = r * np.cos(t)
y = r * np.sin(t)

# Create the spiral path
spiral = gdspy.Path(1, [(x[0], y[0])])
for i in range(1, len(x)):
    spiral.segment([(x[i], y[i])], relative=True)

# Add the spiral to the cell
cell.add(spiral)

# Save the GDS file
lib.write_gds('spiral.gds')