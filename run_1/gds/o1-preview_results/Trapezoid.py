import gdspy

# Create a new GDSII library
lib = gdspy.GdsLibrary()

# Create a new cell in the library
cell = lib.new_cell('TRAPEZOID')

# Trapezoid specifications (dimensions in micrometers)
# Upper edge length: 10 mm = 10000 µm
# Lower edge length: 20 mm = 20000 µm
# Height: 8 mm = 8000 µm
# Centered at (0, 0)

# Calculate the half lengths
upper_half_length = 5000    # Half of upper edge length in µm
lower_half_length = 10000   # Half of lower edge length in µm
half_height = 4000          # Half of height in µm

# Define the coordinates of the trapezoid vertices
points = [
    (-upper_half_length, half_height),   # Upper left vertex
    (upper_half_length, half_height),    # Upper right vertex
    (lower_half_length, -half_height),   # Lower right vertex
    (-lower_half_length, -half_height)   # Lower left vertex
]

# Create the trapezoid polygon
trapezoid = gdspy.Polygon(points)

# Add the polygon to the cell
cell.add(trapezoid)

# Save the library in GDSII format
lib.write_gds('trapezoid.gds')