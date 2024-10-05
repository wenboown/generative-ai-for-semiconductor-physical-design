import gdspy

# Design specifications
fin_width = 0.1
fin_height = 0.2
fin_length = 1.0
gate_length = 0.1
source_drain_length = 0.4
source_drain_extension = 0.2

# Create a GDS Library and a Cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('FINFET')

# Define layers for different regions
fin_layer = 1
gate_layer = 2
source_drain_layer = 3

# Fin
fin_coords = [
    (0, 0),
    (fin_length, 0),
    (fin_length, fin_width),
    (0, fin_width)
]
fin = gdspy.Polygon(fin_coords, layer=fin_layer)
cell.add(fin)

# Source/Drain extensions
source_coords = [
    (-source_drain_extension, -fin_height),
    (0, -fin_height),
    (0, fin_width + fin_height),
    (-source_drain_extension, fin_width + fin_height)
]
source = gdspy.Polygon(source_coords, layer=source_drain_layer)
cell.add(source)

drain_coords = [
    (fin_length, -fin_height),
    (fin_length + source_drain_extension, -fin_height),
    (fin_length + source_drain_extension, fin_width + fin_height),
    (fin_length, fin_width + fin_height)
]
drain = gdspy.Polygon(drain_coords, layer=source_drain_layer)
cell.add(drain)

# Gate
gate_x_start = (fin_length - gate_length) / 2
gate_coords = [
    (gate_x_start, -fin_height),
    (gate_x_start + gate_length, -fin_height),
    (gate_x_start + gate_length, fin_width + fin_height),
    (gate_x_start, fin_width + fin_height)
]
gate = gdspy.Polygon(gate_coords, layer=gate_layer)
cell.add(gate)

# Source/Drain regions
source_drain_y_range = fin_width + 2 * fin_height
source_drain_left_coords = [
    (0, 0),
    (source_drain_length, 0),
    (source_drain_length, source_drain_y_range),
    (0, source_drain_y_range)
]
source_drain_left = gdspy.Polygon(source_drain_left_coords, layer=source_drain_layer)
cell.add(source_drain_left)

source_drain_right_coords = [
    (fin_length - source_drain_length, 0),
    (fin_length, 0),
    (fin_length, source_drain_y_range),
    (fin_length - source_drain_length, source_drain_y_range)
]
source_drain_right = gdspy.Polygon(source_drain_right_coords, layer=source_drain_layer)
cell.add(source_drain_right)

# Write the GDS file
gds_file = "finfet_layout.gds"
lib.write_gds(gds_file)

# Optionally, display all created layout