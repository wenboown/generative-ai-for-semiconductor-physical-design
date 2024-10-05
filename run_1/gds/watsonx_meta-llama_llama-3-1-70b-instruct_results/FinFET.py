import gdspy

# Define the fin width, height, and length
fin_width = 0.1
fin_height = 0.2
fin_length = 1.0

# Define the gate length
gate_length = 0.1

# Define the source/drain length and extension
sd_length = 0.4
sd_extension = 0.2

# Define the layers
fin_layer = (1, 0)  # Layer 1, datatype 0
gate_layer = (2, 0)  # Layer 2, datatype 0
sd_layer = (3, 0)  # Layer 3, datatype 0

# Create a new library and cell
lib = gdspy.Library()
cell = lib.new_cell('FinFET')

# Create the fin
fin = gdspy.Rectangle([-fin_length/2, 0], [fin_length/2, fin_height], layer=fin_layer)
cell.add(fin)

# Create the gate
gate = gdspy.Rectangle([-gate_length/2, fin_height], [gate_length/2, fin_height+0.1], layer=gate_layer)
cell.add(gate)

# Create the source and drain
sd1 = gdspy.Rectangle([-fin_length/2-sd_extension, 0], [-fin_length/2+sd_length, fin_height], layer=sd_layer)
sd2 = gdspy.Rectangle([fin_length/2-sd_length, 0], [fin_length/2+sd_extension, fin_height], layer=sd_layer)
cell.add(sd1)
cell.add(sd2)

# Create a layout with the cell
layout = gdspy.Layout('FinFET', unit=1.0e-6, precision=1.0e-9)
layout.add(cell)

# Save the layout to a GDS file
layout.write_gds('FinFET.gds')