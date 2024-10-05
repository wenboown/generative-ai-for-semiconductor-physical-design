import gdspy

# Define parameters (in micrometers)
total_length = 10000  # 10 mm
head_length = 3000    # 3 mm
body_length = 7000    # 7 mm
head_width = 3000     # 3 mm
body_width = 1000     # 1 mm

# Create a new library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell("ARROW")

# Create the arrow body
body = gdspy.Rectangle((0, -body_width/2), (body_length, body_width/2))

# Create the arrow head
head_points = [
    (body_length, -head_width/2),
    (total_length, 0),
    (body_length, head_width/2),
    (body_length, -head_width/2)
]
head = gdspy.Polygon(head_points)

# Add both shapes to the cell
cell.add(body)
cell.add(head)

# Save the design to a GDS file
lib.write_gds("arrow.gds")

# Optional: View the layout