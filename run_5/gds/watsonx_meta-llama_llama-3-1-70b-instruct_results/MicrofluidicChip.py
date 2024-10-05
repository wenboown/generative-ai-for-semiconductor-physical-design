import gdspy

# Define the library and cell for the GDS layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell('microfluidic_chip')

# Layer definitions
layer0 = {'layer': 0, 'datatype': 0}
layer2 = {'layer': 2, 'datatype': 0}
layer3 = {'layer': 3, 'datatype': 0}

# Draw the bulk of the chip on layer 0
rect = gdspy.Rectangle((0, 0), (30e3, 20e3), **layer0)
cell.add(rect)

# Draw the vias on layer 2
via1 = gdspy.Round((5e3, 10e3), 2e3, **layer2)
via2 = gdspy.Round((25e3, 10e3), 2e3, **layer2)
cell.add(via1)
cell.add(via2)

# Draw the channel on layer 3
channel = gdspy.Rectangle((5e3 - 0.5e3, 9.5e3), (25e3 + 0.5e3, 10.5e3), **layer3)
cell.add(channel)

# Save the design to a GDS file
lib.write_gds('microfluidic_chip.gds')