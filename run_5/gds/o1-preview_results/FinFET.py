import gdspy

# Create the GDSII library
lib = gdspy.GdsLibrary()

# Create a cell for the FinFET
cell = lib.new_cell('FinFET')

# Define layers
FIN_LAYER = 1
GATE_LAYER = 2
SOURCE_DRAIN_LAYER = 3

# Fin dimensions and coordinates (Layer 1)
fin_width = 0.1  # µm
fin_length = 1.0  # µm
fin = gdspy.Rectangle(
    (0, 0),
    (fin_length, fin_width),
    layer=FIN_LAYER
)
cell.add(fin)

# Gate dimensions and coordinates (Layer 2)
gate_length = 0.1  # µm
gate_extension_y = 0.1  # Extension beyond fin in y-direction
gate_y_min = -gate_extension_y
gate_y_max = fin_width + gate_extension_y

# Adjust positions to center the device within the fin length
sd_length = 0.4   # Source/Drain length (µm)
device_total_length = 2 * sd_length + gate_length  # Total device length (µm)
fin_padding = (fin_length - device_total_length) / 2  # Padding to center the device (µm)

source_x_start = fin_padding
source_x_end = source_x_start + sd_length

gate_x_start = source_x_end
gate_x_end = gate_x_start + gate_length

drain_x_start = gate_x_end
drain_x_end = drain_x_start + sd_length

# Gate rectangle
gate = gdspy.Rectangle(
    (gate_x_start, gate_y_min),
    (gate_x_end, gate_y_max),
    layer=GATE_LAYER
)
cell.add(gate)

# Source/Drain dimensions and coordinates (Layer 3)
sd_extension_y = 0.2  # Extension beyond fin in y-direction (µm)
sd_y_min = -sd_extension_y
sd_y_max = fin_width + sd_extension_y

# Source region
source = gdspy.Rectangle(
    (source_x_start, sd_y_min),
    (source_x_end, sd_y_max),
    layer=SOURCE_DRAIN_LAYER
)
cell.add(source)

# Drain region
drain = gdspy.Rectangle(
    (drain_x_start, sd_y_min),
    (drain_x_end, sd_y_max),
    layer=SOURCE_DRAIN_LAYER
)
cell.add(drain)

# Save the GDSII file
lib.write_gds('finfet.gds')