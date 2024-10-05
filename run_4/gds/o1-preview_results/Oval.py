import gdspy
import numpy as np

# Create a new GDSII library
lib = gdspy.GdsLibrary()

# Create a cell to contain the oval
cell = lib.new_cell('OVAL_CELL')

# Define the parameters for the oval (ellipse)
a = 10000  # Semi-major axis in micrometers (20 mm / 2)
b = 6500   # Semi-minor axis in micrometers (13 mm / 2)
center = (0, 0)  # Center of the oval at (0, 0)

# Generate points along the perimeter of the ellipse
num_points = 256  # Number of points to define the ellipse
theta = np.linspace(0, 2 * np.pi, num_points)
x = center[0] + a * np.cos(theta)
y = center[1] + b * np.sin(theta)
points = np.column_stack((x, y))

# Create the ellipse polygon on layer 0
oval = gdspy.Polygon(points, layer=0)

# Add the oval to the cell
cell.add(oval)

# Save the library to a GDS file
lib.write_gds('oval.gds')