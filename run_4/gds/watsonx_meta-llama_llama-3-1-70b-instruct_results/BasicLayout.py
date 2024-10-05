import gdspy

# Step 1: Parse the user’s design specifications and define the library and cell for the GDS layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell('layout')

# Step 2: Draw the rectangular active region with dimensions 10 µm x 5 µm
active_region = gdspy.Rectangle((0, 0), (10, 5), layer=1)
cell.add(active_region)

# Step 3: Place the polysilicon gate that crosses the active region vertically at its center
gate_center = (5, 2.5)  # Center of the active region
gate = gdspy.Rectangle((gate_center[0] - 0.5, gate_center[1] - 2.5), (gate_center[0] + 0.5, gate_center[1] + 2.5), layer=2)
cell.add(gate)

# Step 4: Add two square contact holes, each 1 µm x 1 µm, positioned 1 µm away from the gate on either side along the active region
contact_hole1 = gdspy.Rectangle((gate_center[0] - 1.5, gate_center[1] - 0.5), (gate_center[0] - 0.5, gate_center[1] + 0.5), layer=3)
cell.add(contact_hole1)
contact_hole2 = gdspy.Rectangle((gate_center[0] + 0.5, gate_center[1] - 0.5), (gate_center[0] + 1.5, gate_center[1] + 0.5), layer=3)
cell.add(contact_hole2)

# Step 5: Save the design to a GDS file
lib.write_gds('layout.gds')