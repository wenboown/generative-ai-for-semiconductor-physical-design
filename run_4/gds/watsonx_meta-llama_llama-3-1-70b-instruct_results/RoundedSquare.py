import gdspy

# Define the GDS library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell("rounded_square")

# Define the square dimensions and corner radius
square_size = (10, 10)  # mm
corner_radius = 1  # mm

# Calculate the square coordinates
x_min, y_min = -square_size[0] / 2, -square_size[1] / 2
x_max, y_max = square_size[0] / 2, square_size[1] / 2

# Create the square with rounded corners
points = [
    (x_min + corner_radius, y_min),
    (x_max - corner_radius, y_min),
    (x_max, y_min + corner_radius),
    (x_max, y_max - corner_radius),
    (x_max - corner_radius, y_max),
    (x_min + corner_radius, y_max),
    (x_min, y_max - corner_radius),
    (x_min, y_min + corner_radius)
]

# Create the path for the square
path = gdspy.Path([points], width=0).fracture(0.001)

# Create the polygon for the square
polygon = gdspy.Polygon(points).fracture(0.001)

# Add the polygon to the cell
cell.add(polygon)

# Save the design to a GDS file
lib.write_gds("rounded_square.gds")