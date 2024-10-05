import gdspy

# Create a new library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('FinFET')

# Define the layers for the fin, gate, and source/drain regions
fin_layer = 1
gate_layer = 2
source_drain_layer = 3

# Define the design specifications
fin_width = 0.1
fin_height = 0.2
fin_length = 1.0
gate_length = 0.1
source_drain_length = 0.4
source_drain_extension = 0.2

# Create the fin rectangle
fin = gdspy.Rectangle((0, 0), (fin_length, fin_height), layer=fin_layer)
cell.add(fin)

# Create the gate rectangle
gate_x = (fin_length - gate_length) / 2
gate = gdspy.Rectangle((gate_x, 0), (gate_x + gate_length, fin_height), layer=gate_layer)
cell.add(gate)

# Create the source and drain rectangles
source = gdspy.Rectangle((-source_drain_extension, 0), (source_drain_length + source_drain_extension, fin_height), layer=source_drain_layer)
drain = gdspy.Rectangle((fin_length - source_drain_length - source_drain_extension, 0), (fin_length + source_drain_extension, fin_height), layer=source_drain_layer)
cell.add(source)
cell.add(drain)

# Save the design to a GDS file
lib.write_gds('FinFET.gds')