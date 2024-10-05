import gdspy

# Create a new GDSII library
lib = gdspy.GdsLibrary()

# Create a cell to add elements
cell = lib.new_cell('DLD_CHIP')

# Parameters
gap_size = 0.225  # Gap size in micrometers (225 nm)
pillar_diameter = 0.4  # Pillar diameter in micrometers (400 nm)
pillar_radius = pillar_diameter / 2

row_shift_fraction = 0.1  # Row shift fraction
width_in_pillars = 30  # Width of the array in number of pillars

inlet_diameter = 40  # Inlet diameter in micrometers
outlet_diameter = 40  # Outlet diameter in micrometers

bus_width = 20  # Bus width in micrometers
bus_length = 50  # Bus length in micrometers

# Calculations
pillar_pitch = pillar_diameter + gap_size  # Center-to-center distance between pillars
y_spacing = pillar_pitch * (3 ** 0.5) / 2  # Vertical spacing for hexagonal packing

number_of_rows = int(1 / row_shift_fraction) * 10  # Total rows to complete multiple shift cycles

# Create the pillar array
for row in range(number_of_rows):
    y = row * y_spacing
    row_shift = (row * row_shift_fraction * pillar_pitch) % pillar_pitch
    for col in range(width_in_pillars):
        x = (col * pillar_pitch) + row_shift
        pillar = gdspy.Round((x, y), pillar_radius)
        cell.add(pillar)

# Calculate the array dimensions
array_width = width_in_pillars * pillar_pitch
array_height = number_of_rows * y_spacing
array_center_y = array_height / 2

# Create the inlet
inlet_center = (-bus_length - inlet_diameter / 2, array_center_y)
inlet = gdspy.Round(inlet_center, inlet_diameter / 2)
cell.add(inlet)

# Create the outlet
outlet_center = (array_width + bus_length + outlet_diameter / 2, array_center_y)
outlet = gdspy.Round(outlet_center, outlet_diameter / 2)
cell.add(outlet)

# Create the inlet bus
inlet_bus = gdspy.Rectangle(
    (-bus_length, array_center_y - bus_width / 2),
    (0, array_center_y + bus_width / 2)
)
cell.add(inlet_bus)

# Create the outlet bus
outlet_bus = gdspy.Rectangle(
    (array_width, array_center_y - bus_width / 2),
    (array_width + bus_length, array_center_y + bus_width / 2)
)
cell.add(outlet_bus)

# Save the GDSII file
lib.write_gds('dld_chip.gds')