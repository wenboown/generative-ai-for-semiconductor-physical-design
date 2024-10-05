import gdspy

# Define the GDS layer
layer = 1

# Define the upper edge, lower edge, and height of the trapezoid
upper_edge = 10
lower_edge = 20
height = 8

# Calculate the x-coordinates of the upper and lower edges
x1_upper = -upper_edge / 2
x2_upper = upper_edge / 2
x1_lower = -lower_edge / 2
x2_lower = lower_edge / 2

# Define the points of the trapezoid
points = [(x1_upper, -height / 2), (x2_upper, -height / 2), 
          (x2_lower, height / 2), (x1_lower, height / 2)]

# Create a polygon from the points
trapezoid = gdspy.Polygon(points, layer)

# Create a cell for the GDS layout
cell = gdspy.Cell('TRAPEZOID')

# Add the trapezoid to the cell
cell.add(trapezoid)

# Save the design to a GDS file
gdspy.write_gds('trapezoid.gds', cell, unit=1.0e-6, precision=1.0e-9)