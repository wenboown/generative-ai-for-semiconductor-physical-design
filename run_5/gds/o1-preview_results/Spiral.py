import gdspy
import numpy as np

# Create a new GDSII library
lib = gdspy.GdsLibrary()

# Create a cell to hold the design
cell = lib.new_cell('SPIRAL')

# Generate the spiral data
t = np.linspace(0, 6 * np.pi, 1000)  # Parameter t from 0 to 6π
r = np.exp(-0.1 * t)  # Radius as a function of t
x = r * np.cos(t)  # x-coordinate
y = r * np.sin(t)  # y-coordinate
points = np.column_stack((x, y))  # Combine x and y into coordinate pairs

# Create the spiral path with a line width of 1
path = gdspy.FlexPath(
    points,
    width=1.0,
    corners='circular',  # Smooth corners for the spiral
    gdsii_path=False,  # Represent the path as a polygon for arbitrary shapes
    max_points=0       # No limit on the number of points in the polygon
)

# Add the path to the cell
cell.add(path)

# Save the design to a GDSII file
lib.write_gds('spiral.gds')