import gdspy

# Create a new library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('GRID')

# Define grid parameters
layer = 1
datatype = 4
grid_spacing = 5000  # 5 µm in nm
width = 200000  # 200 µm in nm
height = 400000  # 400 µm in nm
origin = (100, 800)  # Origin coordinates in nm

# Calculate number of lines
num_horizontal_lines = int(height / grid_spacing) + 1
num_vertical_lines = int(width / grid_spacing) + 1

# Create horizontal lines
for i in range(num_horizontal_lines):
    y = origin[1] + i * grid_spacing
    horizontal_line = gdspy.Path(1, (origin[0], y))
    horizontal_line.segment(width, '+x')
    cell.add(horizontal_line)

# Create vertical lines
for i in range(num_vertical_lines):
    x = origin[0] + i * grid_spacing
    vertical_line = gdspy.Path(1, (x, origin[1]))
    vertical_line.segment(height, '+y')
    cell.add(vertical_line)

# Create a boundary rectangle
boundary = gdspy.Rectangle(origin, (origin[0] + width, origin[1] + height), layer=layer, datatype=datatype)
cell.add(boundary)

# Save the layout to a GDSII file
lib.write_gds('grid_layout.gds')

# Display the layout (optional, for visualization purposes)