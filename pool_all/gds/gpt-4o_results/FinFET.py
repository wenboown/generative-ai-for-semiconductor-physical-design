import gdspy

# Specifications
fin_width = 0.1
fin_height = 0.2
fin_length = 1.0
gate_length = 0.1
source_drain_length = 0.4
source_drain_extension = 0.2

# Create a library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('FinFET')

# Layers
fin_layer = 1
gate_layer = 2
source_drain_layer = 3

# Create Fin
fin = gdspy.Rectangle((0, 0), (fin_length, fin_height), layer=fin_layer)
cell.add(fin)

# Create Gate, centered on the fin
gate_x = (fin_length - gate_length) / 2
gate = gdspy.Rectangle((gate_x, -fin_width), (gate_x + gate_length, fin_height + fin_width), layer=gate_layer)
cell.add(gate)

# Create Source
source = gdspy.Rectangle((-source_drain_extension, -fin_width), (0, fin_height + fin_width), layer=source_drain_layer)
cell.add(source)

# Create Drain
drain = gdspy.Rectangle((fin_length, -fin_width), 
                        (fin_length + source_drain_extension, fin_height + fin_width), 
                        layer=source_drain_layer)
cell.add(drain)

# Save the design to a GDS file
lib.write_gds('finfet_layout.gds')