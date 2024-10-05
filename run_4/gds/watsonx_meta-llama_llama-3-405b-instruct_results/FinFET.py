import gdspy

# Define the design specifications
fin_width = 0.1
fin_height = 0.2
fin_length = 1.0
gate_length = 0.1
source_drain_length = 0.4
source_drain_extension = 0.2

# Create the GDS library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('FinFET')

# Define the layers for each region
fin_layer = 1
gate_layer = 2
source_drain_layer = 3

# Create the fin
fin = gdspy.Rectangle((0, 0), (fin_width, fin_height))
fin.translate(-fin_width/2, -fin_height/2)
cell.add(fin, layer=fin_layer)

# Create the gate
gate = gdspy.Rectangle((0, 0), (gate_length, fin_width))
gate.translate(-gate_length/2, 0)
cell.add(gate, layer=gate_layer)

# Create the source and drain regions
source = gdspy.Rectangle((-source_drain_length/2 - source_drain_extension, -fin_height/2),
                         (0, fin_height/2))
source_drain = gdspy.Rectangle((0, -fin_height/2), (source_drain_length/2 + source_drain_extension, fin_height/2))
cell.add(source, layer=source_drain_layer)
cell.add(source_drain, layer=source_drain_layer)

# Create the fin extension
fin_ext = gdspy.Rectangle((-fin_length/2, -fin_height/2), (-source_drain_length/2, fin_height/2))
fin_ext2 = gdspy.Rectangle((source_drain_length/2, -fin_height/2), (fin_length/2, fin_height/2))
cell.add(fin_ext, layer=fin_layer)
cell.add(fin_ext2, layer=fin_layer)

# Save the design to a GDS file
lib.write_gds('FinFET.gds')