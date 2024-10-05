import gdspy

# Define the layers for the fin, gate, and source/drain regions
fin_layer = 1
gate_layer = 2
sd_layer = 3

# Define the design specifications
fin_width = 0.1  # in microns
fin_height = 0.2  # in microns
fin_length = 1.0  # in microns
gate_length = 0.1  # in microns
sd_length = 0.4  # in microns
sd_extension = 0.2  # in microns

# Create a new GDS library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('FinFET')

# Draw the fin
fin_rect = gdspy.Rectangle((0, 0), (fin_length, fin_width), layer=fin_layer)
cell.add(fin_rect)

# Draw the gate
gate_rect = gdspy.Rectangle((0, fin_width/2 - gate_length/2), (fin_length, fin_width/2 + gate_length/2), layer=gate_layer)
cell.add(gate_rect)

# Draw the source and drain regions
sd_rect_left = gdspy.Rectangle((-sd_extension, 0), (-sd_extension + sd_length, fin_width), layer=sd_layer)
sd_rect_right = gdspy.Rectangle((fin_length + sd_extension - sd_length, 0), (fin_length + sd_extension, fin_width), layer=sd_layer)
cell.add(sd_rect_left)
cell.add(sd_rect_right)

# Save the design to a GDS file
lib.write_gds('FinFET.gds')