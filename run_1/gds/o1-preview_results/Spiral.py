import gdspy
import numpy

# Create a new GDSII library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('SPIRAL')

# Define the spiral function
def spiral(t):
    x = numpy.exp(-0.1 * t) * numpy.cos(t)
    y = numpy.exp(-0.1 * t) * numpy.sin(t)
    return (x, y)

# Create the path with width 1
start_x, start_y = spiral(0)
path = gdspy.Path(1, (start_x, start_y))

# Generate the spiral path from t=0 to t=6*pi
path.parametric(spiral, t_max=6 * numpy.pi, number_of_evaluations=1000)

# Add the path to the cell
cell.add(path)

# Save the library in a GDSII file
lib.write_gds('spiral.gds')