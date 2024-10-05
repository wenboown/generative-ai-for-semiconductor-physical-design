import numpy as np
import gdspy

# Parse the user's design specifications
gap_size = 225  # nm
pillar_size = 400  # nm
num_pillars = 30
row_shift_fraction = 0.1
inlet_outlet_diameter = 40  # µm
bus_size = (20, 50)  # µm

# Define the library and cell for the GDS layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell('dld_chip')

# Create the channel with pillars
channel_width = num_pillars * (pillar_size + gap_size)
channel_length = 100  # arbitrary length, can be adjusted

# Calculate the row shift
row_shift = row_shift_fraction * (pillar_size + gap_size)

# Create the pillar array
for i in range(num_pillars):
    for j in range(int(channel_length / (pillar_size + gap_size))):
        x = i * (pillar_size + gap_size)
        y = j * (pillar_size + gap_size) + (i % 2) * row_shift
        pillar = gdspy.Round((x, y), pillar_size / 2, number_of_points=64)
        cell.add(pillar)

# Create the channel boundary
channel_boundary = gdspy.Rectangle((0, 0), (channel_width, channel_length))
cell.add(channel_boundary)

# Create the inlet and outlet
inlet = gdspy.Round((0, channel_length / 2), inlet_outlet_diameter / 2, number_of_points=64)
outlet = gdspy.Round((channel_width, channel_length / 2), inlet_outlet_diameter / 2, number_of_points=64)
cell.add(inlet)
cell.add(outlet)

# Create the bus to connect the inlet and outlet to the channel
bus_x = channel_width / 2
bus_y = channel_length / 2
bus = gdspy.Rectangle((bus_x - bus_size[0] / 2, bus_y - bus_size[1] / 2), (bus_x + bus_size[0] / 2, bus_y + bus_size[1] / 2))
cell.add(bus)

# Save the design to a GDS file
lib.write_gds('dld_chip.gds', unit=1e-6, precision=1e-9)