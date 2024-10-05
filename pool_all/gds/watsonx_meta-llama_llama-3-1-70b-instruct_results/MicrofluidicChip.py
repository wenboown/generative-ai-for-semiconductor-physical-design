import gdspy

# Define the library and cell for the GDS layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell('MICROFLUIDIC_CHIP')

# Define the dimensions of the bulk of the chip
chip_width = 30e3  # 30 mm in micrometers
chip_height = 20e3  # 20 mm in micrometers

# Create the bulk of the chip on layer 0
bulk_rectangle = gdspy.Rectangle((0, 0), (chip_width, chip_height), layer=0)
cell.add(bulk_rectangle)

# Define the positions and radius for the circular vias on layer 2
via_radius = 2e3  # 2 mm in micrometers
via_spacing = 20e3  # 20 mm in micrometers

# Center coordinates of the vias
via_center1 = (chip_width / 2 - via_spacing / 2, chip_height / 2)
via_center2 = (chip_width / 2 + via_spacing / 2, chip_height / 2)

# Create the circular vias on layer 2
via1 = gdspy.Round(via_center1, via_radius, layer=2)
via2 = gdspy.Round(via_center2, via_radius, layer=2)
cell.add(via1)
cell.add(via2)

# Define the channel that connects the vias on layer 3
channel_width = 1e3  # 1 mm in micrometers

# Channel coordinates
channel_x1 = via_center1[0] + via_radius
channel_x2 = via_center2[0] - via_radius
channel_y1 = via_center1[1] - channel_width / 2
channel_y2 = via_center1[1] + channel_width / 2

# Create the channel on layer 3
channel_rectangle = gdspy.Rectangle((channel_x1, channel_y1), (channel_x2, channel_y2), layer=3)
cell.add(channel_rectangle)

# Save the design to a GDS file
lib.write_gds('microfluidic_chip.gds')