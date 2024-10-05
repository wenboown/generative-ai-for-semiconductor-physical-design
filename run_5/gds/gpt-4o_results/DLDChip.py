import gdspy

# Create a new GDSII library
lib = gdspy.GdsLibrary()

# Create a new cell in the library
cell = lib.new_cell('DLD_CHIP')

# Parameters
gap_size = 225e-3  # in microns
pillar_diameter = 0.4  # in microns
num_pillars_width = 30
row_shift_fraction = 0.1

# Inlet and outlet parameters
inlet_diameter = 40  # in microns
outlet_diameter = 40  # in microns
bus_width = 20  # in microns
bus_length = 50  # in microns

# Calculate the total dimensions of the channel
channel_length = num_pillars_width * pillar_diameter / row_shift_fraction
channel_width = (num_pillars_width - 1) * (pillar_diameter + gap_size)

# Define the channel array of circular pillars
for row in range(int(channel_length / pillar_diameter)):
    for col in range(num_pillars_width):
        # Calculate the position of each pillar
        x = col * (pillar_diameter + gap_size)
        y = row * pillar_diameter + col * row_shift_fraction * pillar_diameter
        # Create pillar at position (x, y)
        pillar = gdspy.Round((x, y), pillar_diameter / 2)
        cell.add(pillar)

# Add inlet circle
inlet = gdspy.Round((-bus_length - inlet_diameter / 2, channel_width / 2), inlet_diameter / 2)
cell.add(inlet)

# Add outlet circle
outlet = gdspy.Round((channel_length + bus_length + outlet_diameter / 2, channel_width / 2), outlet_diameter / 2)
cell.add(outlet)

# Add bus connecting inlet to the channel
inlet_bus = gdspy.Rectangle((-bus_length, (channel_width - bus_width) / 2),
                            (0, (channel_width + bus_width) / 2))
cell.add(inlet_bus)

# Add bus connecting outlet to the channel
outlet_bus = gdspy.Rectangle((channel_length, (channel_width - bus_width) / 2),
                             (channel_length + bus_length, (channel_width + bus_width) / 2))
cell.add(outlet_bus)

# Add channel boundary
channel_boundary = gdspy.Rectangle((0, 0), (channel_length, channel_width), layer=1)
cell.add(channel_boundary)

# Save to a GDS file
lib.write_gds('dld_chip.gds')