import gdspy

# Define design parameters
gap_size = 0.225  # in micrometers
pillar_diameter = 0.4  # in micrometers
channel_width = 30 * pillar_diameter + 29 * gap_size  # total width composed of 30 pillars and 29 gaps
row_shift_fraction = 0.1
inlet_diameter = 40  # in micrometers
outlet_diameter = 40  # in micrometers
bus_width = 20  # width of the bus line in micrometers
bus_length = 50  # length of the bus line in micrometers

# Initialize the GDS library and main cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('DLD_CHIP')

# Define functions to create various geometric elements
def create_circle(center, diameter):
    return gdspy.Round(center, diameter/2)

def create_pillar_array(rows, cols, diameter, gap, shift_fraction):
    pillars = []
    for i in range(rows):
        for j in range(cols):
            x = j * (diameter + gap)
            y = i * (diameter + gap) + i * (diameter + shift_fraction)
            pillars.append(gdspy.Round((x, y), diameter/2))
    return gdspy.boolean(pillars, None, 'or')

# Create the inlet
inlet = create_circle((0, 0), inlet_diameter)
cell.add(inlet)

# Create the bus from inlet to channel
bus_to_channel = gdspy.Rectangle((inlet_diameter/2, -bus_width/2), 
                                 (inlet_diameter/2 + bus_length, bus_width/2))
cell.add(bus_to_channel)

# Create the DLD pillar array
rows = 30  # Adjust to desired number of rows
cols = 30
pillar_array = create_pillar_array(rows, cols,
                                   pillar_diameter, 
                                   gap_size, 
                                   row_shift_fraction)
pillar_array_ref = gdspy.CellReference(
    gdspy.Cell('PILLAR_ARRAY', exclude_from_current=True)
)
cell.add(pillar_array)
pillar_array.translate(inlet_diameter/2 + bus_length, -rows * (pillar_diameter + gap_size)/2)

# Create the bus from channel to outlet
bus_to_outlet = gdspy.Rectangle((inlet_diameter/2 + bus_length + channel_width, -bus_width/2), 
                                (inlet_diameter/2 + bus_length + channel_width + bus_length, bus_width/2))
cell.add(bus_to_outlet)

# Create the outlet
outlet = create_circle((inlet_diameter/2 + 2 * bus_length + channel_width, 0), outlet_diameter)
cell.add(outlet)

# Save the design to a GDS file
gds_name = 'dld_chip.gds'
lib.write_gds(gds_name)
print(f"GDS file {gds_name} created successfully.")