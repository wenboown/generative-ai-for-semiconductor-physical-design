import gdspy

# Define grid parameters (convert micrometers to nanometers)
grid_spacing = 5e3   # 5 µm in nanometers
grid_width = 200e3   # 200 µm in nanometers
grid_height = 400e3  # 400 µm in nanometers
start_x = 100e3       # Start X coordinate in nanometers
start_y = 800e3       # Start Y coordinate in nanometers
layer = 1
datatype = 4

# Calculate the number of horizontal and vertical lines
num_vertical_lines = int(grid_width / grid_spacing) + 1
num_horizontal_lines = int(grid_height / grid_spacing) + 1

# Create a new GDSII library and a cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('GRID_CELL')

# Draw vertical lines of the grid
for i in range(int(num_vertical_lines)):
    x_position = start_x + i * grid_spacing
    line = gdspy.Rectangle((x_position, start_y), (x_position, start_y + grid_height), layer=layer, datatype=datatype)
    cell.add(line)

# Draw horizontal lines of the grid
for j in range(int(num_horizontal_lines)):
    y_position = start_y + j * grid_spacing
    line = gdspy.Rectangle((start_x, y_position), (start_x + grid_width, y_position), layer=layer, datatype=datatype)
    cell.add(line)

# Save the library to a GDSII file
lib.write_gds('grid_design.gds')

print("GDSII file 'grid_design.gds' created successfully.")