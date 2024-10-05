import gdspy
import numpy as np

# Create a new library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('SPIRAL')

# Define the parametric equations for the spiral
def r(t):
    return np.exp(-0.1 * t)

def x(t):
    return r(t) * np.cos(t)

def y(t):
    return r(t) * np.sin(t)

# Generate points along the spiral
t = np.linspace(0, 6 * np.pi, 1000)
points = np.column_stack((x(t), y(t)))

# Create the spiral path
spiral = gdspy.FlexPath(
    points,
    1,  # width of 1 unit
    layer=0,
    datatype=0
)

# Add the spiral to the cell
cell.add(spiral)

# Save the design to a GDS file
lib.write_gds('parametric_spiral.gds')

print("GDS file 'parametric_spiral.gds' has been created.")