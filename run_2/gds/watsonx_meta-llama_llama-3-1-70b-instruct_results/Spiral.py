import gdspy
import numpy as np

# Parse the user's design specifications
r_func = lambda t: np.exp(-0.1 * t)
t_start = 0
t_end = 6 * np.pi
line_width = 1

# Create a new library and cell for the GDS layout
lib = gdspy.Library()
cell = lib.new_cell('spiral')

# Generate an array of t values
t = np.linspace(t_start, t_end, 1000)

# Calculate the corresponding r values
r = r_func(t)

# Calculate the x and y coordinates of the spiral
x = r * np.cos(t)
y = r * np.sin(t)

# Create the spiral path
path = gdspy.Path(line_width, [(x[0], y[0])])
for i in range(1, len(x)):
    path.segment([(x[i], y[i])], final_width=line_width)

# Add the path to the cell
cell.add(path)

# Save the design to a GDS file
lib.write_gds('spiral.gds')