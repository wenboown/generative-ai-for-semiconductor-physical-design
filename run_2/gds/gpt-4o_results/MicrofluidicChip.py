import gdspy

# Define the library and cell for the GDS layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell('MICROFLUIDIC_CHIP')

# Define design parameters
bulk_chip_width = 30e3  # 30 mm in micrometers
bulk_chip_height = 20e3  # 20 mm in micrometers
via_radius = 2e3  # 2 mm in micrometers
via_spacing = 20e3  # 20 mm in micrometers
channel_width = 1e3  # 1 mm in micrometers

# Draw the bulk of the chip on layer 0
bulk_rectangle = gdspy.Rectangle((0, 0), (bulk_chip_width, bulk_chip_height), layer=0)
cell.add(bulk_rectangle)

# Calculate coordinates for the centers of the vias
via_center1 = (bulk_chip_width / 2 - via_spacing / 2, bulk_chip_height / 2)
via_center2 = (bulk_chip_width / 2 + via_spacing / 2, bulk_chip_height / 2)

# Draw circular vias on layer 2
via1 = gdspy.Round(via_center1, via_radius, layer=2)
via2 = gdspy.Round(via_center2, via_radius, layer=2)
cell.add(via1)
cell.add(via2)

# Draw the channel connecting the vias at their center on layer 3
# The channel is a rectangle
channel_start_x = via_center1[0] + via_radius
channel_end_x = via_center2[0] - via_radius
channel_y = via_center1[1]  # same y-coordinate as the via centers

channel_rectangle = gdspy.Rectangle((channel_start_x, channel_y - channel_width / 2), 
                                    (channel_end_x, channel_y + channel_width / 2), 
                                    layer=3)
cell.add(channel_rectangle)

# Save the design to a GDS file
lib.write_gds('microfluidic_chip.gds')