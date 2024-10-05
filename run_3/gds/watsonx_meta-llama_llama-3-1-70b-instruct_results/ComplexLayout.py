import gdspy

# Define the layer and cell for the GDS layout
lib = gdspy.Library()
cell = lib.new_cell("layout")

# Define parameters
active_region_width = 20
active_region_height = 5
active_region_spacing = 5
gate_width = 0.5
contact_size = 1

# Draw three rectangular active regions
x_start = 0
for i in range(3):
    active_region = gdspy.Rectangle(
        (x_start, 0), (x_start + active_region_width, active_region_height)
    )
    cell.add(active_region)
    x_start += active_region_width + active_region_spacing

# Create the polysilicon gate pattern
gate_x_start = 0
gate_y_start = active_region_height
gate_columns = 10
gate_rows = 10
gate_pitch = active_region_height / (gate_rows - 1)
for i in range(gate_rows):
    horizontal_gate = gdspy.Rectangle(
        (gate_x_start, gate_y_start + i * gate_pitch),
        (gate_x_start + active_region_width * 3 + active_region_spacing * 2, gate_y_start + i * gate_pitch + gate_width),
        layer=2  # Layer 2 for polysilicon
    )
    cell.add(horizontal_gate)

for i in range(gate_columns):
    vertical_gate = gdspy.Rectangle(
        (gate_x_start + i * gate_pitch, gate_y_start),
        (gate_x_start + i * gate_pitch + gate_width, gate_y_start + active_region_height),
        layer=2  # Layer 2 for polysilicon
    )
    cell.add(vertical_gate)

# Add contact holes at intersections
contact_layer = 3  # Layer 3 for contacts
for i in range(gate_columns):
    for j in range(gate_rows):
        if i < gate_columns - 1 and j < gate_rows - 1:
            contact_x = gate_x_start + i * gate_pitch
            contact_y = gate_y_start + j * gate_pitch
            contact = gdspy.Rectangle(
                (contact_x, contact_y), (contact_x + contact_size, contact_y + contact_size),
                layer=contact_layer
            )
            cell.add(contact)

# Save the design to a GDS file
lib.write_gds("layout.gds")