import gdspy

# Define the library and cell for the GDS layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell('microfluidic_chip')

# Draw the bulk of the chip on layer 0
bulk = gdspy.Rectangle((0, 0), (30e3, 20e3), layer=0)
cell.add(bulk)

# Define the center coordinates of the two vias
via_center1 = (5e3, 10e3)
via_center2 = (25e3, 10e3)

# Draw the two circular vias on layer 2 (via level)
via1 = gdspy.Round((via_center1[0], via_center1[1]), 2e3, layer=2)
via2 = gdspy.Round((via_center2[0], via_center2[1]), 2e3, layer=2)
cell.add(via1)
cell.add(via2)

# Draw the rectangular shaped channel on layer 3 (channel level)
channel_width = 1e3
channel_points = [
    (via_center1[0], via_center1[1] - channel_width/2),
    (via_center1[0], via_center1[1] + channel_width/2),
    (via_center2[0], via_center2[1] + channel_width/2),
    (via_center2[0], via_center2[1] - channel_width/2)
]
channel = gdspy.Polygon(channel_points, layer=3)
cell.add(channel)

# Save the design to a GDS file
lib.write_gds('microfluidic_chip.gds')