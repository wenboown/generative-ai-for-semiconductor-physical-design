import gdspy

# Create a new library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('FinFET')

# Define layers
FIN_LAYER = 1
GATE_LAYER = 2
SD_LAYER = 3

# Define dimensions (in µm)
fin_width = 0.1
fin_height = 0.2
fin_length = 1.0
gate_length = 0.1
sd_length = 0.4
sd_extension = 0.2

# Calculate positions
fin_x = -fin_width / 2
fin_y = -fin_length / 2
gate_y = -gate_length / 2

# Create fin
fin = gdspy.Rectangle((fin_x, fin_y), (fin_x + fin_width, fin_y + fin_length), layer=FIN_LAYER)
cell.add(fin)

# Create gate
gate_width = fin_width + 2 * sd_extension
gate = gdspy.Rectangle((-gate_width/2, gate_y), (gate_width/2, gate_y + gate_length), layer=GATE_LAYER)
cell.add(gate)

# Create source and drain regions
sd_width = fin_width + 2 * sd_extension
source = gdspy.Rectangle((-sd_width/2, fin_y - sd_length), (sd_width/2, fin_y), layer=SD_LAYER)
drain = gdspy.Rectangle((-sd_width/2, fin_y + fin_length), (sd_width/2, fin_y + fin_length + sd_length), layer=SD_LAYER)
cell.add(source)
cell.add(drain)

# Save the layout to a GDS file
lib.write_gds('finfet_layout.gds')

# Optional: View the layout