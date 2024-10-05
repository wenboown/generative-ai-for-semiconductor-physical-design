import gdspy
import numpy as np

# Define the design parameters
gap_size = 225  # nm
pillar_size = 400  # nm
width = 30  # pillars
row_shift_fraction = 0.1
inlet_diameter = 40  # um
outlet_diameter = 40  # um
bus_width = 20  # um
bus_length = 50  # um

# Convert design parameters to microns
gap_size_um = gap_size / 1000
pillar_size_um = pillar_size / 1000

# Create the GDS library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('ld_device')

# Create the pillar array
pillar_array = []
for i in range(width):
    for j in range(width):
        x = i * (pillar_size_um + gap_size_um)
        y = j * (pillar_size_um + gap_size_um) + (i % 2) * row_shift_fraction * (pillar_size_um + gap_size_um)
        pillar_array.append(gdspy.Round((x, y), pillar_size_um/2))

# Create the channel
channel = gdspy.Rectangle((0, 0), (width * (pillar_size_um + gap_size_um), width * (pillar_size_um + gap_size_um)))

# Subtract the pillar array from the channel
channel = gdspy.boolean(channel, pillar_array, 'not')

# Create the inlet and outlet
inlet = gdspy.Round((0, width * (pillar_size_um + gap_size_um) / 2), inlet_diameter/2)
outlet = gdspy.Round((width * (pillar_size_um + gap_size_um), width * (pillar_size_um + gap_size_um) / 2), outlet_diameter/2)

# Create the bus
bus_in = gdspy.Rectangle((0, width * (pillar_size_um + gap_size_um) / 2 - bus_width/2), (bus_length, width * (pillar_size_um + gap_size_um) / 2 + bus_width/2))
bus_out = gdspy.Rectangle((width * (pillar_size_um + gap_size_um) - bus_length, width * (pillar_size_um + gap_size_um) / 2 - bus_width/2), (width * (pillar_size_um + gap_size_um), width * (pillar_size_um + gap_size_um) / 2 + bus_width/2))

# Add the elements to the cell
cell.add(channel)
cell.add(inlet)
cell.add(outlet)
cell.add(bus_in)
cell.add(bus_out)

# Save the design to a GDS file
lib.write_gds('ld_device.gds')