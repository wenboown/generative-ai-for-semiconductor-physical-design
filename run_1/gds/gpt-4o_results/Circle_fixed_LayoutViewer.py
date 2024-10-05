import gdspy
import math

# Create a GDSII library
lib = gdspy.GdsLibrary()

# Define the GDSII cell
cell = lib.new_cell('CIRCLE')

# Circle parameters
radius = 10.0  # mm
center = (0, 0)  # Center of the circle at the origin
layer = 0  # GDSII layer number

# Function for creating a circle using polygons
def create_circle(radius, center, layer, number_of_points=100):
    points = []
    for i in range(number_of_points):
        angle = 2 * math.pi * i / number_of_points
        x = center[0] + radius * math.cos(angle)
        y = center[1] + radius * math.sin(angle)
        points.append((x, y))
    return gdspy.Polygon(points, layer=layer)

# Create and add the circle to the cell
circle = create_circle(radius, center, layer)
cell.add(circle)

# Write the layout to a GDS file
lib.write_gds('circle_layout.gds')

# View the layout using an internal viewer (optional)