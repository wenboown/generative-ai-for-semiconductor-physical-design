import gdspy
import numpy as np

# Define the design specifications
gap_size = 225  # nm
pillar_size = 400  # nm
width = 30  # number of pillars
row_shift_fraction = 0.1
inlet_outlet_diameter = 40  # µm
bus_width = 20  # µm
bus_length = 50  # µm

# Define the library and cell for the GDS layout
lib = gdspy.Library()
cell = lib.new_cell('dld_chip')

# Create the inlet
inlet = gdspy.Round(
    (0, 0), 
    inlet_outlet_diameter / 2, 
    tolerance=1e-4, 
    max_points=0, 
    layer=0, 
    datatype=0
)
cell.add(inlet)

# Calculate the channel dimensions
channel_length = pillar_size * width
channel_height = pillar_size

# Create the channel
channel_poly = gdspy.Rectangle(
    (0, -channel_height / 2), 
    (channel_length, channel_height / 2), 
    layer=0, 
    datatype=0
)
cell.add(channel_poly)

# Create the pillar array
pillar_x = pillar_size / 2
pillar_y = -channel_height / 2 + pillar_size / 2
for i in range(width):
    for j in range(int(channel_length / pillar_size)):
        pillar = gdspy.Round(
            (pillar_x + i * pillar_size + j * pillar_size * row_shift_fraction, 
             pillar_y + j * pillar_size), 
            pillar_size / 2, 
            tolerance=1e-4, 
            max_points=0, 
            layer=1, 
            datatype=0
        )
        cell.add(pillar)

# Create the bus
bus_poly = gdspy.Rectangle(
    (-bus_length / 2, -channel_height / 2 - bus_width / 2), 
    (bus_length / 2, -channel_height / 2 + bus_width / 2), 
    layer=0, 
    datatype=0
)
cell.add(bus_poly)

# Create the outlet
outlet = gdspy.Round(
    (channel_length + bus_length, 0), 
    inlet_outlet_diameter / 2, 
    tolerance=1e-4, 
    max_points=0, 
    layer=0, 
    datatype=0
)
cell.add(outlet)

# Save the design to a GDS file
gdspy.write_gds('dld_chip.gds', lib, unit=1e-6, precision=1e-9)