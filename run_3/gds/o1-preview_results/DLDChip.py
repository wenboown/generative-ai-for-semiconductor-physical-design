import gdspy

# Create the main library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('DLD_Chip')

# Parameters (all dimensions in micrometers)
pillar_diameter = 0.4         # Pillar diameter (400 nm)
gap_size = 0.225              # Gap size between pillars (225 nm)
pitch = pillar_diameter + gap_size    # Pitch between pillars
row_shift_fraction = 0.1       # Row shift fraction

pillars_in_x = 30              # Number of pillars in x-direction (width)
rows = 100                     # Number of rows in y-direction
vertical_pitch = pitch         # Vertical pitch between rows

inlet_diameter = 40            # Inlet diameter
outlet_diameter = 40           # Outlet diameter

bus_width = 20                 # Bus width
bus_length = 50                # Bus length

# Starting positions
x0 = 0
y0 = 0

# Compute array extents
array_width = (pillars_in_x - 1) * pitch + pillar_diameter  # Total width of the pillar array
array_height = (rows - 1) * vertical_pitch + pillar_diameter  # Total height of the pillar array

# Positions for inlet and outlet
y_center = y0 + array_height / 2

x_inlet = x0 - bus_length - inlet_diameter / 2
y_inlet = y_center

x_outlet = x0 + array_width + bus_length + outlet_diameter / 2
y_outlet = y_center

# Create inlet circle
inlet_circle = gdspy.Round((x_inlet, y_inlet), inlet_diameter / 2)
cell.add(inlet_circle)

# Create outlet circle
outlet_circle = gdspy.Round((x_outlet, y_outlet), outlet_diameter / 2)
cell.add(outlet_circle)

# Left bus from inlet circle to array
left_bus = gdspy.Rectangle(
    (x_inlet + inlet_diameter / 2, y_center - bus_width / 2),
    (x0, y_center + bus_width / 2)
)
cell.add(left_bus)

# Right bus from array to outlet circle
right_bus = gdspy.Rectangle(
    (x0 + array_width, y_center - bus_width / 2),
    (x_outlet - outlet_diameter / 2, y_center + bus_width / 2)
)
cell.add(right_bus)

# Create the DLD pillar array
for i in range(rows):
    # Calculate x-offset for the row due to shift fraction
    x_offset = (i * row_shift_fraction * pitch) % pitch
    y = y0 + i * vertical_pitch
    for j in range(pillars_in_x):
        x = x0 + x_offset + j * pitch
        # Create a pillar at (x, y)
        pillar = gdspy.Round((x, y), pillar_diameter / 2)
        # Add the pillar to the cell
        cell.add(pillar)

# Save the GDSII file
lib.write_gds('dld_chip.gds')