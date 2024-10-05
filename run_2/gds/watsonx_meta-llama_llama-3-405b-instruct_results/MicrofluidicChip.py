import gdspy

# Define the library and cell for the GDS layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell('microfluidic_chip')

# Create the bulk of the chip on layer 0
bulk = gdspy.Rectangle((0, 0), (30e-3, 20e-3), layer=0)
cell.add(bulk)

# Create two circular vias on layer 2
via1 = gdspy.Round((10e-3, 10e-3), 2e-3, layer=2)
via2 = gdspy.Round((10e-3 + 20e-3, 10e-3), 2e-3, layer=2)
cell.add([via1, via2])

# Create a rectangular channel on layer 3
channel = gdspy.Rectangle((10e-3, 9e-3), (10e-3 + 20e-3, 11e-3), layer=3)
cell.add(channel)

# Save the design to a GDS file
lib.write_gds('microfluidic_chip.gds')