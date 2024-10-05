import gdspy

# Create a GDS Library
gdsii_lib = gdspy.GdsLibrary()

# Create a cell to contain the design
cell = gdsii_lib.new_cell('MICROFLUIDIC_CHIP')

# Define the bulk of the chip (30 mm x 20 mm rectangle) on layer 0
chip_bulk = gdspy.Rectangle((0, 0), (30000, 20000), layer=0)
cell.add(chip_bulk)

# Define two circular vias with 2 mm radius on layer 2
via_radius = 2000  # 2 mm radius
via_distance = 20000  # 20 mm apart horizontally

# First via centered at (5000, 10000)
via1_center = (5000, 10000)
via1 = gdspy.Round(via1_center, via_radius, layer=2)

# Second via centered at (25000, 10000)
via2_center = (25000, 10000)
via2 = gdspy.Round(via2_center, via_radius, layer=2)

cell.add(via1)
cell.add(via2)

# Define a rectangular channel connecting the center of the two vias on layer 3
channel_width = 1000  # 1 mm width
channel_height = abs(via2_center[0] - via1_center[0])  # Distance between vias
channel_center_y = via1_center[1]

channel = gdspy.Rectangle((via1_center[0], channel_center_y - channel_width / 2),
                          (via2_center[0], channel_center_y + channel_width / 2), layer=3)

cell.add(channel)

# Save the GDS file
gdsii_lib.write_gds('microfluidic_chip.gds')

# Optionally, display the layout using the internal viewer of `gdspy`