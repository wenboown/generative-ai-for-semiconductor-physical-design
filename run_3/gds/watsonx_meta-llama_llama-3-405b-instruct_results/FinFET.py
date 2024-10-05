import gdspy

# Define the library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('FinFET')

# Define the layers
fin_layer = 1
gate_layer = 2
sd_layer = 3

# Define the dimensions
fin_width = 0.1
fin_height = 0.2
fin_length = 1.0
gate_length = 0.1
sd_length = 0.4
sd_extension = 0.2

# Draw the fin
fin = gdspy.Rectangle((0, 0), (fin_width, fin_length), layer=fin_layer)
cell.add(fin)

# Draw the source/drain regions
sd1 = gdspy.Rectangle((-sd_extension, 0), (sd_length, fin_width), layer=sd_layer)
sd1.translate(-sd_length/2 + fin_length/2, 0)
cell.add(sd1)

sd2 = gdspy.Rectangle((-sd_extension, 0), (sd_length, fin_width), layer=sd_layer)
sd2.translate(sd2.size[1][0]/2 + fin_length/2, 0)
cell.add(sd2)

# Draw the gate
gate = gdspy.Rectangle((fin_length/2 - gate_length/2, fin_height/2 - gate_length/2), 
                       (fin_length/2 + gate_length/2, fin_height/2 + gate_length/2), layer=gate_layer)
cell.add(gate)

# Save the design to a GDS file
lib.write_gds('FinFET.gds')