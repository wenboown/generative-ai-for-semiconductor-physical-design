import gdspy

# Design specifications
fin_width = 0.1
fin_height = 0.2
fin_length = 1.0
gate_length = 0.1
source_drain_length = 0.4
source_drain_extension = 0.2

# Create a new library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('FinFET')

# Define layers
fin_layer = 1
gate_layer = 2
sd_layer = 3

# Create the fin
fin = gdspy.Rectangle((0, -fin_width/2), (fin_length, fin_width/2), layer=fin_layer)
cell.add(fin)

# Create the gate
gate_x = (fin_length - gate_length) / 2
gate = gdspy.Rectangle(
    (gate_x, -fin_height/2 - source_drain_extension),
    (gate_x + gate_length, fin_height/2 + source_drain_extension),
    layer=gate_layer
)
cell.add(gate)

# Create source and drain
source = gdspy.Rectangle(
    (-source_drain_extension, -fin_width/2 - source_drain_extension),
    (source_drain_length, fin_width/2 + source_drain_extension),
    layer=sd_layer
)
cell.add(source)

drain = gdspy.Rectangle(
    (fin_length - source_drain_length, -fin_width/2 - source_drain_extension),
    (fin_length + source_drain_extension, fin_width/2 + source_drain_extension),
    layer=sd_layer
)
cell.add(drain)

# Save the design to a GDS file
lib.write_gds('finfet_layout.gds')