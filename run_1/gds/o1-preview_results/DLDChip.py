import gdspy

# Create a new GDSII library
lib = gdspy.GdsLibrary()

# Create the main cell
cell = lib.new_cell('DLD_Chip')

# Define units (all dimensions are in micrometers)
# GDSII unit is 1e-6 meters (micrometers)
# Define layer numbers
layer_channel = 1
layer_pillars = 2
layer_inlet_outlet = 3
layer_bus = 4

# Define DLD array parameters
D = 0.4        # Pillar diameter in micrometers
G = 0.225      # Gap size in micrometers
P = D + G      # Pillar pitch in micrometers
s = 0.1        # Row shift fraction
N_pillars_x = 30   # Number of pillars in x-direction
N_rows = 100       # Number of rows

# Calculate array dimensions
L_array_x = N_pillars_x * P  # Length of the array in x-direction
L_array_y = N_rows * P       # Length of the array in y-direction

# Define bus dimensions
bus_length = 50.0    # Bus length in micrometers
bus_width = 20.0     # Bus width in micrometers

# Define inlet and outlet dimensions
inlet_radius = 20.0   # Radius of inlet/outlet in micrometers

# Define positions
margin = 10.0                                    # Margin around the array
total_height = L_array_y + 2 * margin            # Total height of the chip
inlet_center_x = inlet_radius                    # X-coordinate of inlet center
inlet_center_y = total_height / 2                # Y-coordinate of inlet center

# Inlet circle
inlet_circle = gdspy.Round(
    (inlet_center_x, inlet_center_y),
    inlet_radius,
    number_of_points=64,
    layer=layer_inlet_outlet,
)
cell.add(inlet_circle)

# Inlet bus rectangle
x_bus_start = inlet_center_x + inlet_radius
x_bus_end = x_bus_start + bus_length
y_bus_bottom = inlet_center_y - bus_width / 2
y_bus_top = inlet_center_y + bus_width / 2
inlet_bus = gdspy.Rectangle(
    (x_bus_start, y_bus_bottom),
    (x_bus_end, y_bus_top),
    layer=layer_bus,
)
cell.add(inlet_bus)

# Channel rectangle
x_channel_start = x_bus_end
x_channel_end = x_channel_start + L_array_x
y_channel_bottom = inlet_center_y - L_array_y / 2
y_channel_top = inlet_center_y + L_array_y / 2
channel = gdspy.Rectangle(
    (x_channel_start, y_channel_bottom),
    (x_channel_end, y_channel_top),
    layer=layer_channel,
)
cell.add(channel)

# Outlet bus rectangle
x_bus2_start = x_channel_end
x_bus2_end = x_bus2_start + bus_length
outlet_bus = gdspy.Rectangle(
    (x_bus2_start, y_bus_bottom),
    (x_bus2_end, y_bus_top),
    layer=layer_bus,
)
cell.add(outlet_bus)

# Outlet circle
outlet_center_x = x_bus2_end + inlet_radius
outlet_center_y = inlet_center_y
outlet_circle = gdspy.Round(
    (outlet_center_x, outlet_center_y),
    inlet_radius,
    number_of_points=64,
    layer=layer_inlet_outlet,
)
cell.add(outlet_circle)

# Generate DLD pillar array
for i in range(N_rows):
    row_shift = (i * s * P) % P  # Shift in x-direction for row i
    for j in range(N_pillars_x):
        x_pillar = x_channel_start + (j * P + row_shift) % L_array_x + D / 2
        y_pillar = y_channel_bottom + i * P + D / 2
        # Create pillar
        pillar = gdspy.Round(
            (x_pillar, y_pillar),
            D / 2,
            number_of_points=16,
            layer=layer_pillars,
        )
        cell.add(pillar)

# Save the GDS file
lib.write_gds('dld_chip.gds')