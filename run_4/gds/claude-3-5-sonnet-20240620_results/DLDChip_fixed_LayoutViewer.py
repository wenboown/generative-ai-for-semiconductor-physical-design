import gdspy
import numpy as np

# Create a new library
lib = gdspy.GdsLibrary()

# Create the main cell
main = lib.new_cell('DLD_CHIP')

# Set the precision for the layout
gdspy.current_library.precision = 1e-9  # 1 nm precision

# Define key dimensions
pillar_diameter = 0.4  # 400 nm
gap_size = 0.225  # 225 nm
pillar_spacing = pillar_diameter + gap_size
channel_width = 30 * pillar_spacing
row_shift = 0.1 * pillar_spacing
channel_length = 100  # 100 μm long channel (adjust as needed)

# Create the pillar array
pillars = gdspy.Cell('PILLARS')
for i in range(int(channel_length / pillar_spacing)):
    for j in range(30):
        x = i * pillar_spacing + (j % 10) * row_shift
        y = j * pillar_spacing
        pillars.add(gdspy.Round((x, y), pillar_diameter/2))

# Create the channel
channel = gdspy.Rectangle((0, -gap_size/2), (channel_length, channel_width + gap_size/2))

# Create inlet and outlet
inlet = gdspy.Round((0, channel_width/2), 20)
outlet = gdspy.Round((channel_length, channel_width/2), 20)

# Create buses
inlet_bus = gdspy.Rectangle((-50, channel_width/2 - 10), (0, channel_width/2 + 10))
outlet_bus = gdspy.Rectangle((channel_length, channel_width/2 - 10), (channel_length + 50, channel_width/2 + 10))

# Add everything to the main cell
main.add(channel)
main.add(gdspy.CellReference(pillars))
main.add(inlet)
main.add(outlet)
main.add(inlet_bus)
main.add(outlet_bus)

# Save the design to a GDS file
lib.write_gds('dld_chip.gds')

# Optional: View the layout