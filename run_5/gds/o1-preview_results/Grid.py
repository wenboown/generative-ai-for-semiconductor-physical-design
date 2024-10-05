import gdspy

# Create a new GDSII library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('GRID_CELL')

# Grid parameters
layer = 1  # Layer number
datatype = 4  # Datatype

# Grid dimensions in nanometers
grid_spacing = 5000  # 5 µm in nanometers
line_width = 100  # Line width in nanometers

grid_width = 200000  # 200 µm in nanometers
grid_height = 400000  # 400 µm in nanometers

# Starting position (offset) in nanometers
offset_x = 100  # nanometers
offset_y = 800  # nanometers

# Calculate number of grid lines
num_vertical_lines = int(grid_width / grid_spacing) + 1  # Including endpoints
num_horizontal_lines = int(grid_height / grid_spacing) + 1  # Including endpoints

# Create vertical grid lines
for i in range(num_vertical_lines):
    x = i * grid_spacing + offset_x
    x1 = x - line_width / 2
    x2 = x + line_width / 2
    y1 = offset_y
    y2 = offset_y + grid_height
    rectangle = gdspy.Rectangle((x1, y1), (x2, y2), layer=layer, datatype=datatype)
    cell.add(rectangle)

# Create horizontal grid lines
for j in range(num_horizontal_lines):
    y = j * grid_spacing + offset_y
    y1 = y - line_width / 2
    y2 = y + line_width / 2
    x1 = offset_x
    x2 = offset_x + grid_width
    rectangle = gdspy.Rectangle((x1, y1), (x2, y2), layer=layer, datatype=datatype)
    cell.add(rectangle)

# Save the GDSII file
lib.write_gds('grid_layout.gds')