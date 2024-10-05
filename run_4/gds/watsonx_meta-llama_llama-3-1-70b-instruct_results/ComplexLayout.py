import gdspy

# Define the GDS library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('layout_design')

# Draw three rectangular active regions
active_region_width = 20
active_region_height = 5
spacing = 5
active_region_layer = 1

for i in range(3):
    x = i * (active_region_width + spacing)
    y = 0
    active_region = gdspy.Rectangle((x, y), (x + active_region_width, y + active_region_height), layer=active_region_layer)
    cell.add(active_region)

# Create a complex polysilicon gate pattern
poly_gate_width = 0.5
poly_gate_layer = 2
gate_period = 5

# Vertical lines
for i in range(10):
    x = i * gate_period
    y = 0
    polygon = gdspy.Rectangle((x, y), (x + poly_gate_width, active_region_height), layer=poly_gate_layer)
    cell.add(polygon)

# Horizontal lines
for i in range(5):
    x = 0
    y = i * gate_period
    polygon = gdspy.Rectangle((x, y), (active_region_width * 3 + spacing * 2, y + poly_gate_width), layer=poly_gate_layer)
    cell.add(polygon)

# Add contact holes at intersections
contact_hole_size = 1
contact_hole_layer = 3

# Contact holes at vertical lines
for i in range(10):
    x = i * gate_period
    y = active_region_height / 2
    contact_hole = gdspy.Rectangle((x - contact_hole_size / 2, y - contact_hole_size / 2), (x + contact_hole_size / 2, y + contact_hole_size / 2), layer=contact_hole_layer)
    cell.add(contact_hole)

# Contact holes at horizontal lines
for i in range(5):
    x = active_region_width / 2 + spacing
    y = i * gate_period
    contact_hole = gdspy.Rectangle((x - contact_hole_size / 2, y - contact_hole_size / 2), (x + contact_hole_size / 2, y + contact_hole_size / 2), layer=contact_hole_layer)
    cell.add(contact_hole)

# Save the design to a GDS file
lib.write_gds('layout_design.gds')