import gdspy

# Define the units for the design (1 um = 1000 nm)
unit = 1e-6
units_per_um = 1 / unit

# Parse user's design specifications
grid_layer = 1
grid_datatype = 4
grid_size = 5 * unit
grid_width = 200 * unit
grid_height = 400 * unit
x_coord = 100 * unit
y_coord = 800 * unit

# Create the GDS library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('Grid')

# Define the grid
grid = []
x_start = x_coord
x_end = x_coord + grid_width
y_start = y_coord
y_end = y_coord + grid_height
x_step = grid_size
y_step = grid_size

# Create the horizontal grid lines
for y_pos in [y_start + i * y_step for i in range(int((y_end - y_start) / y_step) + 1)]:
    line = gdspy.Rectangle((x_start, y_pos - (grid_size/units_per_um)/2),
                           (x_end, y_pos + (grid_size/units_per_um)/2),
                           layer=grid_layer, datatype=grid_datatype)
    cell.add(line)

# Create the vertical grid lines
for x_pos in [x_start + i * x_step for i in range(int((x_end - x_start) / x_step) + 1)]:
    line = gdspy.Rectangle((x_pos - (grid_size/units_per_um)/2, y_start),
                           (x_pos + (grid_size/units_per_um)/2, y_end),
                           layer=grid_layer, datatype=grid_datatype)
    cell.add(line)

# Save the design to a GDS file
lib.write_gds("grid.gds")