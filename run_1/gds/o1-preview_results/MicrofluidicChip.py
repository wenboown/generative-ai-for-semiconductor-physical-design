import gdspy

# Create a new GDSII library
lib = gdspy.GdsLibrary()

# Create a cell to contain the layout
cell = lib.new_cell('MICROFLUIDIC_CHIP')

# Dimensions of the bulk chip
bulk_width = 30.0  # mm
bulk_height = 20.0  # mm

# Create the bulk rectangle on layer 0
bulk_rectangle = gdspy.Rectangle((0, 0), (bulk_width, bulk_height), layer=0)
cell.add(bulk_rectangle)

# Coordinates of the vias
via_radius = 2.0  # mm
via_distance = 20.0  # mm

# First via center at (5, 10)
via1_center = (5.0, 10.0)  # mm

# Second via center at (25.0, 10.0)
via2_center = (25.0, 10.0)  # mm

# Create the via circles on layer 2
via1 = gdspy.Round(via1_center, via_radius, layer=2)
via2 = gdspy.Round(via2_center, via_radius, layer=2)
cell.add([via1, via2])

# Create the channel rectangle on layer 3
channel_width = 1.0  # mm

# Channel coordinates
channel_y_min = 10.0 - channel_width / 2
channel_y_max = 10.0 + channel_width / 2
channel = gdspy.Rectangle((via1_center[0], channel_y_min), (via2_center[0], channel_y_max), layer=3)
cell.add(channel)

# Save the GDSII file
lib.write_gds('microfluidic_chip.gds')