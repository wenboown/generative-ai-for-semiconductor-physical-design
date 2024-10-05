import gdspy

# Define the library and cell for the GDS layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell('Arrow')

# Define the arrow dimensions
length = 10  # mm
head_width = 2  # mm
body_width = head_width / 3  # mm

# Create the arrow head
head = gdspy.Polygon([
    (length, head_width/2),
    (length+1, head_width/2),
    (length+0.5, head_width),
    (length+1, -head_width/2),
    (length, -head_width/2),
    (length-0.5, 0),
    (length, head_width/2)
], layer=0)

# Create the arrow body
body = gdspy.Polygon([
    (0, body_width/2),
    (0, -body_width/2),
    (length-1, -body_width/2),
    (length-1, body_width/2),
    (0, body_width/2)
], layer=0)

# Add the arrow head and body to the cell
cell.add(head)
cell.add(body)

# Save the design to a GDS file
lib.write_gds('arrow.gds')