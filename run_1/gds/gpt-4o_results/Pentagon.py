import gdspy
import math

# Create a new GDSII library, name 'pentagon'
gdsii_lib = gdspy.GdsLibrary()

# Create a new cell called 'PENTAGON'
cell = gdsii_lib.new_cell('PENTAGON')

# Define the pentagon parameters
edge_length = 10  # in mm
center = (0, 0)

# Calculate the radius of the circumscribed circle
radius = edge_length / (2 * math.sin(math.pi / 5))

# Define points for the regular pentagon
num_sides = 5
points = []
for i in range(num_sides):
    angle = i * (2 * math.pi / num_sides)  # Divide the circle into 5 parts
    x = center[0] + radius * math.cos(angle)
    y = center[1] + radius * math.sin(angle)
    points.append((x, y))

# Create the polygon
pentagon = gdspy.Polygon(points)

# Add the polygon to the cell
cell.add(pentagon)

# Save the GDS file
gdsii_lib.write_gds('pentagon.gds')

print("Pentagon GDS file created successfully.")