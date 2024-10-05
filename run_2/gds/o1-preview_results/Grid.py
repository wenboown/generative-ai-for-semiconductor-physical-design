import gdspy

# Create a new GDSII library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('GRID_CELL')

# Layer and datatype
layer = 1
datatype = 4

# Starting position in micrometers (converted from nanometers)
start_x = 0.1   # 100 nm = 0.1 µm
start_y = 0.8   # 800 nm = 0.8 µm

# Grid dimensions
width = 200.0        # Total width in µm
height = 400.0       # Total height in µm
grid_spacing = 5.0   # Grid spacing in µm

# Line width (must be non-zero for GDSII)
line_width = 0.1  # Line width in µm

# Calculate the number of grid lines
num_vlines = int(width / grid_spacing) + 1   # Number of vertical lines
num_hlines = int(height / grid_spacing) + 1  # Number of horizontal lines

# Generate positions for vertical lines
x_positions = [start_x + i * grid_spacing for i in range(num_vlines)]
# Generate positions for horizontal lines
y_positions = [start_y + i * grid_spacing for i in range(num_hlines)]

# Create vertical grid lines
for x in x_positions:
    path = gdspy.Path(line_width, (x, start_y))
    path.segment(height, '+y', layer=layer, datatype=datatype)
    cell.add(path)

# Create horizontal grid lines
for y in y_positions:
    path = gdspy.Path(line_width, (start_x, y))
    path.segment(width, '+x', layer=layer, datatype=datatype)
    cell.add(path)

# Save the GDSII file
lib.write_gds('grid_layout.gds')