import gdspy

# Create a new GDSII library
lib = gdspy.GdsLibrary()

# Create a cell for the DLD chip
cell = lib.new_cell('DLD_CHIP')

# Parameters
gap_size = 0.225  # in micrometers (225 nm)
pillar_diameter = 0.4  # in micrometers (400 nm)
width = 30  # number of pillars in x-direction
shift_fraction = 0.1  # shift fraction per row
num_rows = 100  # number of rows in y-direction

# Compute the pitch (distance from center to center of pillars)
pitch = pillar_diameter + gap_size

# Create the DLD array
for row in range(num_rows):
    y = row * pitch
    shift = (row * shift_fraction * pitch) % (pitch)
    for col in range(width):
        x = (col * pitch) + shift
        pillar = gdspy.Round((x, y), pillar_diameter / 2)
        cell.add(pillar)

# Calculate the total height and width of the DLD array
array_width = (width - 1) * pitch + pillar_diameter
array_height = (num_rows - 1) * pitch + pillar_diameter

# Create the channel enclosing the DLD array
channel_margin = 5  # micrometers margin around the array
channel_width = array_width + 2 * channel_margin
channel_height = array_height + 2 * channel_margin
channel_rect = gdspy.Rectangle(
    (-channel_margin, -channel_margin),
    (array_width + channel_margin, array_height + channel_margin)
)
cell.add(channel_rect)

# Inlet and Outlet parameters
inlet_diameter = 40  # micrometers
outlet_diameter = 40  # micrometers

# Bus parameters
bus_width = 20  # micrometers
bus_length = 50  # micrometers

# Create the inlet circle
inlet_center = (array_width / 2, -channel_margin - bus_length - inlet_diameter / 2)
inlet = gdspy.Round(inlet_center, inlet_diameter / 2)
cell.add(inlet)

# Create the bus connecting inlet to the channel
inlet_bus = gdspy.Rectangle(
    (array_width / 2 - bus_width / 2, -channel_margin - bus_length),
    (array_width / 2 + bus_width / 2, -channel_margin)
)
cell.add(inlet_bus)

# Create the outlet circle
outlet_center = (array_width / 2, array_height + channel_margin + bus_length + outlet_diameter / 2)
outlet = gdspy.Round(outlet_center, outlet_diameter / 2)
cell.add(outlet)

# Create the bus connecting channel to the outlet
outlet_bus = gdspy.Rectangle(
    (array_width / 2 - bus_width / 2, array_height + channel_margin),
    (array_width / 2 + bus_width / 2, array_height + channel_margin + bus_length)
)
cell.add(outlet_bus)

# Save the design to a GDS file
lib.write_gds('dld_chip.gds')