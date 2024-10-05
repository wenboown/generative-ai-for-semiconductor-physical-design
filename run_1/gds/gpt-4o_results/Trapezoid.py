import gdspy

# Define the library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('TRAPEZOID')

# Convert mm to microns (assuming 1 mm = 1000 microns)
upper_edge = 10 * 1000
lower_edge = 20 * 1000
height = 8 * 1000

# Calculate the coordinates of the trapezoid
# Let the center of the trapezoid be at (0, 0)
x0 = -lower_edge / 2
x1 = -upper_edge / 2
x2 = upper_edge / 2
x3 = lower_edge / 2
y0 = -height / 2
y1 = height / 2

# Define points of the trapezoid in a counterclockwise manner
points = [
    (x0, y0),  # Bottom-left
    (x3, y0),  # Bottom-right
    (x2, y1),  # Top-right
    (x1, y1)   # Top-left
]

# Create the trapezoid polygon
trapezoid = gdspy.Polygon(points)

# Add the trapezoid to the cell
cell.add(trapezoid)

# Save the design to a GDS file
lib.write_gds('trapezoid_layout.gds')

print("Trapezoid layout has been saved to 'trapezoid_layout.gds'")