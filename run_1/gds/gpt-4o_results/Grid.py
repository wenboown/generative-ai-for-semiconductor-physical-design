import gdspy

# Define grid parameters
grid_width = 5e-6  # 5 µm in meters
grid_height = 5e-6  # 5 µm in meters
total_width = 200e-6  # 200 µm in meters
total_height = 400e-6  # 400 µm in meters
origin_x = 100e-9  # 100 nm in meters
origin_y = 800e-9  # 800 nm in meters

# Create a GDSII library and a cell
gdsii_lib = gdspy.GdsLibrary()
cell = gdsii_lib.new_cell('GRID_CELL')

# Create the grid pattern
x_coords = [origin_x + i * grid_width for i in range(int(total_width // grid_width) + 1)]
y_coords = [origin_y + j * grid_height for j in range(int(total_height // grid_height) + 1)]

# Add vertical lines to the cell
for x in x_coords:
    line = gdspy.Rectangle((x, origin_y), (x, origin_y + total_height), layer=1, datatype=4)
    cell.add(line)

# Add horizontal lines to the cell
for y in y_coords:
    line = gdspy.Rectangle((origin_x, y), (origin_x + total_width, y), layer=1, datatype=4)
    cell.add(line)

# Save the GDSII file
gdsii_lib.write_gds('grid.gds')

print('GDSII file "grid.gds" created successfully.')