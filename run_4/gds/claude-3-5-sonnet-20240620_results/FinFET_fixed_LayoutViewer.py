import gdspy

# Create a new library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('FinFET')

# Define layers
fin_layer = 1
gate_layer = 2
sd_layer = 3

# Define dimensions (in µm)
fin_width = 0.1
fin_length = 1.0
gate_length = 0.1
sd_length = 0.4
sd_extension = 0.2

# Calculate positions
gate_position = (fin_length - gate_length) / 2
sd_width = fin_width + 2 * sd_extension

# Create fin
fin = gdspy.Rectangle((0, 0), (fin_width, fin_length), layer=fin_layer)
cell.add(fin)

# Create gate
gate = gdspy.Rectangle((-sd_extension, gate_position), 
                       (fin_width + sd_extension, gate_position + gate_length), 
                       layer=gate_layer)
cell.add(gate)

# Create source
source = gdspy.Rectangle((-sd_extension, 0), 
                         (sd_width, sd_length), 
                         layer=sd_layer)
cell.add(source)

# Create drain
drain = gdspy.Rectangle((-sd_extension, fin_length - sd_length), 
                        (sd_width, fin_length), 
                        layer=sd_layer)
cell.add(drain)

# Save the design to a GDS file
lib.write_gds('finfet_layout.gds')

# Optional: View the layout