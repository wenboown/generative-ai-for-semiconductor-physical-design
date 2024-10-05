import gdspy
import numpy as np

# Create a new GDSII library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('SPIRAL')

# Define the line width
line_width = 1.0

# Create a path with the specified line width
path = gdspy.Path(width=line_width, initial_point=(0, 0))

# Define the parametric functions for x(t) and y(t)
def x(t):
    return np.exp(-0.1 * t) * np.cos(t)

def y(t):
    return np.exp(-0.1 * t) * np.sin(t)

# Define the parametric function for the path
def parametric_spiral(u):
    t = u * 6 * np.pi  # u ranges from 0 to 1
    return x(t), y(t)

# Number of points to evaluate
number_of_evaluations = 1000

# Use the parametric function to create the path
path.parametric(
    curve_function=parametric_spiral,
    number_of_evaluations=number_of_evaluations
)

# Add the path to the cell
cell.add(path)

# Save the library in a GDSII file
lib.write_gds('parametric_spiral.gds')