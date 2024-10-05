import gdspy

# Define the library and cell for the GDS layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell('microfluidic_chip')

# Create the bulk of the chip on layer 0
bulk = gdspy.Rectangle((0, 0), (30e-3, 20e-3), layer=0)
cell.add(bulk)

# Define the center coordinates of the two vias
via1_center = (10e-3, 10e-3)
via2_center = (30e-3 - 10e-3, 10e-3)

# Create the two circular vias on layer 2
via1 = gdspy.Round(via1_center, 2e-3, layer=2, number_of_points=100)
cell.add(via1)
via2 = gdspy.Round(via2_center, 2e-3, layer=2, number_of_points=100)
cell.add(via2)

# Create the rectangular shaped channel on layer 3
channel = gdspy.Rectangle((via1_center[0] - 0.5e-3, via1_center[1] - 0.5e-3), 
                          (via2_center[0] + 0.5e-3, via1_center[1] + 0.5e-3), layer=3)
cell.add(channel)

# Save the design to a GDS file
lib.write_gds('microfluidic_chip.gds')