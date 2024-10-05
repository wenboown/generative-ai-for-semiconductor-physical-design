import gdspy

# Parse user's design specifications
grid_size = 5  # in micrometers
total_width = 200  # in micrometers
total_height = 400  # in micrometers
layer = 1
datatype = 4
x_offset = 100  # in nanometers
y_offset = 800  # in nanometers

# Define the library and cell for the GDS layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell('grid')

# Define the grid's dimensions in nanometers
grid_size_nm = grid_size * 1000
total_width_nm = total_width * 1000
total_height_nm = total_height * 1000

# Calculate the number of grids in x and y directions
num_grids_x = int(total_width_nm / grid_size_nm)
num_grids_y = int(total_height_nm / grid_size_nm)

# Create each grid element
for i in range(num_grids_x):
    for j in range(num_grids_y):
        x = x_offset + i * grid_size_nm
        y = y_offset + j * grid_size_nm
        rect = gdspy.Rectangle((x, y), (x + grid_size_nm, y + grid_size_nm), layer=layer, datatype=datatype)
        cell.add(rect)

# Save the design to a GDS file
lib.write_gds('grid.gds')