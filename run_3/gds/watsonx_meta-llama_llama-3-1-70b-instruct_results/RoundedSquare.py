import gdspy

# Define the design parameters
size = 10  # mm
radius = 1  # mm

# Create a new GDS library and cell
lib = gdspy.Library()
cell = lib.new_cell("Square")

# Create a square with rounded corners
pts = [
    (-size/2, -size/2+radius),
    (-size/2+radius, -size/2),
    (size/2-radius, -size/2),
    (size/2, -size/2+radius),
    (size/2, size/2-radius),
    (size/2-radius, size/2),
    (-size/2+radius, size/2),
    (-size/2, size/2-radius),
    (-size/2, -size/2+radius)
]
square = gdspy.Polygon(pts, 1)

# Add the square to the cell
cell.add(square)

# Save the design to a GDS file
lib.write_gds("rounded_square.gds")