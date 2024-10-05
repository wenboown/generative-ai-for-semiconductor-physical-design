import gdspy

# Define the GDS library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('FinFET')

# Define the layers
FIN_LAYER = (1, 0)  # Layer 1, datatype 0
GATE_LAYER = (2, 0)  # Layer 2, datatype 0
SD_LAYER = (3, 0)  # Layer 3, datatype 0

# Fin dimensions
fin_width = 0.1  # µm
fin_height = 0.2  # µm
fin_length = 1.0  # µm

# Fin coordinates
fin_x1 = 0
fin_y1 = -fin_height / 2
fin_x2 = fin_length
fin_y2 = fin_y1 + fin_height

# Create the fin shape
fin = gdspy.Rectangle((fin_x1, fin_y1), (fin_x2, fin_y2), FIN_LAYER)
cell.add(fin)

# Gate dimensions
gate_length = 0.1  # µm

# Gate coordinates
gate_x1 = (fin_length - gate_length) / 2
gate_y1 = fin_y2 + 0.1  # Add a small gap between the fin and gate
gate_x2 = gate_x1 + gate_length
gate_y2 = gate_y1 + 0.2  # Gate height

# Create the gate shape
gate = gdspy.Rectangle((gate_x1, gate_y1), (gate_x2, gate_y2), GATE_LAYER)
cell.add(gate)

# Source/drain dimensions
sd_length = 0.4  # µm
sd_extension = 0.2  # µm

# Source coordinates
source_x1 = fin_x1 - sd_extension
source_y1 = fin_y1
source_x2 = source_x1 + sd_length
source_y2 = source_y1 + fin_height

# Create the source shape
source = gdspy.Rectangle((source_x1, source_y1), (source_x2, source_y2), SD_LAYER)
cell.add(source)

# Drain coordinates
drain_x1 = fin_x2 + sd_extension - sd_length
drain_y1 = fin_y1
drain_x2 = drain_x1 + sd_length
drain_y2 = drain_y1 + fin_height

# Create the drain shape
drain = gdspy.Rectangle((drain_x1, drain_y1), (drain_x2, drain_y2), SD_LAYER)
cell.add(drain)

# Save the design to a GDS file
lib.write_gds('finfet.gds')