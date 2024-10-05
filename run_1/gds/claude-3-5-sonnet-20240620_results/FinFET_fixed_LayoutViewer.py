import gdspy

# Step 1: Set up the library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell("FinFET")

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

# Calculate center coordinates
center_x = 0
center_y = 0

# Calculate fin coordinates
fin_x = center_x - fin_width / 2
fin_y = center_y - fin_length / 2

# Calculate gate coordinates
gate_x = center_x - gate_length / 2
gate_y = center_y - (fin_length / 2 + sd_extension)

# Calculate source/drain coordinates
sd_x = center_x - (fin_width / 2 + sd_extension)
sd_y = center_y - (fin_length / 2 + sd_length)

# Step 4: Create rectangles for fin, gate, and source/drain regions
fin = gdspy.Rectangle((fin_x, fin_y), (fin_x + fin_width, fin_y + fin_length), layer=layer_fin)

gate = gdspy.Rectangle(
    (gate_x, gate_y),
    (gate_x + gate_length, gate_y + fin_length + 2 * sd_extension),
    layer=layer_gate
)

source = gdspy.Rectangle(
    (sd_x, sd_y),
    (sd_x + fin_width + 2 * sd_extension, sd_y + sd_length),
    layer=layer_sd
)

drain = gdspy.Rectangle(
    (sd_x, sd_y + fin_length + sd_length),
    (sd_x + fin_width + 2 * sd_extension, sd_y + fin_length + 2 * sd_length),
    layer=layer_sd
)

# Step 5: Add all elements to the cell
cell.add(fin)
cell.add(gate)
cell.add(source)
cell.add(drain)

# Step 6: Save the design to a GDS file
lib.write_gds("finfet_layout.gds")

# Optional: View the layout