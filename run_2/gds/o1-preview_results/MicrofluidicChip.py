import gdspy

# Create a new GDSII library
lib = gdspy.GdsLibrary()

# Create a cell for our design
cell = lib.new_cell('MICROFLUIDIC_CHIP')

# Coordinates in micrometers (1 mm = 1000 μm)

# Layer 0: Bulk of the chip - 30 mm x 20 mm rectangle
bulk_rectangle = gdspy.Rectangle((0, 0), (30000, 20000), layer=0)
cell.add(bulk_rectangle)

# Layer 2: Two circular vias with 2 mm radius, 20 mm apart horizontally
via_radius = 2000  # 2 mm in μm
# Centers of the vias
via1_center = (5000, 10000)   # 5 mm from the left, centered vertically
via2_center = (25000, 10000)  # 25 mm from the left, centered vertically

# Create vias
via1 = gdspy.Round(via1_center, via_radius, layer=2)
via2 = gdspy.Round(via2_center, via_radius, layer=2)
cell.add([via1, via2])

# Layer 3: Rectangular channel connecting the two vias at their centers
channel_width = 1000  # 1 mm in μm
channel_path = gdspy.Path(channel_width, (via1_center[0], via1_center[1]))
channel_path.segment(via2_center[0] - via1_center[0], '+x', layer=3)
cell.add(channel_path)

# Write the GDSII file
lib.write_gds('microfluidic_chip.gds')