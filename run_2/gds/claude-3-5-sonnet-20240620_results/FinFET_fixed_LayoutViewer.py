import gdspy

# Step 1: Set up the library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('FinFET')

# Step 2: Define layers
layer_fin = 1
layer_gate = 2
layer_sd = 3

# Step 3: Calculate coordinates
fin_width = 0.1
fin_height = 0.2
fin_length = 1.0
gate_length = 0.1
sd_length = 0.4
sd_extension = 0.2

# Calculate center positions
center_x = 0
center_y = 0

# Calculate fin coordinates
fin_left = center_x - fin_width / 2
fin_right = center_x + fin_width / 2
fin_bottom = center_y - fin_length / 2
fin_top = center_y + fin_length / 2

# Calculate gate coordinates
gate_left = center_x - gate_length / 2
gate_right = center_x + gate_length / 2
gate_bottom = center_y - fin_length / 2 - sd_extension
gate_top = center_y + fin_length / 2 + sd_extension

# Calculate source/drain coordinates
sd_left = center_x - fin_width / 2 - sd_extension
sd_right = center_x + fin_width / 2 + sd_extension
source_bottom = center_y - fin_length / 2 - sd_length
source_top = center_y - fin_length / 2
drain_bottom = center_y + fin_length / 2
drain_top = center_y + fin_length / 2 + sd_length

# Step 4: Draw the fin structure
fin = gdspy.Rectangle((fin_left, fin_bottom), (fin_right, fin_top), layer=layer_fin)
cell.add(fin)

# Step 5: Draw the gate structure
gate = gdspy.Rectangle((gate_left, gate_bottom), (gate_right, gate_top), layer=layer_gate)
cell.add(gate)

# Step 6: Draw the source and drain regions
source = gdspy.Rectangle((sd_left, source_bottom), (sd_right, source_top), layer=layer_sd)
drain = gdspy.Rectangle((sd_left, drain_bottom), (sd_right, drain_top), layer=layer_sd)
cell.add(source)
cell.add(drain)

# Step 7: Save the design to a GDS file
lib.write_gds('finfet_layout.gds')

# Optional: View the layout