import gdspy

# Define the specifications
fin_width = 0.1
fin_height = 0.2
fin_length = 1.0
gate_length = 0.1
source_drain_length = 0.4
source_drain_extension = 0.2

# Create a new GDS library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('FinFET')

# Create the fin
fin_layer = lib.new_layer(1, 'Fin')
fin = gdspy.Rectangle((0, 0), (fin_length, fin_height), layer=fin_layer)
cell.add(fin)

# Create the gate
gate_layer = lib.new_layer(2, 'Gate')
gate = gdspy.Rectangle((fin_length/2 - gate_length/2, -gate_length/2), (fin_length/2 + gate_length/2, gate_length/2), layer=gate_layer)
cell.add(gate)

# Create the source/drain regions
source_drain_layer = lib.new_layer(3, 'Source/Drain')
source = gdspy.Rectangle((-source_drain_length/2 - source_drain_extension, 0), (source_drain_extension, fin_height), layer=source_drain_layer)
drain = gdspy.Rectangle((fin_length - source_drain_extension, 0), (fin_length + source_drain_length/2 + source_drain_extension, fin_height), layer=source_drain_layer)
cell.add(source)
cell.add(drain)

# Save the design to a GDS file
lib.write_gds('FinFET.gds')