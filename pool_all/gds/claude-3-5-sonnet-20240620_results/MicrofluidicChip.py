import gdspy

# Create a new library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('MICROFLUIDIC_CHIP')

# Define dimensions in micrometers
chip_width = 30e3  # 30 mm
chip_height = 20e3  # 20 mm
via_radius = 2e3   # 2 mm
via_spacing = 20e3 # 20 mm
channel_width = 1e3 # 1 mm

# Layer 0: Bulk of the chip
bulk = gdspy.Rectangle((0, 0), (chip_width, chip_height), layer=0)
cell.add(bulk)

# Layer 2: Two circular vias
via1_center = (chip_width/2 - via_spacing/2, chip_height/2)
via2_center = (chip_width/2 + via_spacing/2, chip_height/2)

via1 = gdspy.Round(via1_center, via_radius, layer=2)
via2 = gdspy.Round(via2_center, via_radius, layer=2)
cell.add(via1)
cell.add(via2)

# Layer 3: Rectangular channel connecting vias
channel_start = (via1_center[0] + via_radius, chip_height/2 - channel_width/2)
channel_end = (via2_center[0] - via_radius, chip_height/2 + channel_width/2)
channel = gdspy.Rectangle(channel_start, channel_end, layer=3)
cell.add(channel)

# Save the design to a GDS file
lib.write_gds('microfluidic_chip.gds')