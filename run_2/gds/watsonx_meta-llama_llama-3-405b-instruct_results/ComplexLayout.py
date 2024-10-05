import gdspy

# Define the library and cell for the GDS layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell('layout')

# Draw three rectangular active regions
active_region_width = 20
active_region_height = 5
active_region_spacing = 5

active_region_x = 0
for i in range(3):
    active_region = gdspy.Rectangle((active_region_x, 0), (active_region_x + active_region_width, active_region_height), layer=0)
    cell.add(active_region)
    active_region_x += active_region_width + active_region_spacing

# Create the complex polysilicon gate pattern
gate_width = 0.5
gate_x_min = 0
gate_x_max = active_region_x + active_region_width
gate_y_min = active_region_height + 2
gate_y_max = gate_y_min + 10

for x in [gate_x_min + i * 2 for i in range(int((gate_x_max - gate_x_min) / 2))]:
    gate_v = gdspy.Rectangle((x, gate_y_min), (x + gate_width, gate_y_max), layer=1)
    cell.add(gate_v)

for y in [gate_y_min + i * 2 for i in range(int((gate_y_max - gate_y_min) / 2))]:
    gate_h = gdspy.Rectangle((gate_x_min, y), (gate_x_max, y + gate_width), layer=1)
    cell.add(gate_h)

# Add contact holes
contact_hole_size = 1
for x in [active_region_x + active_region_width / 2 for active_region_x in [0, active_region_width + active_region_spacing, (active_region_width + active_region_spacing) * 2]]:
    for y in [gate_y_min + i * 2 for i in range(int((gate_y_max - gate_y_min) / 2))]:
        contact_hole = gdspy.Rectangle((x - contact_hole_size / 2, y - contact_hole_size / 2), (x + contact_hole_size / 2, y + contact_hole_size / 2), layer=2)
        cell.add(contact_hole)

# Save the design to a GDS file
lib.write_gds('layout.gds')