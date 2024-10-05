import gdspy
import numpy as np

# Create a new library
lib = gdspy.GdsLibrary()

# Create the main cell
main = lib.new_cell('DLD_CHIP')

# Parameters
gap_size = 0.225  # 225 nm
pillar_diameter = 0.4  # 400 nm
num_pillars_width = 30
row_shift_fraction = 0.1
inlet_outlet_diameter = 40  # 40 µm
bus_width = 20  # 20 µm
bus_length = 50  # 50 µm

# Calculate additional parameters
pillar_spacing = pillar_diameter + gap_size
channel_width = num_pillars_width * pillar_spacing
row_height = pillar_spacing / np.tan(np.arcsin(row_shift_fraction))
num_rows = 100

# Channel outline
channel_length = num_rows * row_height
channel = gdspy.Rectangle((0, 0), (channel_width, channel_length))
main.add(channel)

# Create pillar array
pillar = gdspy.Round((0, 0), pillar_diameter/2, number_of_points=64)
pillar_array = gdspy.CellArray(pillar, num_pillars_width, num_rows,
                               (pillar_spacing, row_height),
                               origin=(pillar_diameter/2, pillar_diameter/2))
main.add(pillar_array)

# Shift odd rows
for i in range(1, num_rows, 2):
    row = gdspy.CellArray(pillar, num_pillars_width, 1, (pillar_spacing, row_height),
                          origin=(pillar_diameter/2 + pillar_spacing*row_shift_fraction, pillar_diameter/2 + i*row_height))
    main.add(row)

# Inlet and outlet
inlet = gdspy.Round((channel_width/2, -inlet_outlet_diameter/2-bus_length), inlet_outlet_diameter/2, number_of_points=64)
outlet = gdspy.Round((channel_width/2, channel_length+inlet_outlet_diameter/2+bus_length), inlet_outlet_diameter/2, number_of_points=64)
main.add(inlet)
main.add(outlet)

# Buses
inlet_bus = gdspy.Rectangle((channel_width/2-bus_width/2, -bus_length), (channel_width/2+bus_width/2, 0))
outlet_bus = gdspy.Rectangle((channel_width/2-bus_width/2, channel_length), (channel_width/2+bus_width/2, channel_length+bus_length))
main.add(inlet_bus)
main.add(outlet_bus)

# Save the layout to a GDSII file
lib.write_gds('dld_chip.gds')

# Display all cells using the internal viewer