import gdspy

# Define the grid specifications
grid_layer = 1
grid_datatype = 4
grid_size = 5  # in micrometers
grid_width = 200  # in micrometers
grid_height = 400  # in micrometers
grid_x = 100  # in nanometers
grid_y = 800  # in nanometers

# Create a new GDS library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell("Grid")

# Convert micrometers to nanometers (GDS unit)
grid_size_nm = grid_size * 1000
grid_width_nm = grid_width * 1000
grid_height_nm = grid_height * 1000

# Calculate the number of grid cells
num_cells_x = int(grid_width_nm / grid_size_nm)
num_cells_y = int(grid_height_nm / grid_size_nm)

# Draw the grid
for i in range(num_cells_x + 1):
    x = grid_x + i * grid_size_nm
    cell.add(gdspy.Rectangle((x, grid_y), (x, grid_y + grid_height_nm), layer=grid_layer, datatype=grid_datatype))

for i in range(num_cells_y + 1):
    y = grid_y + i * grid_size_nm
    cell.add(gdspy.Rectangle((grid_x, y), (grid_x + grid_width_nm, y), layer=grid_layer, datatype=grid_datatype))

# Save the design to a GDS file
lib.write_gds("grid.gds")