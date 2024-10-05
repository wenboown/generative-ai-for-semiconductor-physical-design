import gdspy

# Create a new library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('MAIN')

# 1. Draw three rectangular active regions
active_width = 20
active_height = 5
active_spacing = 5

for i in range(3):
    x = i * (active_width + active_spacing)
    active = gdspy.Rectangle((x, 0), (x + active_width, active_height))
    cell.add(active)

# 2. Create complex polysilicon gate pattern
gate_width = 0.5
gate_spacing = 5
total_width = 3 * active_width + 2 * active_spacing
total_height = active_height

# Vertical lines
for x in range(0, int(total_width) + 1, gate_spacing):
    gate_v = gdspy.Path(gate_width, (x, 0))
    gate_v.segment(total_height, '+y')
    cell.add(gate_v)

# Horizontal lines
for y in range(0, int(total_height) + 1, gate_spacing):
    gate_h = gdspy.Path(gate_width, (0, y))
    gate_h.segment(total_width, '+x')
    cell.add(gate_h)

# 3. Add contact holes at intersections
contact_size = 1

for x in range(0, int(total_width) + 1, gate_spacing):
    for y in range(0, int(total_height) + 1, gate_spacing):
        # Check if the contact is within an active region
        active_index = x // (active_width + active_spacing)
        if 0 <= active_index < 3 and active_index * (active_width + active_spacing) <= x < (active_index + 1) * active_width + active_index * active_spacing:
            contact = gdspy.Rectangle((x - contact_size/2, y - contact_size/2),
                                      (x + contact_size/2, y + contact_size/2))
            cell.add(contact)

# Save the layout to a GDS file
lib.write_gds('layout.gds')

# Optional: View the layout