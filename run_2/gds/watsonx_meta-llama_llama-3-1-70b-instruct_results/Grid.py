import gdspy

# Define the grid parameters
layer = 1
datatype = 4
grid_size = 5  # in micrometers
total_width = 200  # in micrometers
total_height = 400  # in micrometers
x_offset = 100  # in nanometers
y_offset = 800  # in nanometers

# Define the grid dimensions in micrometers
grid_width = total_width / grid_size
grid_height = total_height / grid_size

# Create a new GDS library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('grid')

# Define the grid elements
for i in range(int(grid_height)):
    for j in range(int(grid_width)):
        x = x_offset + j * grid_size * 1000  # convert um to nm
        y = y_offset - i * grid_size * 1000  # convert um to nm
        rect = gdspy.Rectangle((x, y), (x + grid_size * 1000, y - grid_size * 1000), layer=layer, datatype=datatype)
        cell.add(rect)

# Save the GDS file
lib.write_gds('grid.gds')