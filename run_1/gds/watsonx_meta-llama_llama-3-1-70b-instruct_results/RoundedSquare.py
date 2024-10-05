import gdspy

# Parse the user's design specifications
specifications = {
    'size': (10, 10),  # mm
    'corner_radius': 1  # mm
}

# Define the library and cell for the GDS layout
lib = gdspy.Library()
cell = lib.new_cell('rounded_square')

# Define the coordinates for the square
x, y = 0, 0
width, height = specifications['size']
corner_radius = specifications['corner_radius']

# Create each geometric element (e.g., rectangles, polygons) with precise coordinates
points = [
    (x, y + corner_radius),
    (x, y + height - corner_radius),
    (x + corner_radius, y + height),
    (x + width - corner_radius, y + height),
    (x + width, y + height - corner_radius),
    (x + width, y + corner_radius),
    (x + width - corner_radius, y),
    (x + corner_radius, y)
]

# Create the rounded square polygon
polygon = gdspy.Polygon(points)

# Add the polygon to the cell
cell.add(polygon)

# Save the design to a GDS file
lib.write_gds('rounded_square.gds')