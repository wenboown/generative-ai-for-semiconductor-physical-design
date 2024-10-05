import gdspy

# Define the library and the cell for the GDS layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell('FinFET')

# Parameters
fin_width = 0.1
fin_height = 0.2
fin_length = 1.0
gate_length = 0.1
source_drain_length = 0.4
source_drain_extension = 0.2

# Layers
fin_layer = 0
gate_layer = 1
source_drain_layer = 2

# Coordinates calculation
fin_x = 0
fin_y = 0

# Fin region
fin = gdspy.Rectangle((fin_x, fin_y), 
                      (fin_x + fin_length, fin_y + fin_height), 
                      layer=fin_layer)
cell.add(fin)

# Gate region
gate_y = fin_y + fin_height * 0.5 - gate_length * 0.5
gate = gdspy.Rectangle((fin_x + fin_length * 0.5 - gate_length * 0.5, gate_y),
                       (fin_x + fin_length * 0.5 + gate_length * 0.5, gate_y + gate_length), 
                       layer=gate_layer)
cell.add(gate)

# Source/Drain region
source_x = fin_x - source_drain_extension
drain_x = fin_x + fin_length

source = gdspy.Rectangle((source_x, fin_y), 
                         (source_x + source_drain_length, fin_y + fin_height), 
                         layer=source_drain_layer)

drain = gdspy.Rectangle((drain_x, fin_y), 
                        (drain_x + source_drain_length, fin_y + fin_height), 
                        layer=source_drain_layer)

cell.add(source)
cell.add(drain)

# Saving GDS to a file
lib.write_gds('finfet.gds')

print("FinFET layout has been saved to 'finfet.gds'")