import gdspy

# Define arrow dimensions (in micrometers)
arrow_length = 10000  # 10 mm
head_width = 3000  # 3 mm (arbitrary, can be adjusted)
body_width = head_width / 3
head_length = 2000  # 2 mm (arbitrary, can be adjusted)

# Create a new library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('ARROW')

# Define arrow polygon points
points = [
    (0, -body_width/2),
    (arrow_length - head_length, -body_width/2),
    (arrow_length - head_length, -head_width/2),
    (arrow_length, 0),
    (arrow_length - head_length, head_width/2),
    (arrow_length - head_length, body_width/2),
    (0, body_width/2)
]

# Create the arrow polygon
arrow = gdspy.Polygon(points)

# Add the arrow to the cell
cell.add(arrow)

# Save the design to a GDS file
lib.write_gds('arrow.gds')

print("Arrow GDS file has been created: arrow.gds")