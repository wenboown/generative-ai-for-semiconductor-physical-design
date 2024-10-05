import gdspy

# Create a new GDSII library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('DLD_DESIGN')

# Define parameters
pillar_diameter = 0.4      # in micrometers
gap_size = 0.225           # in micrometers
pitch_x = pillar_diameter + gap_size  # Horizontal pitch
pitch_y = pitch_x                     # Vertical pitch
width_in_pillars = 30
row_shift_fraction = 0.1

shift_per_row = row_shift_fraction * pitch_x

# Number of rows
num_rows = 100  # Adjust as needed

array_width = (width_in_pillars - 1) * pitch_x + pillar_diameter
array_height = (num_rows - 1) * pitch_y + pillar_diameter

# Inlet and outlet parameters
inlet_diameter = 40    # in micrometers
outlet_diameter = 40   # in micrometers
bus_width = 20         # in micrometers (vertical dimension)
bus_length = 50        # in micrometers (horizontal dimension)

# Calculate positions
inlet_center = (0, array_height / 2)
array_origin_x = bus_length + inlet_diameter / 2
array_origin_y = 0  # Starting at y = 0
outlet_center = (array_origin_x + array_width + bus_length + outlet_diameter / 2, array_height / 2)

# Add inlet circle
inlet_circle = gdspy.Round(inlet_center, inlet_diameter / 2)
cell.add(inlet_circle)

# Add inlet bus (rectangle)
inlet_bus = gdspy.Rectangle(
    (inlet_center[0] + inlet_diameter / 2, inlet_center[1] - bus_width / 2),
    (array_origin_x, inlet_center[1] + bus_width / 2)
)
cell.add(inlet_bus)

# Add outlet circle
outlet_circle = gdspy.Round(outlet_center, outlet_diameter / 2)
cell.add(outlet_circle)

# Add outlet bus (rectangle)
outlet_bus = gdspy.Rectangle(
    (array_origin_x + array_width, inlet_center[1] - bus_width / 2),
    (outlet_center[0] - outlet_diameter / 2, inlet_center[1] + bus_width / 2)
)
cell.add(outlet_bus)

# Generate pillars
max_cols = width_in_pillars + 2  # Adjusted to cover potential shifts
for row in range(num_rows):
    y = array_origin_y + row * pitch_y
    x_shift = (row * shift_per_row) % pitch_x
    for col in range(max_cols):
        x = array_origin_x + col * pitch_x + x_shift
        if array_origin_x <= x <= array_origin_x + array_width + pitch_x:
            pillar_center = (x, y)
            pillar = gdspy.Round(pillar_center, pillar_diameter / 2)
            cell.add(pillar)

# Save to GDSII file
lib.write_gds('dld_design.gds')