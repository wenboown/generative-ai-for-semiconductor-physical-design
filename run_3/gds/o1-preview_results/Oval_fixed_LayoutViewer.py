import gdspy
import numpy as np

# Create a new GDSII library, which contains a set of cells.
lib = gdspy.GdsLibrary()

# Create a cell (top level) to contain the layout elements.
cell = lib.new_cell('OVAL')

# Define parameters for the ellipse (oval)
# Dimensions are in micrometers (µm)
# Convert millimeters to micrometers (1 mm = 1000 µm)
center = (0, 0)        # Center at (0, 0)
a = 10000              # Semi-major axis length in µm (10 mm)
b = 6500               # Semi-minor axis length in µm (6.5 mm)
num_points = 200       # Number of points to approximate the ellipse
layer_number = 0       # Layer number

# Generate points along the ellipse perimeter
theta = np.linspace(0, 2 * np.pi, num_points)
x = center[0] + a * np.cos(theta)
y = center[1] + b * np.sin(theta)
points = np.column_stack((x, y))

# Create the polygon representing the ellipse on the specified layer
ellipse = gdspy.Polygon(points, layer=layer_number)

# Add the polygon to the cell
cell.add(ellipse)

# Write the GDSII file to disk.
# The default unit is 1e-6 meters (1 µm), so we do not need to adjust units
lib.write_gds('oval.gds')

# Optional: View the layout using gdspy's internal viewer (requires matplotlib)