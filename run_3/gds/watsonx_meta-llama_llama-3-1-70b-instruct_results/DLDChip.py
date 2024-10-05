import gdspy

# Define the design parameters
gap_size = 225  # nm
pillar_size = 400  # nm
width = 30  # number of pillars
row_shift_fraction = 0.1
inlet_outlet_diameter = 40  # µm
bus_width = 20  # µm
bus_length = 50  # µm

# Create the GDS library and cell
lib = gdspy.Library()
cell = lib.new_cell("DLDDesign")

# Define the channel parameters
channel_length = pillar_size * width / (1 - row_shift_fraction)
channel_width = pillar_size + gap_size

# Create the channel
channel = gdspy.Rectangle((0, 0), (channel_length, channel_width))
cell.add(channel)

# Create the array of pillars
for i in range(width):
    for j in range(int(width / (1 - row_shift_fraction))):
        x = i * pillar_size + j * pillar_size * row_shift_fraction
        y = 0
        if i % 2 == 1:
            y = gap_size / 2
        pillar = gdspy.Round((x, y), pillar_size / 2, num_points=128)
        cell.add(pillar)

# Create the inlet
inlet = gdspy.Round((channel_length / 2 - inlet_outlet_diameter / 2, -inlet_outlet_diameter / 2), inlet_outlet_diameter / 2, num_points=128)
cell.add(inlet)

# Create the outlet
outlet = gdspy.Round((channel_length / 2 - inlet_outlet_diameter / 2, channel_width + inlet_outlet_diameter / 2), inlet_outlet_diameter / 2, num_points=128)
cell.add(outlet)

# Create the bus connecting the inlet and outlet to the channel
bus1 = gdspy.Rectangle((channel_length / 2 - bus_width / 2, -bus_length), (channel_length / 2 + bus_width / 2, -inlet_outlet_diameter / 2))
bus2 = gdspy.Rectangle((channel_length / 2 - bus_width / 2, channel_width + inlet_outlet_diameter / 2), (channel_length / 2 + bus_width / 2, channel_width + bus_length))
cell.add(bus1)
cell.add(bus2)

# Save the design to a GDS file
lib.write_gds("dld_design.gds")