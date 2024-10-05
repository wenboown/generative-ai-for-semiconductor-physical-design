import gdspy

# Create a new GDSII library
lib = gdspy.GdsLibrary()

# Create a cell for the microfluidic chip
cell = lib.new_cell('MICROFLUIDIC_CHIP')

# Define units (gdspy uses micrometers)
mm_to_um = 1000  # Conversion factor from mm to µm

# Chip dimensions in micrometers
chip_width = 30 * mm_to_um     # 30 mm
chip_height = 20 * mm_to_um    # 20 mm

# Create the bulk rectangle on layer 0
bulk_rectangle = gdspy.Rectangle(
    (0, 0),
    (chip_width, chip_height),
    layer=0
)
cell.add(bulk_rectangle)

# Vias specifications
via_radius = 2 * mm_to_um      # 2 mm
via_distance = 20 * mm_to_um   # 20 mm apart
chip_center_x = chip_width / 2
chip_center_y = chip_height / 2

# Calculate the centers of the two vias
via1_center = (
    chip_center_x - via_distance / 2,
    chip_center_y
)
via2_center = (
    chip_center_x + via_distance / 2,
    chip_center_y
)

# Create the two circular vias on layer 2
via1 = gdspy.Round(
    center=via1_center,
    radius=via_radius,
    number_of_points=64,
    layer=2
)
via2 = gdspy.Round(
    center=via2_center,
    radius=via_radius,
    number_of_points=64,
    layer=2
)
cell.add([via1, via2])

# Channel specifications
channel_width = 1 * mm_to_um   # 1 mm
channel_y_bottom = chip_center_y - channel_width / 2
channel_y_top = chip_center_y + channel_width / 2

# Create the rectangular channel on layer 3
channel_rectangle = gdspy.Rectangle(
    (via1_center[0], channel_y_bottom),
    (via2_center[0], channel_y_top),
    layer=3
)
cell.add(channel_rectangle)

# Save the design to a GDS file
lib.write_gds('microfluidic_chip.gds')

# Optionally, to view the layout (requires a GUI environment)