import gdspy

# Creating a library
lib = gdspy.GdsLibrary()

# Creating a cell (a module within the GDSII file to hold specific layout patterns)
cell = lib.new_cell('FinFET')

# Specifications
fin_width = 0.1
fin_height = 0.2
fin_length = 1.0
gate_length = 0.1
source_drain_length = 0.4
source_drain_extension = 0.2

# Layers
fin_layer = 1
gate_layer = 2
source_drain_layer = 3

# Fin (created as a rectangle)
fin = gdspy.Rectangle(
    (-fin_length/2, -fin_width/2), 
    (fin_length/2, fin_width/2), 
    layer=fin_layer)

# Gate (created as a rectangle and positioned around the fin)
gate = gdspy.Rectangle(
    (-gate_length/2, -fin_height/2), 
    (gate_length/2, fin_height/2), 
    layer=gate_layer)

# Source and Drain (created as rectangles and positioned beyond the gate length and fin)
source = gdspy.Rectangle(
    (-fin_length/2 - source_drain_length, -fin_height/2), 
    (-fin_length/2, fin_height/2), 
    layer=source_drain_layer)

drain = gdspy.Rectangle(
    (fin_length/2, -fin_height/2), 
    (fin_length/2 + source_drain_length, fin_height/2), 
    layer=source_drain_layer)

# Source/Drain Extensions beyond the fin
source_extension = gdspy.Rectangle(
    (-fin_length/2 - source_drain_length, fin_height/2), 
    (-fin_length/2, fin_height/2 + source_drain_extension), 
    layer=source_drain_layer)

drain_extension = gdspy.Rectangle(
    (fin_length/2, fin_height/2), 
    (fin_length/2 + source_drain_length, fin_height/2 + source_drain_extension), 
    layer=source_drain_layer)

# Adding all elements to the cell
cell.add(fin)
cell.add(gate)
cell.add(source)
cell.add(drain)
cell.add(source_extension)
cell.add(drain_extension)

# Exporting the GDS file
lib.write_gds('finfet.gds')