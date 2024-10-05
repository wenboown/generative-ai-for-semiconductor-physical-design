import gdspy

# Define the library and cell for the GDS layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell('design')

# Define the layer numbers and datatype for active regions, polysilicon gate, and contact holes
active_layer = (1, 0)
polysilicon_gate_layer = (2, 0)
contact_hole_layer = (3, 0)

# Draw three rectangular active regions with dimensions 20 µm x 5 µm
for i in range(3):
    active_region = gdspy.Rectangle((i * 25, 0), ((i * 25) + 20, 5), layer=active_layer[0], datatype=active_layer[1])
    cell.add(active_region)

# Create a complex polysilicon gate pattern consisting of multiple vertical and horizontal lines
for i in range(5):
    for j in range(3):
        # Draw horizontal lines
        polysilicon_gate_h = gdspy.Rectangle((j * 25 + 2.5, i * 2.5), ((j * 25) + 17.5, (i * 2.5) + 0.5), layer=polysilicon_gate_layer[0], datatype=polysilicon_gate_layer[1])
        cell.add(polysilicon_gate_h)
        
        # Draw vertical lines
        polysilicon_gate_v = gdspy.Rectangle((j * 25 + (i * 5), 2.5), ((j * 25) + (i * 5) + 0.5, 2.5 + 12.5), layer=polysilicon_gate_layer[0], datatype=polysilicon_gate_layer[1])
        cell.add(polysilicon_gate_v)

# Add several contact holes (each 1 µm x 1 µm) positioned at the intersections of the polysilicon gate pattern and the active regions
for i in range(5):
    for j in range(3):
        contact_hole = gdspy.Rectangle((j * 25 + (i * 5), 2.5 + (i * 2.5)), ((j * 25) + (i * 5) + 1, 2.5 + (i * 2.5) + 1), layer=contact_hole_layer[0], datatype=contact_hole_layer[1])
        cell.add(contact_hole)

# Save the design to a GDS file
lib.write_gds('design.gds')