import gdspy

# Define the design specifications
gap_size = 0.225  # in microns
pillar_size = 0.4  # in microns
width = 30  # number of pillars
row_shift_fraction = 0.1  # fraction of pillar size
inlet_diameter = 40  # in microns
outlet_diameter = 40  # in microns
bus_width = 20  # in microns
bus_height = 50  # in microns

# Create the GDS library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('deterministic_lateral_displacement_chip')

# Create the channel with pillars
pillar_spacing = gap_size + pillar_size
channel_length = width * pillar_spacing
channel_width = pillar_size + 2 * gap_size

# Create the channel shape
channel = gdspy.Rectangle((0, 0), (channel_length, channel_width))
cell.add(channel)

# Create the pillars
for i in range(width):
    x = i * pillar_spacing + gap_size
    y = gap_size + row_shift_fraction * pillar_size if i % 2 else gap_size
    pillar = gdspy.Round((x, y), pillar_size/2)
    cell.add(pillar)

# Create the inlet and outlet
inlet = gdspy.Round((0, channel_width + bus_height), inlet_diameter/2)
outlet = gdspy.Round((channel_length, channel_width + bus_height), outlet_diameter/2)
cell.add(inlet)
cell.add(outlet)

# Create the bus to connect the inlet and outlet to the channel
bus_in = gdspy.Rectangle((0, channel_width), (bus_width, channel_width + bus_height))
bus_out = gdspy.Rectangle((channel_length - bus_width, channel_width), (channel_length, channel_width + bus_height))
cell.add(bus_in)
cell.add(bus_out)

# Save the design to a GDS file
lib.write_gds('deterministic_lateral_displacement_chip.gds')