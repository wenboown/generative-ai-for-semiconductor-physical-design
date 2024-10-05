import gdspy

# Define the design requirements
arrow_length = 10  # mm
head_width = 1  # mm
body_width = head_width / 3  # mm
start_x, start_y = 0, 0  # Starting coordinates

# Create a new GDS library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('arrow')

# Calculate the arrow head coordinates
head_length = arrow_length / 5
head_points = [
    (start_x + arrow_length, start_y - head_width / 2),
    (start_x + arrow_length - head_length, start_y),
    (start_x + arrow_length, start_y + head_width / 2),
    (start_x + arrow_length - head_length, start_y)
]

# Create the arrow head polygon
head_polygon = gdspy.Polygon(points=head_points, layer=0)
cell.add(head_polygon)

# Create the arrow body rectangle
body_rectangle = gdspy.Rectangle(
    (start_x, start_y - body_width / 2),
    (start_x + arrow_length - head_length, start_y + body_width / 2),
    layer=0
)
cell.add(body_rectangle)

# Save the design to a GDS file
lib.write_gds('arrow.gds')