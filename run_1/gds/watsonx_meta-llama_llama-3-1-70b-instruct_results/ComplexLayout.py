import gdspy

# Define the GDSII library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('layout')

# Define the geometry for the active regions
active_region_width = 20
active_region_height = 5
active_region_spacing = 5
num_active_regions = 3
active_region_y = 10
active_regions = []

for i in range(num_active_regions):
    x = i * (active_region_width + active_region_spacing)
    active-region = gdspy.Rectangle(
        (x, active_region_y),
        (x + active_region_width, active_region_y + active_region_height),
        layer=1
    )
    active_regions.append(active-region)
    cell.add(active-region)

# Define the geometry for the polysilicon gate pattern
gate_width = 0.5
gate_space = 1
x_start = 0
x_end = num_active_regions * (active_region_width + active_region_spacing)
num_horizontal_gates = int((x_end - x_start) / (gate_width + gate_space)) + 1
horizontal_gates = []

for i in range(num_horizontal_gates):
    x = x_start + i * (gate_width + gate_space)
    y = active_region_y - gate_width
    gate = gdspy.Rectangle(
        (x, y),
        (x + gate_width, y + gate_width),
        layer=2
    )
    horizontal_gates.append(gate)
    cell.add(gate)

    y = active_region_y + active_region_height
    gate = gdspy.Rectangle(
        (x, y),
        (x + gate_width, y + gate_width),
        layer=2
    )
    horizontal_gates.append(gate)
    cell.add(gate)

polysilicon_gate_x = [x_start, x_end]
polysilicon_gate_y = [active_region_y - gate_width, active_region_y + active_region_height]

for y in polysilicon_gate_y:
    for x in polysilicon_gate_x:
        gate = gdspy.Rectangle(
            (x, y),
            (x + gate_width, y + gate_width),
            layer=2
        )
        cell.add(gate)

# Define the geometry for the contact holes
contact_hole_size = 1
contact_holes = []

for active_region in active_regions:
    x = active_region.x
    y = active_region.y
    contact_hole = gdspy.Rectangle(
        (x, y),
        (x + contact_hole_size, y + contact_hole_size),
        layer=3
    )
    contact_holes.append(contact_hole)
    cell.add(contact_hole)

# Save the design to a GDS file
lib.write_gds('layout.gds')