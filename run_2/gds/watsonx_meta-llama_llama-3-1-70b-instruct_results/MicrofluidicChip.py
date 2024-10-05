import gdspy

# Define the library and cell for the GDS layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell("microfluidic_chip")

# Layer 0: Bulk of the chip (30 * 20 mm rectangle)
bulk_layer = 0
bulk_rect = gdspy.Rectangle((0, 0), (30e3, 20e3), layer=bulk_layer)
cell.add(bulk_rect)

# Layer 2: Via level (two circular vias with 2 mm radius, 20 mm apart horizontally)
via_layer = 2
via_radius = 2e3  # 2 mm
via_center1 = (5e3, 10e3)  # 5 mm from the left edge, 10 mm from the bottom edge
via_center2 = (25e3, 10e3)  # 25 mm from the left edge, 10 mm from the bottom edge
via1 = gdspy.Round(via_center1, via_radius, layer=via_layer, number_of_points=32)
via2 = gdspy.Round(via_center2, via_radius, layer=via_layer, number_of_points=32)
cell.add(via1)
cell.add(via2)

# Layer 3: Channel level (rectangular shaped channel connecting the two vias at their center)
channel_layer = 3
channel_width = 1e3  # 1 mm
channel_rect = gdspy.Rectangle((via_center1[0] - channel_width/2, via_center1[1] - channel_width/2), 
                               (via_center2[0] + channel_width/2, via_center2[1] + channel_width/2), 
                               layer=channel_layer)
cell.add(channel_rect)

# Save the design to a GDS file
lib.write_gds("microfluidic_chip.gds")