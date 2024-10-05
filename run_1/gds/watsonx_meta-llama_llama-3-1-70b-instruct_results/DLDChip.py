import gdspy

# Define the design specifications
gap_size = 225  # nm
pillar_size = 400  # nm
num_pillars = 30
row_shift_fraction = 0.1
inlet_outlet_diameter = 40  # µm
bus_size = (20, 50)  # µm

# Create the GDS library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('DLD')

# Define the geometric elements
def create_pillar(x, y):
    return gdspy.Round((x, y), pillar_size/2, number_of_points=64)

def create_channel(x, y, num_pillars):
    pillars = []
    for i in range(num_pillars):
        if i % 2 == 0:
            pillars.append(create_pillar(x + i * (pillar_size + gap_size), y))
        else:
            pillars.append(create_pillar(x + (i * (pillar_size + gap_size)) - row_shift_fraction * pillar_size, y + row_shift_fraction * pillar_size))
    return pillars

def create_inlet_outlet(x, y):
    return gdspy.Circular((x, y), inlet_outlet_diameter/2, number_of_points=64)

def create_bus(x, y, width, height):
    return gdspy.Rectangle((x, y), (x + width, y + height))

# Create the inlet and outlet
inlet = create_inlet_outlet(0, 0)
outlet = create_inlet_outlet(200, 0)

# Create the bus
bus1 = create_bus(0, -25, bus_size[0], bus_size[1])
bus2 = create_bus(200, -25, bus_size[0], bus_size[1])

# Create the channel
channel = create_channel(20, -50, num_pillars)

# Add the elements to the cell
cell.add(inlet)
cell.add(outlet)
cell.add(bus1)
cell.add(bus2)
for pillar in channel:
    cell.add(pillar)

# Save the design to a GDS file
lib.write_gds('DLD.gds')