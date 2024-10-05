import gdspy

lib = gdspy.GdsLibrary()
cell = lib.new_cell('LAYOUT')
unit = 1.0e-6
precision = 1.0e-9
lib = gdspy.GdsLibrary(unit=unit, precision=precision)

# Dimensions and spacing
active_width = 20
active_height = 5
spacing = 5
gate_width = 0.5

# Draw three rectangular active regions
for i in range(3):
    x_offset = i * (active_width + spacing)
    active_region = gdspy.Rectangle((x_offset, 0), (x_offset + active_width, active_height))
    cell.add(active_region)

# Create complex polysilicon gate pattern
for x in range(-20, 70, 5):
    gate_v = gdspy.Rectangle((x, -2.5), (x + gate_width, 7.5))
    cell.add(gate_v)
for y in range(0, 20, 5):
    gate_h = gdspy.Rectangle((-2.5, y), (60, y + gate_width))
    cell.add(gate_h)

# Add several contact holes (1µm x 1µm) positioned at the intersections of the polysilicon gate pattern and active regions
contact_size = 1 
for x in [5, 25, 45]:
    for y in [2.5, 7.5, 12.5]:
        contact_hole = gdspy.Rectangle((x - contact_size/2, y - contact_size/2), (x + contact_size/2, y + contact_size/2))
        cell.add(contact_hole)

lib.write_gds('layout.gds')