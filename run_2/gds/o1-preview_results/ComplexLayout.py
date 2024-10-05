import gdspy

# Create a new GDSII library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('CELL')

# Define layers
active_layer = 1
polysilicon_layer = 2
contact_layer = 3

# Active region dimensions
active_width = 20  # µm
active_height = 5  # µm
active_spacing = 5  # µm

# Positions for the active regions
active1_x = 0
active2_x = active1_x + active_width + active_spacing  # 25 µm
active3_x = active2_x + active_width + active_spacing  # 50 µm
active_y = 0  # All active regions start at y=0

# Create active region rectangles
active1 = gdspy.Rectangle(
    (active1_x, active_y),
    (active1_x + active_width, active_y + active_height),
    layer=active_layer
)
active2 = gdspy.Rectangle(
    (active2_x, active_y),
    (active2_x + active_width, active_y + active_height),
    layer=active_layer
)
active3 = gdspy.Rectangle(
    (active3_x, active_y),
    (active3_x + active_width, active_y + active_height),
    layer=active_layer
)
cell.add([active1, active2, active3])

# Polysilicon gate grid dimensions
poly_width = 0.5  # µm

# Grid area dimensions
grid_x_min = 0
grid_x_max = 70  # Total width to cover active regions
grid_y_min = -5  # Extend below active regions
grid_y_max = 15  # Extend above active regions

# Spacing between polysilicon lines
vertical_spacing = 5  # µm
horizontal_spacing = 5  # µm

# Generate vertical polysilicon lines
vertical_lines = []
x_positions = []
x_pos = grid_x_min
while x_pos <= grid_x_max:
    line = gdspy.Rectangle(
        (x_pos - poly_width / 2, grid_y_min),
        (x_pos + poly_width / 2, grid_y_max),
        layer=polysilicon_layer
    )
    vertical_lines.append(line)
    x_positions.append(x_pos)
    x_pos += vertical_spacing
cell.add(vertical_lines)

# Generate horizontal polysilicon lines
horizontal_lines = []
y_positions = []
y_pos = grid_y_min
while y_pos <= grid_y_max:
    line = gdspy.Rectangle(
        (grid_x_min, y_pos - poly_width / 2),
        (grid_x_max, y_pos + poly_width / 2),
        layer=polysilicon_layer
    )
    horizontal_lines.append(line)
    y_positions.append(y_pos)
    y_pos += horizontal_spacing
cell.add(horizontal_lines)

# Identify positions within active regions for contact holes
y_positions_in_active = [
    y for y in y_positions if active_y <= y <= active_y + active_height
]
x_positions_in_active = []

# First active region
x_positions_in_active += [
    x for x in x_positions if active1_x <= x <= active1_x + active_width
]
# Second active region
x_positions_in_active += [
    x for x in x_positions if active2_x <= x <= active2_x + active_width
]
# Third active region
x_positions_in_active += [
    x for x in x_positions if active3_x <= x <= active3_x + active_width
]

# Create contact holes at intersections
contact_size = 1  # µm
contact_holes = []
for x in x_positions_in_active:
    for y in y_positions_in_active:
        contact = gdspy.Rectangle(
            (x - contact_size / 2, y - contact_size / 2),
            (x + contact_size / 2, y + contact_size / 2),
            layer=contact_layer
        )
        contact_holes.append(contact)
cell.add(contact_holes)

# Write the GDSII file
lib.write_gds('layout.gds')