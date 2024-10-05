import gdspy

# Define the key dimensions
arrow_length = 10.0e3  # 10 mm in micrometers
head_width = 3.0e3  # 3 mm in micrometers
body_width = head_width / 3  # 1/3 of the head width
arrow_head_length = 2.0e3  # Arbitrary length for the arrow head

# Create a new GDSII library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('ARROW')

# Coordinates for the arrow body (rectangle)
body_points = [
    (0, head_width / 2 - body_width / 2),  # Bottom-left corner
    (arrow_length - arrow_head_length, head_width / 2 - body_width / 2),  # Bottom-right before head
    (arrow_length - arrow_head_length, -head_width / 2 + body_width / 2),  # Top-right before head
    (0, -head_width / 2 + body_width / 2)  # Top-left corner
]

# Coordinates for the arrow head (triangle)
head_points = [
    (arrow_length - arrow_head_length, head_width / 2),  # Left vertex
    (arrow_length, 0),  # Right vertex (tip)
    (arrow_length - arrow_head_length, -head_width / 2)  # Left bottom vertex
]

# Create the body and head polygons
body_polygon = gdspy.Polygon(body_points)
head_polygon = gdspy.Polygon(head_points)

# Add polygons to the cell
cell.add(body_polygon)
cell.add(head_polygon)

# Save the GDS file
lib.write_gds('arrow_layout.gds')

# Optionally display layout using gdspy internal viewer