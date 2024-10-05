import gdspy
import numpy as np

# Create a new GDSII library
lib = gdspy.GdsLibrary()

# Create a cell to add geometric elements
cell = lib.new_cell('SPIRAL')

# Define the spiral parameters
path_width = 1.0
t_start = 0
t_end = 6 * np.pi
num_evaluations = 1000  # Increase for smoother spiral

# Starting point of the spiral
r0 = np.exp(-0.1 * t_start)
x0 = r0 * np.cos(t_start)
y0 = r0 * np.sin(t_start)
path = gdspy.Path(path_width, (x0, y0))

# Parametric function for the spiral
def parametric_spiral(u):
    r = np.exp(-0.1 * u)
    x = r * np.cos(u)
    y = r * np.sin(u)
    return (x, y)

# Create the spiral path
path.parametric(
    parametric_spiral,
    t_start,
    t_end,
    number_of_evaluations=num_evaluations,
    max_points=199
)

# Add the path to the cell
cell.add(path)

# Save the library to a GDSII file
lib.write_gds('spiral.gds')

# Optionally, view the layout (requires a GUI environment)