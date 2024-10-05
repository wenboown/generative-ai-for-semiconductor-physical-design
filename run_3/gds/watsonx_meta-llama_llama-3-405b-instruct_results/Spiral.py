import gdspy
import numpy as np

# Define the parameters
t_min, t_max = 0, 6*np.pi
t_step = 0.01
line_width = 1

# Generate the spiral points
t = np.arange(t_min, t_max, t_step)
r = np.exp(-0.1*t)
x = r * np.cos(t)
y = r * np.sin(t)

# Create the GDS library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('spiral')

# Create the spiral path
path = gdspy.FlexPath(np.column_stack((x, y)), line_width)

# Add the path to the cell
cell.add(path)

# Save the design to a GDS file
lib.write_gds('spiral.gds')