import gdspy

# Create a new library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('LAYOUT')

# 1. Create three active regions
active_width = 20
active_height = 5
active_spacing = 5

for i in range(3):
    x = i * (active_width + active_spacing)
    active = gdspy.Rectangle((x, 0), (x + active_width, active_height))
    cell.add(active)

# 2. Create complex polysilicon gate pattern
gate_width = 0.5
gate_spacing = 4.5  # Adjust this value to create a suitable grid pattern
gate_length = 3 * active_width + 2 * active_spacing

# Vertical lines
for x in range(0, int(gate_length + gate_width), int(gate_width + gate_spacing)):
    gate_v = gdspy.Rectangle((x, -2.5), (x + gate_width, active_height + 2.5))
    cell.add(gate_v)

# Horizontal lines
for y in range(-2, int(active_height + 3), int(gate_width + gate_spacing)):
    gate_h = gdspy.Rectangle((0, y), (gate_length, y + gate_width))
    cell.add(gate_h)

# 3. Add contact holes
contact_size = 1

for i in range(3):
    active_x = i * (active_width + active_spacing)
    for x in range(int(active_x), int(active_x + active_width), int(gate_width + gate_spacing)):
        for y in range(0, int(active_height), int(gate_width + gate_spacing)):
            contact = gdspy.Rectangle((x, y), (x + contact_size, y + contact_size))
            cell.add(contact)

# Save the layout to a GDS file
lib.write_gds('layout.gds')

# Optional: View the layout