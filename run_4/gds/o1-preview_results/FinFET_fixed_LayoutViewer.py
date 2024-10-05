import gdspy

# Create a new GDS library
lib = gdspy.GdsLibrary()

# Create a new cell for the FinFET
cell = lib.new_cell('FinFET')

# Specifications in microns
# Fin dimensions
fin_width = 0.1      # Fin width (W_fin)
fin_length = 1.0     # Fin length (L_fin)
fin_layer = 1        # Layer for the fin

# Gate dimensions
gate_length = 0.1    # Gate length (L_gate)
gate_extension = 0.2 # Extension beyond the fin in the width direction (W_gate_ext)
gate_layer = 2       # Layer for the gate

# Source/Drain dimensions
sd_length = 0.4           # Source/Drain length overlapping the fin (L_s_d)
sd_extension_length = 0.2 # Extension beyond the fin lengthwise (L_s_d_ext)
sd_extension_width = 0.2  # Extension beyond the fin widthwise (W_s_d_ext)
sd_layer = 3              # Layer for the source/drain

# Define the fin rectangle
fin = gdspy.Rectangle(
    (0, 0),
    (fin_length, fin_width),
    layer=fin_layer
)
cell.add(fin)

# Define the gate rectangle centered along the fin
gate_start_x = (fin_length / 2) - (gate_length / 2)
gate_end_x = (fin_length / 2) + (gate_length / 2)
gate_start_y = -gate_extension
gate_end_y = fin_width + gate_extension

gate = gdspy.Rectangle(
    (gate_start_x, gate_start_y),
    (gate_end_x, gate_end_y),
    layer=gate_layer
)
cell.add(gate)

# Define the source region
source_start_x = -sd_extension_length
source_end_x = sd_length
source_start_y = -sd_extension_width
source_end_y = fin_width + sd_extension_width

source = gdspy.Rectangle(
    (source_start_x, source_start_y),
    (source_end_x, source_end_y),
    layer=sd_layer
)
cell.add(source)

# Define the drain region
drain_start_x = fin_length - sd_length
drain_end_x = fin_length + sd_extension_length
drain_start_y = -sd_extension_width
drain_end_y = fin_width + sd_extension_width

drain = gdspy.Rectangle(
    (drain_start_x, drain_start_y),
    (drain_end_x, drain_end_y),
    layer=sd_layer
)
cell.add(drain)

# Save the layout to a GDS file
lib.write_gds('finfet.gds')

# Optionally, visualize the layout (requires matplotlib)