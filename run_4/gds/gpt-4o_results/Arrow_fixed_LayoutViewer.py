import gdspy

# Define units (1 unit = 1 um; precision = 1 nm)
gdsii_unit = 1e-6
precision = 1e-9

# Create a new GDSII Library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('ARROW')

# Dimensions in micrometers (um)
length = 10000  # 10 mm
head_width = 3000  # Arbitrary width for the head
body_width = head_width / 3

# Coordinates for the arrow polygon (initially an open arrow to illustrate points)
arrow_points = [
    (0, body_width / 2),
    (length - head_width, body_width / 2),
    (length - head_width, head_width / 2),
    (length, 0),
    (length - head_width, -head_width / 2),
    (length - head_width, -body_width / 2),
    (0, -body_width / 2)
]

# Create the arrow polygon
arrow = gdspy.Polygon(arrow_points, layer=0)

# Add the polygon to the cell
cell.add(arrow)

# Write the GDSII file
lib.write_gds('arrow.gds')

# Optionally, view the layout using gdspy internal viewer