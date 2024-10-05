import gdspy

# Create a library and add a new cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('FinFET')

# Specifications
fin_width = 0.1
fin_height = 0.2
fin_length = 1.0
gate_length = 0.1
source_drain_length = 0.4
source_drain_extension = 0.2

# Fin coordinates (on layer 1)
fin_polygon = gdspy.Rectangle((0, 0), (fin_length, fin_height), layer=1)
cell.add(fin_polygon)

# Gate coordinates (on layer 2)
gate_x = (fin_length - gate_length) / 2
gate_polygon = gdspy.Rectangle((gate_x, -fin_width), (gate_x + gate_length, fin_height + fin_width), layer=2)
cell.add(gate_polygon)

# Source/Drain coordinates (on layers 3, 4)
source_polygon = gdspy.Rectangle((-source_drain_extension, -fin_width), (0, fin_height + fin_width), layer=3)
drain_polygon = gdspy.Rectangle((fin_length, -fin_width), (fin_length + source_drain_extension, fin_height + fin_width), layer=4)
cell.add(source_polygon)
cell.add(drain_polygon)

# Save the layout to a GDS file
lib.write_gds('finfet_layout.gds')

# Optionally, view using an internal viewer (if supported)
try:
    lib.view()
except:
    print("Viewer not supported in the current environment.")