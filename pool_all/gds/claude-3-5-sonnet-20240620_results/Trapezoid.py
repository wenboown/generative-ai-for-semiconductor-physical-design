import gdspy

# Define the trapezoid dimensions (in µm)
upper_edge = 10000  # 10 mm
lower_edge = 20000  # 20 mm
height = 8000       # 8 mm

# Create a new library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('TRAPEZOID')

# Calculate trapezoid vertices
half_upper = upper_edge / 2
half_lower = lower_edge / 2
half_height = height / 2

vertices = [
    (-half_lower, -half_height),
    (half_lower, -half_height),
    (half_upper, half_height),
    (-half_upper, half_height)
]

# Create the trapezoid polygon
trapezoid = gdspy.Polygon(vertices, layer=0)

# Add the trapezoid to the cell
cell.add(trapezoid)

# Save the design to a GDS file
lib.write_gds('trapezoid.gds')

print("Trapezoid GDS file has been generated successfully.")