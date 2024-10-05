import gdspy

# Define the GDS file and library
gds_file = gdspy.GdsLibrary()

# Create a cell for the octagon
octagon_cell = gds_file.new_cell('octagon')

# Define the center coordinates
center_x, center_y = 0, 0

# Calculate the radius of the circumscribed circle
side_length = 10  # mm
radius = side_length / (2 * (1 - 0.5 * (1 + 1/4)))

# Define the vertices of the octagon
angles = [i * 45 for i in range(8)]  # 45 degrees between each vertex
x_coords = [center_x + radius * math.cos(math.radians(angle)) for angle in angles]
y_coords = [center_y + radius * math.sin(math.radians(angle)) for angle in angles]
vertices = list(zip(x_coords, y_coords))

# Create the octagon polygon
octagon_polygon = gdspy.Polygon(vertices)

# Add the polygon to the cell
octagon_cell.add(octagon_polygon)

# Save the layout to a GDS file
gds_file.write_gds('octagon.gds')