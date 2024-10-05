import gdspy
import numpy as np

# Define spiral parameters
t_start = 0
t_end = 6 * np.pi
num_points = 1000
line_width = 1

# Generate spiral points
t = np.linspace(t_start, t_end, num_points)
r = np.exp(-0.1 * t)
x = r * np.cos(t)
y = r * np.sin(t)

# Create GDS layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell('SPIRAL')

# Create the spiral path
spiral_path = gdspy.FlexPath(
    points=list(zip(x, y)),
    width=line_width,
    layer=0,
    datatype=0
)

# Add the spiral to the cell
cell.add(spiral_path)

# Save the GDS file
lib.write_gds('parametric_spiral.gds')

print("GDS file 'parametric_spiral.gds' has been generated.")