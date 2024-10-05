import gdspy

# Define the design specifications
unit = 1.0e-6  # Convert dimensions from microns to meters
active_region_width = 20 * unit
active_region_height = 5 * unit
active_region_spacing = 5 * unit
poly_gate_width = 0.5 * unit
contact_hole_size = 1 * unit

# Define the library and cell for the GDS layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell("layout")

# Create the three active regions
active_regions = []
for i in range(3):
    x = i * (active_region_width + active_region_spacing)
    active_region = gdspy.Rectangle([x, 0], [x + active_region_width, active_region_height])
    active_regions.append(active_region)
    cell.add(active_regions[-1])

# Create the polysilicon gate pattern
poly_gate_pattern = []
for i in range(5):
    x = i * poly_gate_width
    poly_gate_line = gdspy.Rectangle([x, 0], [x + poly_gate_width, 10 * unit], width=poly_gate_width)
    poly_gate_pattern.append(poly_gate_line)
    cell.add(poly_gate_pattern[-1])
    y = i * poly_gate_width
    poly_gate_line = gdspy.Rectangle([0, y], [10 * unit, y + poly_gate_width], width=poly_gate_width)
    poly_gate_pattern.append(poly_gate_line)
    cell.add(poly_gate_pattern[-1])

# Create the contact holes
contact_holes = []
for i in range(3):
    for j in range(5):
        x = i * (active_region_width + active_region_spacing) + active_region_width / 2
        y = j * poly_gate_width + poly_gate_width / 2
        contact_hole = gdspy.Rectangle([x - contact_hole_size / 2, y - contact_hole_size / 2], 
                                       [x + contact_hole_size / 2, y + contact_hole_size / 2])
        contact_holes.append(contact_hole)
        cell.add(contact_holes[-1])

# Save the design to a GDS file
lib.write_gds("layout.gds", cells=[cell], unit=1.0e-6, precision=1.0e-9)