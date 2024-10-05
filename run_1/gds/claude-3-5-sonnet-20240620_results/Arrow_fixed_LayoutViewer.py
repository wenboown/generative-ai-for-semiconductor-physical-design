import gdspy
import numpy as np

# Create a new library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('ARROW')

# Define arrow dimensions (in micrometers)
arrow_length = 10000  # 10 mm = 10000 μm
body_length = arrow_length * 0.7  # 70% of total length for the body
head_length = arrow_length - body_length
head_width = 2000  # Arbitrary width, adjust as needed
body_width = head_width / 3

# Create arrow body
body = gdspy.Rectangle((0, -body_width/2), (body_length, body_width/2))

# Create arrow head
head_points = [
    (body_length, -head_width/2),
    (arrow_length, 0),
    (body_length, head_width/2),
    (body_length, -head_width/2)
]
head = gdspy.Polygon(head_points)

# Add both shapes to the cell
cell.add(body)
cell.add(head)

# Save the design to a GDS file
lib.write_gds('arrow.gds')

# Optional: View the layout