import gdspy

# Parse the user’s design specifications
cell_size = (10, 10)  # mm
corner_radius = 1  # mm

# Define the library and cell for the GDS layout
lib = gdspy.Library()
cell = lib.new_cell('rounded_square')

# Create each geometric element (e.g., rectangles, polygons) with precise coordinates
x_min, y_min = 0, 0
x_max, y_max = cell_size[0], cell_size[1]

# Define the polygon points
points = [
    [x_min + corner_radius, y_min],
    [x_max - corner_radius, y_min],
    [x_max, y_min + corner_radius],
    [x_max, y_max - corner_radius],
    [x_max - corner_radius, y_max],
    [x_min + corner_radius, y_max],
    [x_min, y_max - corner_radius],
    [x_min, y_min + corner_radius]
]

# Use the gdspy.Round function to create a rounded polygon
poly = gdspy.Round(points, corner_radius)

# Add the polygon to the cell
cell.add(poly)

# Save the design to a GDS file
lib.write_gds('rounded_square.gds')