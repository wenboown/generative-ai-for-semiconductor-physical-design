import gdspy
import numpy as np

# Create a new library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('DLD_Chip')

# Define parameters
gap_size = 0.225  # 225 nm
pillar_diameter = 0.4  # 400 nm
num_pillars_width = 30
row_shift_fraction = 0.1
inlet_outlet_diameter = 40  # 40 µm
bus_width = 20  # 20 µm
bus_length = 50  # 50 µm

# Calculate derived dimensions
pillar_center_distance = gap_size + pillar_diameter
array_width = num_pillars_width * pillar_center_distance
row_shift = pillar_center_distance * row_shift_fraction

# Calculate the number of rows needed to achieve a full shift
num_rows = int(1 / row_shift_fraction)

# Create the pillar array
for col in range(num_pillars_width):
    for row in range(num_rows):
        x = col * pillar_center_distance + (row * row_shift) % pillar_center_distance
        y = row * pillar_center_distance
        pillar = gdspy.Round((x, y), pillar_diameter / 2)
        cell.add(pillar)

# Create the channel
channel_width = array_width + gap_size
channel_height = num_rows * pillar_center_distance + gap_size
channel = gdspy.Rectangle((0, -gap_size/2), (channel_width, channel_height + gap_size/2))
cell.add(channel)

# Create inlet and outlet
inlet_center = (-bus_length, channel_height / 2)
outlet_center = (channel_width + bus_length, channel_height / 2)
inlet = gdspy.Round(inlet_center, inlet_outlet_diameter / 2)
outlet = gdspy.Round(outlet_center, inlet_outlet_diameter / 2)

# Create buses
inlet_bus = gdspy.Rectangle(
    (inlet_center[0], inlet_center[1] - bus_width / 2),
    (0, inlet_center[1] + bus_width / 2)
)
outlet_bus = gdspy.Rectangle(
    (channel_width, outlet_center[1] - bus_width / 2),
    (outlet_center[0], outlet_center[1] + bus_width / 2)
)

# Add inlet, outlet, and buses to the cell
cell.add(inlet)
cell.add(outlet)
cell.add(inlet_bus)
cell.add(outlet_bus)

# Save the design to a GDS file
lib.write_gds('dld_chip.gds')

# Display the layout (optional, requires a GUI)