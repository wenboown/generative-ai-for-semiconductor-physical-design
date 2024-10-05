import gdspy

# Define the library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('GRID_CELL')

# Define the grid parameters
layer = 1
datatype = 4
grid_size = 5  # in micrometers
grid_width = 200  # in micrometers
grid_height = 400  # in micrometers
x_offset = 100  # in nanometers
y_offset = 800  # in nanometers

# Convert dimensions from micrometers to nanometers
grid_size_nm = grid_size * 1000
grid_width_nm = grid_width * 1000
grid_height_nm = grid_height * 1000

# Calculate the number of grid lines
num_vertical_lines = grid_width_nm // grid_size_nm + 1
num_horizontal_lines = grid_height_nm // grid_size_nm + 1

# Draw vertical lines
for i in range(int(num_vertical_lines)):
    x_position = x_offset + i * grid_size_nm
    line = gdspy.Rectangle((x_position, y_offset), (x_position, y_offset + grid_height_nm), layer=layer, datatype=datatype)
    cell.add(line)

# Draw horizontal lines
for j in range(int(num_horizontal_lines)):
    y_position = y_offset + j * grid_size_nm
    line = gdspy.Rectangle((x_offset, y_position), (x_offset + grid_width_nm, y_position), layer=layer, datatype=datatype)
    cell.add(line)

# Save the library to a GDSII file
lib.write_gds('grid_design.gds')

print("GDSII file 'grid_design.gds' created successfully.")