import gdspy

# Create a new library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('MICROFLUIDIC_CHIP')

# Layer 0: Bulk of the chip
bulk = gdspy.Rectangle((0, 0), (30e6, 20e6), layer=0)
cell.add(bulk)

# Layer 2: Two circular vias
via1 = gdspy.Round((5e6, 10e6), 2e6, layer=2)
via2 = gdspy.Round((25e6, 10e6), 2e6, layer=2)
cell.add(via1)
cell.add(via2)

# Layer 3: Rectangular channel connecting vias
channel = gdspy.Path(1e6, (5e6, 10e6))
channel.segment(20e6, '+x', layer=3)
cell.add(channel)

# Save the design to a GDS file
lib.write_gds('microfluidic_chip.gds')

# Optional: View the layout