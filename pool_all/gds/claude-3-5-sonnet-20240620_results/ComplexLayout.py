import gdspy

# Create a new library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('LAYOUT')

# Define layer numbers
LAYER_ACTIVE = 1
LAYER_POLY = 2
LAYER_CONTACT = 3

# 1. Draw three rectangular active regions
active_width = 20
active_height = 5
active_spacing = 5

for i in range(3):
    x = i * (active_width + active_spacing)
    active = gdspy.Rectangle((x, 0), (x + active_width, active_height), layer=LAYER_ACTIVE)
    cell.add(active)

# 2. Create complex polysilicon gate pattern
poly_width = 0.5
total_width = 3 * active_width + 2 * active_spacing
total_height = active_height

# Vertical lines
for x in range(0, int(total_width + poly_width), 5):
    poly_vert = gdspy.Path(poly_width, (x, -2))
    poly_vert.segment(total_height + 4, '+y', layer=LAYER_POLY)
    cell.add(poly_vert)

# Horizontal lines
for y in range(-2, int(total_height + 3), 5):
    poly_horz = gdspy.Path(poly_width, (0, y))
    poly_horz.segment(total_width, '+x', layer=LAYER_POLY)
    cell.add(poly_horz)

# 3. Add contact holes at intersections
contact_size = 1

for i in range(3):
    x_start = i * (active_width + active_spacing)
    x_end = x_start + active_width
    for x in range(int(x_start), int(x_end + poly_width), 5):
        for y in range(0, int(active_height + poly_width), 5):
            contact = gdspy.Rectangle(
                (x - contact_size/2, y - contact_size/2),
                (x + contact_size/2, y + contact_size/2),
                layer=LAYER_CONTACT
            )
            cell.add(contact)

# Save the layout to a GDS file
lib.write_gds('layout.gds')