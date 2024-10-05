import gdspy

# Define the library and cell for the GDS layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell('arrow')

# Define the arrow's dimensions
length = 10  # mm
head_width = 2  # mm
body_width = head_width / 3

# Calculate the points for the arrow head
head_points = [(length, head_width/2), (length - head_width, -head_width/2), (length, -head_width/2)]

# Calculate the points for the arrow body
body_points = [(length - head_width, body_width/2), (0, body_width/2), (0, -body_width/2), (length - head_width, -body_width/2)]

# Create the arrow head polygon
head_polygon = gdspy.Polygon(head_points)

# Create the arrow body polygon
body_polygon = gdspy.Polygon(body_points)

# Add the polygons to the cell
cell.add(head_polygon)
cell.add(body_polygon)

# Save the design to a GDS file
lib.write_gds('arrow.gds')