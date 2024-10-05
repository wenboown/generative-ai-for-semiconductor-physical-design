import gdspy

# Create a GDSII library
lib = gdspy.GdsLibrary()

# Create a cell
cell = lib.new_cell('TRAPEZOID')

# Define the points of the trapezoid in micrometers (1 mm = 1000 um)
points = [(-5000, 4000), (5000, 4000), (10000, -4000), (-10000, -4000)]

# Create the trapezoid polygon
trapezoid = gdspy.Polygon(points)

# Add the trapezoid to the cell
cell.add(trapezoid)

# Save the library in a GDSII file
lib.write_gds('trapezoid.gds')