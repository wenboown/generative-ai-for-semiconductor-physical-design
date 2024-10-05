import gdspy

# Define the library and cell for the GDS layout
lib = gdspy.Library()
cell = lib.new_cell('microfluidic_chip')

# Draw the bulk of the chip on layer 0
bulk = gdspy.Rectangle((0, 0), (30, 20), layer=0)
cell.add(bulk)

# Draw two circular vias on layer 2 (via level)
via1 = gdspy.Round((5, 10), 2, layer=2)
via2 = gdspy.Round((25, 10), 2, layer=2)
cell.add(via1)
cell.add(via2)

# Draw a rectangular shaped channel on layer 3 (channel level)
channel = gdspy.Rectangle((3, 9), (27, 11), layer=3)
cell.add(channel)

# Save the design to a GDS file
lib.write_gds('microfluidic_chip.gds')