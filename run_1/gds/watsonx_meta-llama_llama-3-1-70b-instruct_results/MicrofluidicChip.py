import gdspy

# Create a new library and cell for the GDS layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell("Microfluidic Chip")

# Draw the chip bulk on layer 0
chip_bulk = gdspy.Rectangle((0, 0), (30, 20), layer=0)
cell.add(chip_bulk)

# Draw the vias on layer 2
via_radius = 2
via_center1 = (10, 10)
via_center2 = (10 + 20, 10)
via1 = gdspy.Round(via_center1, via_radius, layer=2, tolerance=0.01)
via2 = gdspy.Round(via_center2, via_radius, layer=2, tolerance=0.01)
cell.add(via1)
cell.add(via2)

# Draw the channel on layer 3
channel_width = 1
channel_length = 20
channel_points = [(via_center1[0] + via_radius, via_center1[1]), 
                  (via_center2[0] - via_radius, via_center2[1])]
channel = gdspy.Path(channel_width, layer=3).points(channel_points)
cell.add(channel)

# Save the design to a GDS file
lib.write_gds("microfluidic_chip.gds")