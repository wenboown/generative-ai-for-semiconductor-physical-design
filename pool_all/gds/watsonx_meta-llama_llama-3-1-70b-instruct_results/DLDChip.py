import gdspy


# Define the design specifications
gap_size = 0.225  # in microns
pillar_size = 0.4  # in microns
width = 30  # number of pillars
row_shift_fraction = 0.1  # fraction of row shift
inlet_diameter = 40  # in microns
outlet_diameter = 40  # in microns
bus_width = 20  # in microns
bus_length = 50  # in microns

# Create a new GDS library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell("deterministic_lateral_displacement_chip")

# Create the channel
channel = gdspy.Rectangle((0, 0), (width * pillar_size + (width - 1) * gap_size, pillar_size), layer=1)
cell.add(channel)

# Add the pillars
for i in range(width):
    pillar = gdspy.Round((i * (pillar_size + gap_size) + pillar_size/2, pillar_size/2), pillar_size/2, layer=1)
    cell.add(pillar)

# Add the row shift
row_shift = row_shift_fraction * pillar_size
for i in range(1, width):
    pillar = gdspy.Round((i * (pillar_size + gap_size) + pillar_size/2 + row_shift, pillar_size/2), pillar_size/2, layer=1)
    cell.add(pillar)

# Create the inlet and outlet
inlet = gdspy.Round((0, -inlet_diameter/2), inlet_diameter/2, layer=1)
outlet = gdspy.Round((width * pillar_size + (width - 1) * gap_size, -outlet_diameter/2), outlet_diameter/2, layer=1)
cell.add([inlet, outlet])

# Create the bus
bus_in = gdspy.Rectangle((-bus_length/2, -bus_width/2), (bus_length/2, bus_width/2), layer=1)
bus_out = gdspy.Rectangle((width * pillar_size + (width - 1) * gap_size - bus_length/2, -bus_width/2), (width * pillar_size + (width - 1) * gap_size + bus_length/2, bus_width/2), layer=1)
cell.add([bus_in, bus_out])

# Save the design to a GDS file
lib.write_gds("deterministic_lateral_displacement_chip.gds")