import gdspy

# Create a GDSII library
lib = gdspy.GdsLibrary()

# Create a cell to contain the design
cell = lib.new_cell('MICROFLUIDIC_CHIP')

# Dimensions of the bulk chip
chip_width = 30e3  # in microns (30 mm)
chip_height = 20e3  # in microns (20 mm)

# Create the bulk of the chip on layer 0
bulk_chip = gdspy.Rectangle((0, 0), (chip_width, chip_height), layer=0)
cell.add(bulk_chip)

# Positions for the two vias
via_radius = 2e3  # in microns (2 mm)
via_spacing = 20e3  # in microns (20 mm)
via_y_position = chip_height / 2
via_1_center = (chip_width / 2 - via_spacing / 2, via_y_position)
via_2_center = (chip_width / 2 + via_spacing / 2, via_y_position)

# Create the two vias on layer 2
via_1 = gdspy.Round(via_1_center, via_radius, layer=2)
via_2 = gdspy.Round(via_2_center, via_radius, layer=2)
cell.add(via_1)
cell.add(via_2)

# Create the rectangular shaped channel on layer 3
channel_width = 1e3  # in microns (1 mm)
channel_length = via_spacing  # in microns (20 mm)
channel_y_min = via_y_position - channel_width / 2
channel_y_max = via_y_position + channel_width / 2

# Define the coordinates of the channel rectangle
channel_rect = gdspy.Rectangle((via_1_center[0], channel_y_min),
                               (via_2_center[0], channel_y_max), layer=3)
cell.add(channel_rect)

# Save the design to a GDS file
lib.write_gds('microfluidic_chip.gds')

# Optionally, we can view the layout using the internal viewer (if available)