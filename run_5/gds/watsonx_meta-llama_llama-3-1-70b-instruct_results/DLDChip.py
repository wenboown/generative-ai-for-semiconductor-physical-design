import gdspy
import math

# Define design parameters
gap_size = 0.225  # in µm
pillar_size = 0.4  # in µm
width = 30  # number of pillars
row_shift_fraction = 0.1  # fraction of pillar size
inlet_outlet_diameter = 40  # in µm
bus_size = (20, 50)  # in µm

# Create a new library and cell
lib = gdspy.Library()
cell = lib.new_cell('DLDA')

# Define a function to create a circular pillar
def create_pillar(x, y, size):
    return gdspy.Round((x, y), size/2, number_of_points=128)

# Define a function to create a channel
def create_channel(x, y, width, gap_size, pillar_size, row_shift_fraction):
    pillars = []
    for i in range(width):
        for j in range(width):
            x_pos = x + (i * (pillar_size + gap_size)) + (j % 2) * row_shift_fraction * pillar_size
            y_pos = y + j * (pillar_size + gap_size)
            pillars.append(create_pillar(x_pos, y_pos, pillar_size))
    return pillars

# Create the channel
channel_x = 10  # in µm
channel_y = 10  # in µm
channel_pillars = create_channel(channel_x, channel_y, width, gap_size, pillar_size, row_shift_fraction)

# Create the inlet and outlet
inlet = gdspy.Round((5, 25), inlet_outlet_diameter/2, number_of_points=128)
outlet = gdspy.Round((45, 25), inlet_outlet_diameter/2, number_of_points=128)

# Create the bus
bus = gdspy.Rectangle((5, 15), (45, 35))

# Add all shapes to the cell
cell.add(channel_pillars)
cell.add(inlet)
cell.add(outlet)
cell.add(bus)

# Save the design to a GDS file
lib.write_gds('DLDA.gds')