import gdspy

# Create a new library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('GRID')

# Define grid parameters
layer = 1
datatype = 4
grid_size = 5000  # 5 µm in nanometers
total_width = 200000  # 200 µm in nanometers
total_height = 400000  # 400 µm in nanometers
origin_x = 100  # nm
origin_y = 800  # nm

# Create horizontal lines
for y in range(0, total_height + grid_size, grid_size):
    path = gdspy.Path(1, (origin_x, origin_y + y))
    path.segment(total_width, '+x', layer=layer, datatype=datatype)
    cell.add(path)

# Create vertical lines
for x in range(0, total_width + grid_size, grid_size):
    path = gdspy.Path(1, (origin_x + x, origin_y))
    path.segment(total_height, '+y', layer=layer, datatype=datatype)
    cell.add(path)

# Save the layout to a GDSII file
lib.write_gds('grid_layout.gds')

# Optional: View the layout