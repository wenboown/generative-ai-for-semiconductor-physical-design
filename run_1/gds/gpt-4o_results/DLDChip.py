import gdspy

# Parameters for the design
gap_size = 225e-3  # 225 nm converted to micrometers
pillar_diameter = 400e-3  # 400 nm converted to micrometers
num_pillars_width = 30
row_shift_fraction = 0.1
inlet_diameter = 40.0  # µm
outlet_diameter = 40.0  # µm
bus_width = 20.0  # µm
bus_length = 50.0  # µm

# Create a GDSII library and a cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('DLD_CHIP')

# Helper functions to place elements
def create_circle(center, radius, layer=0):
    return gdspy.Round(center, radius, layer=layer)

def create_rectangle(bottom_left, top_right, layer=0):
    return gdspy.Rectangle(bottom_left, top_right, layer=layer)

# Create Inlet
inlet = create_circle((inlet_diameter / 2, inlet_diameter / 2), inlet_diameter / 2)
cell.add(inlet)

# Create Outlet
outlet = create_circle((inlet_diameter / 2 + num_pillars_width * (pillar_diameter + gap_size) + 2 * bus_length, inlet_diameter / 2), outlet_diameter / 2)
cell.add(outlet)

# Connect Inlet to Channel
inlet_bus = create_rectangle((inlet_diameter / 2, inlet_diameter), (inlet_diameter / 2 + bus_length, inlet_diameter + bus_width))
cell.add(inlet_bus)

# Connect Channel to Outlet
outlet_bus = create_rectangle((inlet_diameter / 2 + num_pillars_width * (pillar_diameter + gap_size) + bus_length, inlet_diameter),
                              (inlet_diameter / 2 + num_pillars_width * (pillar_diameter + gap_size) + 2 * bus_length, inlet_diameter + bus_width))
cell.add(outlet_bus)

# Create Channel with pillars
for row in range(int(num_pillars_width / row_shift_fraction)):
    row_y = inlet_diameter + bus_width + row * (pillar_diameter + gap_size)
    shift_x = (row % int(1 / row_shift_fraction)) * row_shift_fraction * (pillar_diameter + gap_size)
    for col in range(num_pillars_width):
        pillar_x = inlet_diameter / 2 + bus_length + col * (pillar_diameter + gap_size) + shift_x
        pillar = create_circle((pillar_x, row_y), pillar_diameter / 2)
        cell.add(pillar)

# Write the GDS file
lib.write_gds('dld_chip.gds')