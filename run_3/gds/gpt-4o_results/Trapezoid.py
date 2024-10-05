import gdspy

# Define dimensions of the trapezoid
upper_edge = 10.0  # in mm
lower_edge = 20.0  # in mm
height = 8.0  # in mm

# Since center is at (0,0), calculate the coordinates of the vertices
# Vertices of trapezoid centered at (0,0)
vertices = [
    (-lower_edge / 2, -height / 2),  # Bottom-left
    (lower_edge / 2, -height / 2),   # Bottom-right
    (upper_edge / 2, height / 2),    # Top-right
    (-upper_edge / 2, height / 2)    # Top-left
]

# Create a GDSII library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('TRAPEZOID')

# Add the trapezoid to the cell
trapezoid = gdspy.Polygon(vertices)
cell.add(trapezoid)

# Save the design to a GDS file
lib.write_gds('trapezoid.gds')

print("Trapezoid layout generated and saved as 'trapezoid.gds'")