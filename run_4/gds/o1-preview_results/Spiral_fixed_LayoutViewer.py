import numpy as np
import gdspy

# Parameters for the spiral
t_start = 0
t_end = 6 * np.pi
num_points = 1000  # Number of points to define the spiral
line_width = 1

# Generate the parameter t
t = np.linspace(t_start, t_end, num_points)

# Compute r(t)
r = np.exp(-0.1 * t)

# Convert polar coordinates to Cartesian coordinates
x = r * np.cos(t)
y = r * np.sin(t)

# Combine x and y into a list of points
points = np.column_stack((x, y))

# Create a new GDSII library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('Spiral_Cell')

# Create a path with the specified line width using the points
spiral_path = gdspy.FlexPath(
    points,
    line_width,
    corners='smooth',
    bend_radius=None,
    max_points=199  # To ensure compatibility with GDSII format limitations
)

# Add the path to the cell
cell.add(spiral_path)

# Write the library to a GDSII file
lib.write_gds('parametric_spiral.gds')

# Optional: View the layout using gdspy (commented out)