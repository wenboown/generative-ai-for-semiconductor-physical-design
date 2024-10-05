import gdspy

# Create a new GDSII library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('FinFET')

# Specifications
fin_width = 0.1           # Fin width in micrometers
fin_length = 1.0          # Fin length in micrometers
gate_length = 0.1         # Gate length in micrometers
source_drain_length = 0.4 # Source/drain length in micrometers
extension = 0.2           # Source/drain extension beyond the fin in micrometers

# Fin rectangle (Layer 1)
fin = gdspy.Rectangle((0, 0), (fin_length, fin_width), layer=1)
cell.add(fin)

# Gate rectangle (Layer 2)
# Gate is centered over the fin
gate_x0 = (fin_length - gate_length) / 2
gate_x1 = gate_x0 + gate_length
# Assume the gate extends beyond the fin in the y-direction
gate_y0 = -0.1  # Extending below the fin
gate_y1 = fin_width + 0.1  # Extending above the fin
gate = gdspy.Rectangle((gate_x0, gate_y0), (gate_x1, gate_y1), layer=2)
cell.add(gate)

# Source region (Layer 3)
source_x0 = -extension  # Extending beyond the fin
source_x1 = source_drain_length
source_y0 = 0
source_y1 = fin_width
source = gdspy.Rectangle((source_x0, source_y0), (source_x1, source_y1), layer=3)
cell.add(source)

# Drain region (Layer 3)
drain_x0 = fin_length - source_drain_length
drain_x1 = fin_length + extension  # Extending beyond the fin
drain_y0 = 0
drain_y1 = fin_width
drain = gdspy.Rectangle((drain_x0, drain_y0), (drain_x1, drain_y1), layer=3)
cell.add(drain)

# Save the layout to a GDSII file
lib.write_gds('finfet.gds')

# Optionally, view the layout (uncomment the line below if needed)