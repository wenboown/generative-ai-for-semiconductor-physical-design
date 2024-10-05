import gdspy

# Define the library and cell
lib = gdspy.GdsLibrary(unit=1e-6, precision=1e-9)
cell = lib.new_cell('FinFET')

# Define the layers
fin_layer = {'layer': 1, 'datatype': 0}
gate_layer = {'layer': 2, 'datatype': 0}
sd_layer = {'layer': 3, 'datatype': 0}

# Draw the fin
fin = gdspy.Rectangle((-0.05, -0.1), (0.05, 0.1), **fin_layer)
cell.add(fin)
# Draw the fin extension (length)
fin_ext = gdspy.Rectangle((-0.05, -0.1), (0.05, -0.1 + 1.0), **fin_layer)
cell.add(fin_ext)

# Draw the gate
gate = gdspy.Rectangle((-0.05, -0.05), (0.05, 0.05), **gate_layer)
gate.translate(0, 0.5)
cell.add(gate)

# Draw the source/drain regions
source = gdspy.Rectangle((-0.2, -0.2), (0, 0.2), **sd_layer)
drain = gdspy.Rectangle((0, -0.2), (0.2, 0.2), **sd_layer)
source.translate(-0.5, 0)
drain.translate(0.5, 0)
cell.add([source, drain])

# Save the design to a GDS file
lib.write_gds('finfet.gds')