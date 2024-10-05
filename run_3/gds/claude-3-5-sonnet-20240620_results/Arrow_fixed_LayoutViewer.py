import gdspy

# Create a new library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('ARROW')

# Define the arrow dimensions (in micrometers)
total_length = 10000  # 10 mm
head_length = 2500    # 2.5 mm
body_length = 7500    # 7.5 mm
head_width = 1500     # 1.5 mm
body_width = 500      # 0.5 mm

# Create the arrow body
body = gdspy.Rectangle((0, -body_width/2), (body_length, body_width/2))

# Create the arrow head
head_points = [
    (body_length, 0),
    (total_length, head_width/2),
    (total_length, -head_width/2)
]
head = gdspy.Polygon(head_points)

# Add both shapes to the cell
cell.add(body)
cell.add(head)

# Save the design to a GDS file
lib.write_gds('arrow.gds')

# Optional: View the layout