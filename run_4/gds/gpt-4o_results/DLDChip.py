import gdspy

# Specifications
gap_size = 225  # in nm
pillar_diameter = 400  # in nm
width_pillars = 30
row_shift_fraction = 0.1
inlet_outlet_diameter = 40e3  # in nm (40 µm)
bus_width = 20e3  # in nm (20 µm)
bus_length = 50e3  # in nm (50 µm)

# Calculate the height of the pillar array
pillar_radius = pillar_diameter / 2
row_height = pillar_diameter + gap_size
num_rows = int(width_pillars / row_shift_fraction)

# Create a new GDSII library and a cell for our design
lib = gdspy.GdsLibrary()
cell = lib.new_cell('DLD_CHIP')

# Create the pillars array
for r in range(num_rows):
    y_shift = r * row_height
    x_shift = (r * row_shift_fraction) * (pillar_diameter + gap_size)
    for c in range(width_pillars):
        x_center = c * (pillar_diameter + gap_size) + x_shift
        y_center = y_shift
        pillar = gdspy.Round((x_center, y_center), pillar_radius)
        cell.add(pillar)

# Total height of the array
total_height = (num_rows - 1) * row_height + pillar_diameter

# Add Inlet
inlet = gdspy.Round((0, total_height + bus_length), inlet_outlet_diameter / 2)
cell.add(inlet)

# Add Outlet
outlet_position = ((width_pillars - 1) * (pillar_diameter + gap_size), -(bus_length + inlet_outlet_diameter/2))
outlet = gdspy.Round(outlet_position, inlet_outlet_diameter / 2)
cell.add(outlet)

# Add the bus connections
# From Inlet to bottom of array
bus1 = gdspy.Rectangle((-bus_width / 2, total_height), (bus_width / 2, total_height + bus_length))
cell.add(bus1)

# From top of array to Outlet
bus2 = gdspy.Rectangle((outlet_position[0] - bus_width / 2, -bus_length), (outlet_position[0] + bus_width / 2, 0))
cell.add(bus2)

# Save to a GDS file
output_file = 'dld_chip.gds'
lib.write_gds(output_file)

# Ensure the library is cleaned up
lib.close()
sh
pip install gdspy