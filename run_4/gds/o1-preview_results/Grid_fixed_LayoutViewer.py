import gdspy

# Create a GDSII library
lib = gdspy.GdsLibrary()

# Create a cell to contain the grid
cell = lib.new_cell('GRID_CELL')

# Grid parameters
layer = 1           # Layer number
datatype = 4        # Datatype
grid_spacing = 5.0  # Grid spacing in micrometers
width = 200.0       # Total width in micrometers
height = 400.0      # Total height in micrometers
origin_x = 0.1      # Origin x-position in micrometers (100 nm)
origin_y = 0.8      # Origin y-position in micrometers (800 nm)

# Number of grid lines along x and y (including both ends)
num_lines_x = int(width / grid_spacing) + 1
num_lines_y = int(height / grid_spacing) + 1

# Line width to make lines visible in GDSII
line_width = 0.1  # Line width in micrometers

# Generate vertical grid lines
for i in range(num_lines_x):
    x = i * grid_spacing + origin_x
    x1 = x - line_width / 2
    x2 = x + line_width / 2
    y1 = origin_y
    y2 = origin_y + height
    vertical_line = gdspy.Rectangle(
        (x1, y1),
        (x2, y2),
        layer=layer,
        datatype=datatype
    )
    cell.add(vertical_line)

# Generate horizontal grid lines
for j in range(num_lines_y):
    y = j * grid_spacing + origin_y
    y1 = y - line_width / 2
    y2 = y + line_width / 2
    x1 = origin_x
    x2 = origin_x + width
    horizontal_line = gdspy.Rectangle(
        (x1, y1),
        (x2, y2),
        layer=layer,
        datatype=datatype
    )
    cell.add(horizontal_line)

# Save the GDSII file
lib.write_gds('grid_layout.gds')

# Optional: View the layout using the built-in viewer (requires matplotlib)