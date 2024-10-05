import numpy as np
import gdspy

# Define the parameters
t_start = 0
t_end = 6 * np.pi
t_step = 0.01
line_width = 1
num_points = int((t_end - t_start) / t_step)

# Generate the parametric spiral
t = np.linspace(t_start, t_end, num_points)
r = np.exp(-0.1 * t)
x = r * np.cos(t)
y = r * np.sin(t)

# Create the GDS library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('spiral')

# Create the spiral path
path = gdspy.FlexPath(np.column_stack((x, y)),
                      line_width,
                      layer=0,
                      datatype=0)

# Add the path to the cell
cell.add(path)

# Save the GDS file
lib.write_gds('spiral.gds')