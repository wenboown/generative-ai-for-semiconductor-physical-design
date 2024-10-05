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

# Calculate dimensions
pillar_center_distance = gap_size + pillar_diameter
channel_width = num_pillars_width * pillar_center_distance
channel_length = 100  # Adjust as needed

# Create pillars
for row in range(int(channel_length / pillar_center_distance)):
    row_shift = (row * row_shift_fraction * pillar_center_distance) % pillar_center_distance
    for col in range(num_pillars_width):
        x = col * pillar_center_distance + row_shift
        y = row * pillar_center_distance
        pillar = gdspy.Round((x, y), pillar_diameter / 2)
        main.add(pillar)

# Create channel
channel = gdspy.Rectangle((0, 0), (channel_width, channel_length))
main.add(channel)

# Create inlet and outlet
inlet_center = (-bus_length, channel_length / 2)
outlet_center = (channel_width + bus_length, channel_length / 2)
inlet = gdspy.Round(inlet_center, inlet_outlet_diameter / 2)
outlet = gdspy.Round(outlet_center, inlet_outlet_diameter / 2)
main.add(inlet)
main.add(outlet)

# Create buses
inlet_bus = gdspy.Rectangle(
    (inlet_center[0], inlet_center[1] - bus_width / 2),
    (0, inlet_center[1] + bus_width / 2)
)
outlet_bus = gdspy.Rectangle(
    (channel_width, outlet_center[1] - bus_width / 2),
    (outlet_center[0], outlet_center[1] + bus_width / 2)
)
main.add(inlet_bus)
main.add(outlet_bus)

# Save the design
lib.write_gds('dld_chip.gds')