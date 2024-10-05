import gdspy

# Create a new GDSII library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('TRAPEZOID')

# Define the coordinates of the trapezoid in micrometers (since 1 mm = 1000 um)
points = [
    (-10000, -4000),  # Bottom left corner (−10 mm, −4 mm)
    (10000, -4000),   # Bottom right corner (10 mm, −4 mm)
    (5000, 4000),     # Top right corner (5 mm, 4 mm)
    (-5000, 4000)     # Top left corner (−5 mm, 4 mm)
]

# Create the trapezoid polygon
trapezoid = gdspy.Polygon(points)

# Add the trapezoid to the cell
cell.add(trapezoid)

# Write the GDSII file
lib.write_gds('trapezoid.gds')