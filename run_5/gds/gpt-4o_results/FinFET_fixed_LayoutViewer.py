import gdspy

# Design parameters
fin_width = 0.1
fin_height = 0.2
fin_length = 1.0
gate_length = 0.1
source_drain_length = 0.4
source_drain_extension = 0.2

# Create a new GDS library
lib = gdspy.GdsLibrary()

# Create a cell for the FinFET
cell = lib.new_cell('FinFET')

# Fin layer
fin_layer = 1
fin = gdspy.Rectangle((0, 0), (fin_length, fin_height), layer=fin_layer)
cell.add(fin)

# Gate layer
gate_layer = 2
# Gate position is in the middle of the fin along the length
gate_x = (fin_length - gate_length) / 2
gate = gdspy.Rectangle((gate_x, 0), (gate_x + gate_length, fin_height), layer=gate_layer)
cell.add(gate)

# Source/Drain layer
source_drain_layer = 3
# Source location at the left extension
source = gdspy.Rectangle(
    (gate_x - source_drain_length, -source_drain_extension),
    (gate_x, fin_height + source_drain_extension),
    layer=source_drain_layer
)
cell.add(source)

# Drain location at the right extension
drain = gdspy.Rectangle(
    (gate_x + gate_length, -source_drain_extension),
    (gate_x + gate_length + source_drain_length, fin_height + source_drain_extension),
    layer=source_drain_layer
)
cell.add(drain)

# Save to GDS file
lib.write_gds('FinFET.gds')

# View the layout using a layout viewer (optional)