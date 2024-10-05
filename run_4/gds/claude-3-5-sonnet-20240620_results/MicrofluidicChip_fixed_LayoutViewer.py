import gdspy

# Create a new library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('MICROFLUIDIC_CHIP')

# Layer 0: Bulk of the chip (30 x 20 mm rectangle)
bulk = gdspy.Rectangle((0, 0), (30e3, 20e3), layer=0)
cell.add(bulk)

# Layer 2: Two circular vias (2 mm radius, 20 mm apart horizontally)
via1_center = (5e3, 10e3)  # 5 mm from left edge, centered vertically
via2_center = (25e3, 10e3)  # 25 mm from left edge, centered vertically
via1 = gdspy.Round(via1_center, 2e3, layer=2)
via2 = gdspy.Round(via2_center, 2e3, layer=2)
cell.add(via1)
cell.add(via2)

# Layer 3: Rectangular channel connecting the vias (1 mm width)
channel_path = gdspy.Path(1e3, via1_center, layer=3)
channel_path.segment(20e3, '+x')  # 20 mm horizontal segment
cell.add(channel_path)

# Save the design to a GDS file
lib.write_gds('microfluidic_chip.gds')

# Optional: View the layout