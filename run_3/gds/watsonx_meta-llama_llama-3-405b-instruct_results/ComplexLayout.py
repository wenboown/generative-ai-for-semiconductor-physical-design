import gdspy

# Define the library and cell for the GDS layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell('layout')

# Draw three rectangular active regions
active_region_width = 20
active_region_height = 5
active_region_spacing = 5
for i in range(3):
    x = i * (active_region_width + active_region_spacing)
    rect = gdspy.Rectangle((x, 0), (x + active_region_width, active_region_height), layer=1)
    cell.add(rect)

# Create a complex polysilicon gate pattern
gate_width = 0.5
gate_pitch = 5
num_vertical_gates = 10
num_horizontal_gates = 5
for i in range(num_vertical_gates):
    x = i * gate_pitch
    for j in range(num_horizontal_gates):
        y = j * gate_pitch
        # Vertical lines
        vline = gdspy.Rectangle((x, y), (x + gate_width, y + gate_pitch), layer=2)
        cell.add(vline)
        # Horizontal lines
        hline = gdspy.Rectangle((x, y), (x + gate_pitch, y + gate_width), layer=2)
        cell.add(hline)

# Add several contact holes at the intersections of the polysilicon gate pattern and the active regions
contact_size = 1
for i in range(num_vertical_gates):
    x = i * gate_pitch
    for j in range(num_horizontal_gates):
        y = j * gate_pitch
        # Check if contact hole is within an active region
        if x < (active_region_width + active_region_spacing) * 3 and y < active_region_height:
            contact = gdspy.Rectangle((x, y), (x + contact_size, y + contact_size), layer=3)
            cell.add(contact)

# Save the design to a GDS file
lib.write_gds('layout.gds')