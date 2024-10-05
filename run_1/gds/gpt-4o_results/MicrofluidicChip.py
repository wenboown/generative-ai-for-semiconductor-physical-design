import gdspy

# Create a new GDSII library
lib = gdspy.GdsLibrary()

# Create a new cell to contain the layout
cell_name = 'MICROFLUIDIC_CHIP'
cell = lib.new_cell(cell_name)

# Define the dimensions of the bulk of the chip
chip_width = 30e3   # in microns (30 mm)
chip_height = 20e3  # in microns (20 mm)

# Create the bulk of the chip on layer 0
chip_bulk = gdspy.Rectangle((0, 0), (chip_width, chip_height), layer=0)

# Add the bulk of the chip to the cell
cell.add(chip_bulk)

# Define the positions and radius for the circular vias on layer 2
via_radius = 2e3  # in microns (2 mm)
via_distance = 20e3  # in microns (20 mm)

# Center of the first via
via1_center = (chip_width / 2 - via_distance / 2, chip_height / 2)
# Center of the second via
via2_center = (chip_width / 2 + via_distance / 2, chip_height / 2)

# Create the circular vias on layer 2
via1 = gdspy.Round(via1_center, via_radius, layer=2)
via2 = gdspy.Round(via2_center, via_radius, layer=2)

# Add the vias to the cell
cell.add(via1)
cell.add(via2)

# Define the rectangle channel that connects the vias on layer 3
channel_width = 1e3  # in microns (1 mm)

# Channel coordinates
channel_x1 = via1_center[0] + via_radius
channel_x2 = via2_center[0] - via_radius
channel_y1 = via1_center[1] - channel_width / 2
channel_y2 = via1_center[1] + channel_width / 2

# Create the channel on layer 3
channel = gdspy.Rectangle((channel_x1, channel_y1), (channel_x2, channel_y2), layer=3)

# Add the channel to the cell
cell.add(channel)

# Save the design to a GDS file
gds_filename = 'microfluidic_chip.gds'
lib.write_gds(gds_filename)

print(f"GDS file '{gds_filename}' has been created.")