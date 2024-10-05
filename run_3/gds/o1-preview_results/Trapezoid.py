import gdspy

# Reset the current library to ensure a clean slate
gdspy.current_library = None

# Create a new GDSII library with units in millimeters (unit=1e-3 meters)
lib = gdspy.GdsLibrary(unit=1e-3, precision=1e-6)

# Create a new cell to contain the trapezoid
cell = lib.new_cell('TRAPEZOID_CELL')

# Define the coordinates of the trapezoid
# Upper edge (top): from x = -5 mm to x = 5 mm at y = 4 mm
# Lower edge (bottom): from x = -10 mm to x = 10 mm at y = -4 mm
points = [(-5, 4), (5, 4), (10, -4), (-10, -4)]

# Create the trapezoid polygon using the defined points
trapezoid = gdspy.Polygon(points)

# Add the trapezoid to the cell
cell.add(trapezoid)

# Save the library in a GDSII file called 'trapezoid.gds'
lib.write_gds('trapezoid.gds')