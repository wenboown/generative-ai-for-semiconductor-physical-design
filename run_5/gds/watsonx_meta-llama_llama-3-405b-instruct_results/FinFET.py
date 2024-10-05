import gdspy

# Define the library and cell for the GDS layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell('FinFET')

# Define the layers for the fin, gate, and source/drain regions
fin_layer = 1
gate_layer = 2
sd_layer = 3

# Define the coordinates for the fin
fin_x = 0
fin_y = 0
fin_width = 0.1
fin_height = 0.2
fin_length = 1.0

# Create the fin rectangle
fin = gdspy.Rectangle((fin_x, fin_y), (fin_x + fin_width, fin_y + fin_height), layer=fin_layer)
cell.add(fin)

# Create the fin extension (length)
fin_ext = gdspy.Rectangle((fin_x, fin_y), (fin_x + fin_width, fin_y + fin_length), layer=fin_layer)
cell.add(fin_ext)

# Define the coordinates for the gate
gate_x = fin_x + fin_width/2 - 0.05  # centered over the fin
gate_y = fin_y + fin_height
gate_length = 0.1
gate_width = fin_width + 0.1  # wider than the fin to ensure overlap

# Create the gate rectangle
gate = gdspy.Rectangle((gate_x, gate_y), (gate_x + gate_length, gate_y + gate_width), layer=gate_layer)
cell.add(gate)

# Define the coordinates for the source/drain regions
sd_x1 = fin_x - 0.2  # source/drain extension beyond the fin
sd_y1 = fin_y
sd_x2 = fin_x + fin_width + 0.2  # source/drain extension beyond the fin
sd_y2 = fin_y + fin_length
sd_length = 0.4

# Create the source/drain rectangles
source = gdspy.Rectangle((sd_x1, sd_y1), (sd_x1 + sd_length, sd_y1 + fin_height), layer=sd_layer)
cell.add(source)
drain = gdspy.Rectangle((sd_x2 - sd_length, sd_y2 - fin_height), (sd_x2, sd_y2), layer=sd_layer)
cell.add(drain)

# Save the design to a GDS file
lib.write_gds('FinFET.gds')