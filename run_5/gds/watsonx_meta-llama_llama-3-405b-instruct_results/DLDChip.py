import gdspy
import numpy as np

# Parse user's design specifications
gap_size = 225  # nm
pillar_size = 400  # nm
width = 30  # pillars
row_shift_fraction = 0.1
inlet_diameter = 40  # um
outlet_diameter = 40  # um
bus_width = 20  # um
bus_length = 50  # um

# Define the library and cell for the GDS layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell('Deterministic Lateral Displacement Chip')

# Create the pillar array
pillar spacing = pillar_size + gap_size
row_shift = pillar_size * row_shift_fraction
for i in range(width):
    for j in range(width):
        x = i * pillar_spacing + (j % 2) * row_shift
        y = j * pillar_spacing
        pillar = gdspy.Round((x, y), pillar_size/2)
        cell.add(pillar)

# Create the channel
channel_width = width * pillar_spacing + pillar_size
channel_length = width * pillar_spacing
channel = gdspy.Rectangle((0, 0), (channel_length, channel_width))
cell.add(channel)

# Create the inlet and outlet
inlet = gdspy.Round((0, channel_width/2), inlet_diameter/2)
outlet = gdspy.Round((channel_length, channel_width/2), outlet_diameter/2)
cell.add(inlet)
cell.add(outlet)

# Create the bus to connect the inlet and outlet to the channel
bus_in = gdspy.Rectangle((0, channel_width/2 - bus_width/2), (bus_length, channel_width/2 + bus_width/2))
bus_out = gdspy.Rectangle((channel_length - bus_length, channel_width/2 - bus_width/2), (channel_length, channel_width/2 + bus_width/2))
cell.add(bus_in)
cell.add(bus_out)

# Save the design to a GDS file
lib.write_gds('deterministic_lateral_displacement_chip.gds')