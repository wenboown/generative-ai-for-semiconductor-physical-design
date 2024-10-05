import gdspy

# Initialize the GDSII layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell('ARROW_RIGHT')

# Define the arrow dimensions
length = 10000  # 10 mm in microns (1000 microns = 1 mm)
head_width = 10000 / 3  # 1/3 of the head length
body_width = head_width / 3  # 1/3 width of head

# Arrow body coordinates (a rectangle)
x0, y0 = 0, head_width / 3
x1, y1 = length - head_width, y0
x2, y2 = x1, y0 + body_width
x3, y3 = x0, x2

arrow_body = gdspy.Rectangle((x0, y0), (x2, y2))

# Arrow head coordinates (a closed polygon)
h0, k0 = length - head_width, 0
h1, k1 = length, head_width / 2
h2, k2 = length - head_width, head_width

arrow_head = gdspy.Polygon([(h0, k0), (h1, k1), (h2, k2)])

# Add arrow body and head to the cell
cell.add(arrow_body)
cell.add(arrow_head)

# Save the design to a GDS file
lib.write_gds('arrow.gds')

print("Arrow layout has been saved to 'arrow.gds'")