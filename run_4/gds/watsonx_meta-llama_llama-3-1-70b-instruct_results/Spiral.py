import numpy as np
import gdspy

# Define the GDS library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell("spiral")

# Define the spiral parameters
t_start = 0
t_end = 6 * np.pi
r_func = lambda t: np.exp(-0.1 * t)
line_width = 1

# Generate the spiral path
t_range = np.linspace(t_start, t_end, 1000)
x = r_func(t_range) * np.cos(t_range)
y = r_func(t_range) * np.sin(t_range)

# Create the spiral path in the GDS cell
path = gdspy.Path(line_width, initial_point=(x[0], y[0]))
for i in range(1, len(x)):
    path.segment((x[i], y[i]), relative=False)

# Add the path to the cell
cell.add(path)

# Save the GDS layout to a file
lib.write_gds("spiral.gds")