import numpy as np
import gdspy

# Define the library and cell for the GDS layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell('parametric_spiral')

# Define the spiral parameters
start_angle = 0
end_angle = 6 * np.pi
num_points = 1000
line_width = 1

# Generate the spiral points
t = np.linspace(start_angle, end_angle, num_points)
r = np.exp(-0.1 * t)
x = r * np.cos(t)
y = r * np.sin(t)

# Create the spiral polygon
spiral = gdspy.FlexPath(np.column_stack((x, y)), line_width)

# Add the spiral to the cell
cell.add(spiral)

# Save the design to a GDS file
lib.write_gds('parametric_spiral.gds')