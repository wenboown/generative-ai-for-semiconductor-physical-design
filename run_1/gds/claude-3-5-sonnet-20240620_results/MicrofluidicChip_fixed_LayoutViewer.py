import gdspy

# Create a new library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('MICROFLUIDIC_CHIP')

# Layer 0: Bulk of the chip (30x20 mm rectangle)
bulk = gdspy.Rectangle((0, 0), (30e3, 20e3), layer=0)
cell.add(bulk)

# Layer 2: Two circular vias (2 mm radius, 20 mm apart horizontally)
via1_center = (5e3, 10e3)  # 5 mm from left, centered vertically
via2_center = (25e3, 10e3)  # 25 mm from left, centered vertically
via1 = gdspy.Round(via1_center, 2e3, layer=2)
via2 = gdspy.Round(via2_center, 2e3, layer=2)
cell.add(via1)
cell.add(via2)

# Layer 3: Rectangular channel connecting the vias
channel_width = 1e3  # 1 mm width
channel = gdspy.Rectangle(
    (via1_center[0], via1_center[1] - channel_width/2),
    (via2_center[0], via2_center[1] + channel_width/2),
    layer=3
)
cell.add(channel)

# Save the design to a GDS file
lib.write_gds('microfluidic_chip.gds')

# Optional: View the layout