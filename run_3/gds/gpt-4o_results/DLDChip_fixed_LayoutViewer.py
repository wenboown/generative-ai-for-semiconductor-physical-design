import gdspy

# Define the library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('DLD_CHIP')

# Channel and pillars parameters
pillar_size = 0.4 # in micrometers (um)
gap_size = 0.225 # in micrometers (um)
width_pillars = 30
height_pillars = 100 # assuming a large number of rows for the sake of the example
row_shift_fraction = 0.1
pillar_radius = pillar_size / 2

# Inlet/outlet parameters
inlet_outlet_diameter = 40.0 # in micrometers (um)
bus_width = 20.0 # in micrometers (um)
bus_length = 50.0 # in micrometers (um)

# Coordinates for the inlet, channel, and outlet
start_x = 0
start_y = 0
bus_inlet_end = start_x + bus_length
channel_start_x = bus_inlet_end
channel_width = (width_pillars * (pillar_size + gap_size)) - gap_size
inlet_center_x = start_x + (inlet_outlet_diameter / 2)

# Add inlet circle
inlet = gdspy.Round(
    (inlet_center_x, start_y),
    inlet_outlet_diameter / 2,
    number_of_points=64,
)
cell.add(inlet)

# Add inlet bus
inlet_bus = gdspy.Rectangle(
    (start_x, start_y - bus_width / 2),
    (bus_inlet_end, start_y + bus_width / 2)
)
cell.add(inlet_bus)

# Configure the pillars within the channel
current_x = channel_start_x
current_y = start_y

for i in range(height_pillars):
    for j in range(width_pillars):
        center_x = current_x + j * (pillar_size + gap_size)
        center_y = current_y + (i * (pillar_size + gap_size)) + (pillar_size + gap_size) * row_shift_fraction * i
        
        # Add each pillar to the cell
        pillar = gdspy.Round(
            (center_x, center_y),
            pillar_radius,
            number_of_points=64,
        )
        cell.add(pillar)

# Add outlet bus
channel_end_x = current_x + (width_pillars - 1) * (pillar_size + gap_size)
bus_outlet_start = channel_end_x + pillar_radius + gap_size / 2
bus_outlet_end = bus_outlet_start + bus_length

outlet_bus = gdspy.Rectangle(
    (bus_outlet_start, start_y - bus_width / 2),
    (bus_outlet_end, start_y + bus_width / 2)
)
cell.add(outlet_bus)

# Add outlet circle
outlet_center_x = bus_outlet_end + (inlet_outlet_diameter / 2)

outlet = gdspy.Round(
    (outlet_center_x, start_y),
    inlet_outlet_diameter / 2,
    number_of_points=64,
)
cell.add(outlet)

# Save the layout to a GDS file
lib.write_gds('dld_chip.gds')

# Optionally display the layout using a viewer