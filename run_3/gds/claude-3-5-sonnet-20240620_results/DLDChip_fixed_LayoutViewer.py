import gdspy
import numpy as np

# Create a new library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('DLD_CHIP')

# Parameters
gap_size = 0.225  # 225 nm
pillar_diameter = 0.4  # 400 nm
num_pillars_width = 30
row_shift_fraction = 0.1
inlet_outlet_diameter = 40  # 40 µm
bus_width = 20  # 20 µm
bus_length = 50  # 50 µm

# Calculated dimensions
pillar_center_distance = pillar_diameter + gap_size
channel_width = num_pillars_width * pillar_center_distance
row_shift = row_shift_fraction * pillar_center_distance

# Create main channel
channel_length = 100  # Adjust as needed
channel = gdspy.Rectangle((0, 0), (channel_length, channel_width))
cell.add(channel)

# Add pillars
num_rows = int(channel_length / pillar_center_distance)
for row in range(num_rows):
    for col in range(num_pillars_width):
        x = row * pillar_center_distance + (row * row_shift) % pillar_center_distance
        y = col * pillar_center_distance
        pillar = gdspy.Round((x, y), pillar_diameter/2)
        cell.add(pillar)

# Create inlet and outlet
inlet_center = (-bus_length, channel_width/2)
outlet_center = (channel_length + bus_length, channel_width/2)
inlet = gdspy.Round(inlet_center, inlet_outlet_diameter/2)
outlet = gdspy.Round(outlet_center, inlet_outlet_diameter/2)
cell.add(inlet)
cell.add(outlet)

# Add connecting buses
inlet_bus = gdspy.Rectangle(
    (inlet_center[0], channel_width/2 - bus_width/2),
    (0, channel_width/2 + bus_width/2)
)
outlet_bus = gdspy.Rectangle(
    (channel_length, channel_width/2 - bus_width/2),
    (outlet_center[0], channel_width/2 + bus_width/2)
)
cell.add(inlet_bus)
cell.add(outlet_bus)

# Save the design
lib.write_gds('dld_chip.gds')

# Optional: View the layout