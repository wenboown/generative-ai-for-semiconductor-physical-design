import numpy as np
import gdspy

# Design specifications
t = np.linspace(0, 6 * np.pi, 1000)
r = np.exp(-0.1 * t)
x = r * np.cos(t)
y = r * np.sin(t)
points = np.vstack((x, y)).T

# Create a new GDS library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('SPIRAL')

# Create the spiral path
path = gdspy.Path(1, (x[0], y[0]))
path.parametric(lambda u: r[int(u * (len(t) - 1))] * np.cos(t[int(u * (len(t) - 1))]),
                lambda u: r[int(u * (len(t) - 1))] * np.sin(t[int(u * (len(t) - 1))]),
                number_of_evaluations=len(t))

# Add the path to the cell
cell.add(path)

# Save to a GDS file
gdspy.write_gds('parametric_spiral.gds', unit=1.0e-6, precision=1.0e-9)