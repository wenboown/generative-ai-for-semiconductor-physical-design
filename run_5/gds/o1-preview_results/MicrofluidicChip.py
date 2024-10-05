import gdspy

# Create a new GDSII library
lib = gdspy.GdsLibrary()

# Create a new cell for the microfluidic chip
cell = lib.new_cell('MICROFLUIDIC_CHIP')

# Define dimensions in microns (1 mm = 1000 microns)
# Bulk of the chip (Layer 0)
bulk_width = 30000   # 30 mm in microns
bulk_height = 20000  # 20 mm in microns
bulk_rect = gdspy.Rectangle((0, 0), (bulk_width, bulk_height), layer=0)
cell.add(bulk_rect)

# Vias (Layer 2)
via_radius = 2000  # 2 mm in microns
via_spacing = 20000  # 20 mm apart horizontally in microns
via_y = bulk_height / 2  # Centered vertically in the bulk

# First via at (5 mm, 10 mm)
via1_center = (5000, via_y)
via1 = gdspy.Round(via1_center, via_radius, layer=2)
cell.add(via1)

# Second via at (25 mm, 10 mm)
via2_center = (via1_center[0] + via_spacing, via_y)
via2 = gdspy.Round(via2_center, via_radius, layer=2)
cell.add(via2)

# Channel connecting the vias (Layer 3)
channel_width = 1000  # 1 mm in microns
channel_left = via1_center[0]
channel_right = via2_center[0]
channel_bottom = via_y - channel_width / 2
channel_top = via_y + channel_width / 2
channel_rect = gdspy.Rectangle(
    (channel_left, channel_bottom),
    (channel_right, channel_top),
    layer=3
)
cell.add(channel_rect)

# Write the GDSII file
lib.write_gds('microfluidic_chip.gds')