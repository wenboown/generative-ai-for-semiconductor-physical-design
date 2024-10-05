import gdspy

# Step 1: Define the GDS library and cell
lib = gdspy.Library()
cell = lib.new_cell("Square_with_Rounded_Corners")

# Step 2: Define the parameters
square_size = (10, 10)  # mm
corner_radius = 1  # mm

# Step 3: Draw the square with rounded corners
points = [
    (-square_size[0]/2 + corner_radius, -square_size[1]/2),
    (-square_size[0]/2, -square_size[1]/2 + corner_radius),
    (-square_size[0]/2, square_size[1]/2 - corner_radius),
    (-square_size[0]/2 + corner_radius, square_size[1]/2),
    (square_size[0]/2 - corner_radius, square_size[1]/2),
    (square_size[0]/2, square_size[1]/2 - corner_radius),
    (square_size[0]/2, -square_size[1]/2 + corner_radius),
    (square_size[0]/2 - corner_radius, -square_size[1]/2)
]

poly = gdspy.Polygon(points, layer=1, datatype=1)
cell.add(poly)

# Step 4: Add corner circles for rounding
for point, angle in [
    ((-square_size[0]/2, -square_size[1]/2), 0),
    ((-square_size[0]/2, square_size[1]/2), 90),
    ((square_size[0]/2, square_size[1]/2), 180),
    ((square_size[0]/2, -square_size[1]/2), 270)
]:
    circle = gdspy.Round(point, corner_radius, number_of_points=128, layer=1, datatype=1)
    cell.add(circle)

# Step 5: Save the design to a GDS file
lib.write_gds('square_with_rounded_corners.gds')