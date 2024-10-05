import gdspy

# Define GDSII library
lib = gdspy.GdsLibrary()

# Create a cell for the design
cell = lib.new_cell('LAYOUT')

# Define layers
via_layer = 1
metal_layer = 2
pad_layer = 3

# Geometric properties
via_radius = 10
pad_radius = 30
metal_width = 40
metal_length = 600
margin = 10  # Margin between edge of metal and edge of pad
via_spacing = (metal_length - metal_width - 2 * margin) / 2 - via_radius

# Coordinates for vias and pads
via1_center = (50, 150)
via2_center = (550, 150)

# Create via 1
via1 = gdspy.Round(via1_center, via_radius, number_of_points=64, layer=via_layer)
cell.add(via1)

# Create via 2
via2 = gdspy.Round(via2_center, via_radius, number_of_points=64, layer=via_layer)
cell.add(via2)

# Create pad 1
pad1 = gdspy.Round(via1_center, pad_radius, number_of_points=64, layer=pad_layer)
cell.add(pad1)

# Create pad 2
pad2 = gdspy.Round(via2_center, pad_radius, number_of_points=64, layer=pad_layer)
cell.add(pad2)

# Create metal connection
metal_conn_x1 = via1_center[0] - margin - metal_width / 2
metal_conn_x2 = via2_center[0] + margin + metal_width / 2
metal_conn_y1 = via1_center[1] - metal_width / 2
metal_conn_y2 = via1_center[1] + metal_width / 2

metal_connection = gdspy.Rectangle((metal_conn_x1, metal_conn_y1), (metal_conn_x2, metal_conn_y2), layer=metal_layer)
cell.add(metal_connection)

# Write the GDS file
lib.write_gds('layout_design.gds')