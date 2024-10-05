import gdspy

# Create a new GDSII library with units in micrometers
lib = gdspy.GdsLibrary(unit=1e-6, precision=1e-9)

# Create a cell for the FinFET design
cell = lib.new_cell('FinFET')

# Specifications
fin_width = 0.1        # µm
fin_length = 1.0       # µm
gate_length = 0.1      # µm
sd_length = 0.4        # µm
sd_extension = 0.2     # µm (extension beyond the fin in Y-direction)

# Layers
fin_layer = 1
gate_layer = 2
sd_layer = 3

# Fin coordinates
fin_coords = [(0, 0), (fin_length, fin_width)]

# Create the fin rectangle
fin = gdspy.Rectangle(fin_coords[0], fin_coords[1], layer=fin_layer)
cell.add(fin)

# Gate coordinates (centered at fin_length / 2)
gate_x0 = (fin_length - gate_length) / 2
gate_x1 = gate_x0 + gate_length
gate_y0 = -sd_extension
gate_y1 = fin_width + sd_extension
gate_coords = [(gate_x0, gate_y0), (gate_x1, gate_y1)]

# Create the gate rectangle
gate = gdspy.Rectangle(gate_coords[0], gate_coords[1], layer=gate_layer)
cell.add(gate)

# Source coordinates
source_x0 = 0
source_x1 = sd_length
source_y0 = -sd_extension
source_y1 = fin_width + sd_extension
source_coords = [(source_x0, source_y0), (source_x1, source_y1)]

# Create the source rectangle
source = gdspy.Rectangle(source_coords[0], source_coords[1], layer=sd_layer)
cell.add(source)

# Drain coordinates
drain_x0 = fin_length - sd_length
drain_x1 = fin_length
drain_y0 = -sd_extension
drain_y1 = fin_width + sd_extension
drain_coords = [(drain_x0, drain_y0), (drain_x1, drain_y1)]

# Create the drain rectangle
drain = gdspy.Rectangle(drain_coords[0], drain_coords[1], layer=sd_layer)
cell.add(drain)

# Save the design to a GDS file
lib.write_gds('finfet.gds')