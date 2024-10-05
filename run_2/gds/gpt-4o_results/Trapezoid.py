import gdspy

# Define the upper edge length, lower edge length, and height of the trapezoid
upper_edge = 10
lower_edge = 20
height = 8

# Calculate half the lengths to center the trapezoid at (0, 0)
half_upper_edge = upper_edge / 2
half_lower_edge = lower_edge / 2
half_height = height / 2

# Define the coordinates of the trapezoid vertices
vertices = [
    (-half_lower_edge, -half_height),
    (half_lower_edge, -half_height),
    (half_upper_edge, half_height),
    (-half_upper_edge, half_height)
]

# Create a new GDSII library
lib = gdspy.GdsLibrary()

# Create a cell to contain the trapezoid
cell = lib.new_cell('TRAPEZOID')

# Create the trapezoid as a polygon
trapezoid = gdspy.Polygon(vertices)

# Add the trapezoid to the cell
cell.add(trapezoid)

# Save the GDS file
lib.write_gds('trapezoid.gds')

print("GDS layout with trapezoid generated and saved as 'trapezoid.gds'")