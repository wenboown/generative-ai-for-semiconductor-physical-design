import gdspy

# Define the GDS library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell("Grid")

# Define the grid parameters
layer = 1
datatype = 4
grid_size = 5  # in microns
grid_width = 200  # in microns
grid_height = 400  # in microns
x_offset = 100  # in nanometers
y_offset = 800  # in nanometers

# Convert micron values to nanometers
grid_size_nm = grid_size * 1000
grid_width_nm = grid_width * 1000
grid_height_nm = grid_height * 1000

# Calculate the number of grid cells in x and y directions
num_x_cells = int(grid_width_nm / grid_size_nm)
num_y_cells = int(grid_height_nm / grid_size_nm)

# Draw the grid
for i in range(num_x_cells + 1):
    x = x_offset + i * grid_size_nm
    cell.add(gdspy.Rectangle((x, y_offset), (x, y_offset + grid_height_nm), layer=layer, datatype=datatype))

for j in range(num_y_cells + 1):
    y = y_offset + j * grid_size_nm
    cell.add(gdspy.Rectangle((x_offset, y), (x_offset + grid_width_nm, y), layer=layer, datatype=datatype))

# Save the GDS layout
lib.write_gds("grid.gds")