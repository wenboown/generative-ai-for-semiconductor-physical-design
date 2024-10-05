import gdspy
import math

# Define the library and cell for the GDS layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell('pentagon')

# Parse the user's design specifications
edge_length = 10  # mm
center_x, center_y = 0, 0

# Calculate the coordinates for a regular pentagon
num_sides = 5
angle_step = 2 * math.pi / num_sides
points = []
for i in range(num_sides):
    angle = i * angle_step
    x = center_x + edge_length * math.cos(angle)
    y = center_y + edge_length * math.sin(angle)
    points.append((x * 1e6, y * 1e6))  # Convert to microns (GDS unit)

# Create a polygon element with precise coordinates
poly = gdspy.Polygon(points)

# Add the polygon to the cell and ensure correct placement
cell.add(poly)

# Save the design to a GDS file
lib.gdsii.write_gds('pentagon.gds')