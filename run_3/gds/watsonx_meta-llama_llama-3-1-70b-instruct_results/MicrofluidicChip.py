import gdspy

# Define the design specifications
bulk_size = (30, 20)  # mm
via_radius = 2  # mm
via_separation = 20  # mm
channel_width = 1  # mm

# Define the layers
layer_bulk = 0
layer_via = 2
layer_channel = 3

# Create a new GDS library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('microfluidic_chip')

# Draw the bulk of the chip (layer 0)
bulk = gdspy.Rectangle((0, 0), (bulk_size[0], bulk_size[1]), layer=layer_bulk)
cell.add(bulk)

# Draw the circular vias (layer 2)
via1 = gdspy.Round((via_separation / 2, 0), via_radius, number_of_points=100, layer=layer_via)
via2 = gdspy.Round((bulk_size[0] - via_separation / 2, 0), via_radius, number_of_points=100, layer=layer_via)
cell.add(via1)
cell.add(via2)

# Draw the rectangular shaped channel (layer 3)
channel = gdspy.Rectangle((via_radius, -channel_width/2), (bulk_size[0] - via_radius, channel_width/2), layer=layer_channel)
cell.add(channel)

# Save the design to a GDS file
lib.write_gds('microfluidic_chip.gds')