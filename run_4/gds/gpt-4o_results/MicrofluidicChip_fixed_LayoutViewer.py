import gdspy

# Define constants
chip_width = 30e3  # in microns
chip_height = 20e3  # in microns
via_radius = 2e3  # in microns
via_distance = 20e3  # in microns
channel_width = 1e3  # in microns

# Create a new GDSII library and a cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('MICROFLUIDIC_CHIP')

# Create the bulk of the chip on layer 0
bulk_chip = gdspy.Rectangle((0, 0), (chip_width, chip_height), layer=0)
cell.add(bulk_chip)

# Define the center points of the vias on layer 2
via_center1 = (chip_width / 2 - via_distance / 2, chip_height / 2)
via_center2 = (chip_width / 2 + via_distance / 2, chip_height / 2)

# Create circular vias on layer 2
via1 = gdspy.Round(via_center1, radius=via_radius, layer=2)
via2 = gdspy.Round(via_center2, radius=via_radius, layer=2)
cell.add(via1)
cell.add(via2)

# Create a channel that connects the two circular vias on layer 3
# The channel is a rectangle centered vertically and horizontally between the two vias
channel_start = (via_center1[0] + via_radius, chip_height / 2 - channel_width / 2)
channel_end = (via_center2[0] - via_radius, chip_height / 2 + channel_width / 2)
channel = gdspy.Rectangle(channel_start, channel_end, layer=3)
cell.add(channel)

# Save the design to a GDS file
lib.write_gds('microfluidic_chip.gds')

# Plot the layout using the built-in viewer