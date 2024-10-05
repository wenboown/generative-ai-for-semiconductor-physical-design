import gdspy

# Define the library and cell for the GDS layout
lib = gdspy.Library()
cell = lib.new_cell('FinFET')

# Define the fin layer and create the fin rectangle
fin_layer = 1
fin_rect = gdspy.Rectangle((0, 0), (1.0, 0.2), fin_layer)
cell.add(fin_rect)

# Define the gate layer and create the gate rectangle
gate_layer = 2
gate_rect = gdspy.Rectangle((0.45, -0.1), (0.55, 0.1), gate_layer)
cell.add(gate_rect)

# Define the source/drain layer and create the source/drain rectangles
sdr_layer = 3
src_rect = gdspy.Rectangle((-0.4, 0), (-0.2, 0.2), sdr_layer)
drn_rect = gdspy.Rectangle((0.8, 0), (1.0, 0.2), sdr_layer)
cell.add(src_rect)
cell.add(drn_rect)

# Save the design to a GDS file
lib.write_gds('finfet.gds')