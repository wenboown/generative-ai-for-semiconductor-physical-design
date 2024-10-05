import gdspy

# Define parameters
layer = 1
datatype = 4
grid_size = 5 * 1000  # Convert 5 µm to nanometers
total_width = 200 * 1000  # Convert 200 µm to nanometers
total_height = 400 * 1000  # Convert 400 µm to nanometers
origin_x = 100  # in nanometers
origin_y = 800  # in nanometers

# Create GDSII library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('GRID_CELL')

# Vertical lines
for i in range(0, total_width + grid_size, grid_size):
    path = gdspy.Path(1, (origin_x + i, origin_y))
    path.segment(total_height, '+y', layer=layer, datatype=datatype)
    cell.add(path)

# Horizontal lines
for j in range(0, total_height + grid_size, grid_size):
    path = gdspy.Path(1, (origin_x, origin_y + j))
    path.segment(total_width, '+x', layer=layer, datatype=datatype)
    cell.add(path)

# Output GDSII file
lib.write_gds('grid_design.gds')