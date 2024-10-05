import gdspy

# Create a new library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('MICROFLUIDIC_CHIP')

# Layer 0: Bulk of the chip (30 mm x 20 mm rectangle)
bulk = gdspy.Rectangle((0, 0), (30000, 20000), layer=0)
cell.add(bulk)

# Layer 2: Two circular vias
via_radius = 2000  # 2 mm radius
via_distance = 20000  # 20 mm apart horizontally
via_y_position = 10000  # Centered vertically

via1_center = (5000, via_y_position)
via2_center = (25000, via_y_position)

via1 = gdspy.Round(via1_center, via_radius, layer=2)
via2 = gdspy.Round(via2_center, via_radius, layer=2)
cell.add(via1)
cell.add(via2)

# Layer 3: Rectangular channel connecting vias
channel_width = 1000  # 1 mm width
channel_path = gdspy.Path(channel_width, via1_center)
channel_path.segment(via_distance, '+x', layer=3)
cell.add(channel_path)

# Save the design to a GDS file
lib.write_gds('microfluidic_chip.gds')

# Optional: View the layout