import gdspy

# Create a new library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('MAIN')

# 1. Create three rectangular active regions
active_width = 20
active_height = 5
active_spacing = 5

for i in range(3):
    x = i * (active_width + active_spacing)
    active = gdspy.Rectangle((x, 0), (x + active_width, active_height))
    cell.add(active)

# 2. Create complex polysilicon gate pattern
poly_width = 0.5
total_width = 3 * active_width + 2 * active_spacing
total_height = active_height

# Vertical lines
for x in range(0, int(total_width) + 1, 5):
    poly_line = gdspy.Path(poly_width, (x, 0))
    poly_line.segment(total_height, '+y')
    cell.add(poly_line)

# Horizontal lines
for y in range(0, int(total_height) + 1, 5):
    poly_line = gdspy.Path(poly_width, (0, y))
    poly_line.segment(total_width, '+x')
    cell.add(poly_line)

# 3. Add contact holes
contact_size = 1

for x in range(0, int(total_width) + 1, 5):
    for y in range(0, int(total_height) + 1, 5):
        # Check if the contact is within an active region
        region_index = x // (active_width + active_spacing)
        if region_index < 3:
            region_start = region_index * (active_width + active_spacing)
            if region_start <= x < region_start + active_width:
                contact = gdspy.Rectangle(
                    (x - contact_size/2, y - contact_size/2),
                    (x + contact_size/2, y + contact_size/2)
                )
                cell.add(contact)

# Save the design to a GDS file
lib.write_gds('layout_design.gds')

# Optional: View the layout