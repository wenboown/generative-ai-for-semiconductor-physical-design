import gdspy

# Define design parameters
gap_size = 0.225  # micrometers
pillar_diameter = 0.4  # micrometers
num_pillars_width = 30
row_shift_fraction = 0.1
inlet_outlet_diameter = 40  # micrometers
bus_width = 20  # micrometers
bus_length = 50  # micrometers

# Initialize the GDS library and main cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('DLD_CHIP')

# Create a circular pillar
def create_pillar(x, y, diameter):
    return gdspy.Round((x, y), diameter / 2)

# Create pillar array with deterministic lateral displacement
for row in range(int(1 / row_shift_fraction)):
    for col in range(num_pillars_width):
        x = col * (pillar_diameter + gap_size)
        y = row * (pillar_diameter + gap_size) + (col * row_shift_fraction * (pillar_diameter + gap_size))
        pillar = create_pillar(x, y, pillar_diameter)
        cell.add(pillar)

# Create inlet and outlet
inlet = gdspy.Round((-bus_length, 0), inlet_outlet_diameter / 2)
outlet = gdspy.Round((num_pillars_width * (pillar_diameter + gap_size), 0), outlet_outlet_diameter / 2)

# Create buses
inlet_bus = gdspy.Rectangle((-bus_length, -bus_width / 2), (0, bus_width / 2))
outlet_bus = gdspy.Rectangle((num_pillars_width * (pillar_diameter + gap_size), -bus_width / 2), 
                             (num_pillars_width * (pillar_diameter + gap_size) + bus_length, bus_width / 2))

# Add elements to the cell
cell.add(inlet)
cell.add(outlet)
cell.add(inlet_bus)
cell.add(outlet_bus)

# Save the design to a GDS file
lib.write_gds('dld_chip.gds')