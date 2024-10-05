import gdspy

# Create a new GDSII library
lib = gdspy.GdsLibrary()

# Create a cell in the library
cell = lib.new_cell('MICROFLUIDIC_CHIP')

# Layer definitions
bulk_layer = 0       # Layer for the bulk of the chip
via_layer = 2        # Layer for the vias
channel_layer = 3    # Layer for the channel

# Chip dimensions
chip_width = 30.0     # Width of the chip in mm
chip_height = 20.0    # Height of the chip in mm

# Via properties
via_radius = 2.0       # Radius of the vias in mm
via_distance = 20.0    # Horizontal distance between the centers of the vias in mm

# Channel properties
channel_width = 1.0    # Width of the channel in mm

# Create the bulk of the chip on layer 0
chip_bulk = gdspy.Rectangle(
    (0, 0),
    (chip_width, chip_height),
    layer=bulk_layer
)
cell.add(chip_bulk)

# Calculate centers of the two vias such that they are 20 mm apart horizontally and centered vertically
via1_center_x = (chip_width - via_distance) / 2
via2_center_x = (chip_width + via_distance) / 2
via_center_y = chip_height / 2

# Create the first via on layer 2
via1 = gdspy.Round(
    (via1_center_x, via_center_y),
    via_radius,
    layer=via_layer
)
cell.add(via1)

# Create the second via on layer 2
via2 = gdspy.Round(
    (via2_center_x, via_center_y),
    via_radius,
    layer=via_layer
)
cell.add(via2)

# Create the channel connecting the two vias at their centers on layer 3
channel = gdspy.Rectangle(
    (via1_center_x, via_center_y - channel_width / 2),
    (via2_center_x, via_center_y + channel_width / 2),
    layer=channel_layer
)
cell.add(channel)

# Write the GDSII file
lib.write_gds('microfluidic_chip.gds')