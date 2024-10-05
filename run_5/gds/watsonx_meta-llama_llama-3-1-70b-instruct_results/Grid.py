import gdspy

# Define the GDS library and cell
lib = gdspy.Library()
cell = lib.new_cell('Grid')

# Define the grid parameters
layer = 1
datatype = 4
grid_size = 5  # in microns
width = 200  # in microns
height = 400  # in microns
x_offset = 100  # in nanometers
y_offset = 800  # in nanometers

# Calculate the number of grid lines
num_x_lines = int(width / grid_size)
num_y_lines = int(height / grid_size)

# Draw the grid lines
for i in range(num_x_lines + 1):
    x = x_offset + (i * grid_size * 1000)  # convert microns to nanometers
    path = gdspy.Path(1, [(x, y_offset), (x, y_offset + height * 1000)])
    path.datatype = datatype
    cell.add(path)

for i in range(num_y_lines + 1):
    y = y_offset + (i * grid_size * 1000)  # convert microns to nanometers
    path = gdspy.Path(1, [(x_offset, y), (x_offset + width * 1000, y)])
    path.datatype = datatype
    cell.add(path)

# Save the GDS layout to a file
lib.write_gds('grid.gds', [cell], unit=1e-9, precision=1e-9)