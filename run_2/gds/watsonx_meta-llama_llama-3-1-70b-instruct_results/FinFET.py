import gdspy

# Create a new library and cell for the FinFET design
lib = gdspy.GdsLibrary()
cell = lib.new_cell('FinFET')

# Define the layers for the fin, gate, and source/drain regions
fin_layer = (1, 0)
gate_layer = (2, 0)
sdt_layer = (3, 0)

# Define the FinFET dimensions
fin_width = 0.1
fin_height = 0.2
fin_length = 1.0
gate_length = 0.1
sdt_length = 0.4
sdt_ext = 0.2

# Create the fin
fin = gdspy.Rectangle(
    (0, 0),
    (fin_length, fin_height),
    layer=fin_layer
)
cell.add(fin)

# Create the gate
gate = gdspy.Rectangle(
    (fin_length / 2 - gate_length / 2, -0.05),
    (fin_length / 2 + gate_length / 2, fin_height + 0.05),
    layer=gate_layer
)
cell.add(gate)

# Create the source and drain regions
sdt_src = gdspy.Rectangle(
    (-sdt_ext, 0),
    (sdt_length + sdt_ext, fin_height),
    layer=sdt_layer
)
cell.add(sdt_src)

sdt_drn = gdspy.Rectangle(
    (fin_length - sdt_length - sdt_ext, 0),
    (fin_length + sdt_ext, fin_height),
    layer=sdt_layer
)
cell.add(sdt_drn)

# Save the design to a GDS file
lib.write_gds('FinFET.gds')