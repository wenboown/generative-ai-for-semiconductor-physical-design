import gdspy

# Create a new library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('TRAPEZOID')

# Define the coordinates of the trapezoid
coordinates = [
    (-5e6, 4e6),   # Top-left corner
    (5e6, 4e6),    # Top-right corner
    (10e6, -4e6),  # Bottom-right corner
    (-10e6, -4e6)  # Bottom-left corner
]

# Create the trapezoid polygon
trapezoid = gdspy.Polygon(coordinates, layer=0)

# Add the trapezoid to the cell
cell.add(trapezoid)

# Save the design to a GDS file
lib.write_gds('trapezoid.gds')

print("Trapezoid GDS file has been generated successfully.")