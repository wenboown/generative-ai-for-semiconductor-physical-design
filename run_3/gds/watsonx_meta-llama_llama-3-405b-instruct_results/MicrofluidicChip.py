import gdspy

# Define the library and cell for the GDS layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell('microfluidic_chip')

# Create the bulk of the chip on layer 0
bulk = gdspy.Rectangle((0, 0), (30e3, 20e3), layer=0)
cell.add(bulk)

# Create the two circular vias on layer 2
via1 = gdspy.Round((10e3, 10e3), 2e3, layer=2)
via2 = gdspy.Round((30e3, 10e3), 2e3, layer=2)
cell.add(via1)
cell.add(via2)

# Create the rectangular shaped channel on layer 3
channel = gdspy.Rectangle((9e3, 9e3), (11e3, 11e3), layer=3)
channel.translate(0, 0)
channel.scale((1, 1), (1e3, 9e3))
channel.translate(10e3, 0)
cell.add(channel)
channel2 = gdspy.Rectangle((29e3, 9e3), (31e3, 11e3), layer=3)
channel2.translate(-10e3, 0)
cell.add(channel2)
channel3 = gdspy.Rectangle((11e3, 9e3), (29e3, 11e3), layer=3)
cell.add(channel3)

# Save the design to a GDS file
lib.write_gds('microfluidic_chip.gds')