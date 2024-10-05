import numpy as np
import gdspy

# Create a new library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('spiral')

# Define the parameters
t_min = 0
t_max = 6 * np.pi
line_width = 1

# Generate the spiral coordinates
t = np.linspace(t_min, t_max, 1000)
r = np.exp(-0.1 * t)
x = r * np.cos(t)
y = r * np.sin(t)

# Create the spiral path
spiral = gdspy.Path(line_width, [(x[0], y[0])])
for i in range(1, len(x)):
    spiral.segment([(x[i], y[i])], relative=True, **{'layer': 1, 'datatype': 0})

# Add the spiral to the cell
cell.add(spiral)

# Save the design to a GDS file
lib.write_gds('spiral.gds')