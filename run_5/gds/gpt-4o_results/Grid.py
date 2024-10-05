import gdspy

# Design specifications
layer = 1
datatype = 4
grid_size = 5  # in micrometers
width = 200  # in micrometers
height = 400  # in micrometers
origin_x = 0.1  # in micrometers (100 nanometers)
origin_y = 0.8  # in micrometers (800 nanometers)

# Create the GDSII library
lib = gdspy.GdsLibrary()

# Create a cell (container for shapes)
cell = lib.new_cell('GRID_CELL')

# Convert dimensions from micrometers to nanometers for internal consistency
grid_size_nm = grid_size * 1000
width_nm = width * 1000
height_nm = height * 1000

# Calculate the number of grid lines to draw
num_vertical_lines = int(width / grid_size)
num_horizontal_lines = int(height / grid_size)

# Draw vertical grid lines
for i in range(num_vertical_lines + 1):
    x = origin_x * 1000 + i * grid_size_nm
    line = gdspy.Path(1, (x, origin_y * 1000))
    line.segment(height_nm, '+y', layer=layer, datatype=datatype)
    cell.add(line)

# Draw horizontal grid lines
for i in range(num_horizontal_lines + 1):
    y = origin_y * 1000 + i * grid_size_nm
    line = gdspy.Path(1, (origin_x * 1000, y))
    line.segment(width_nm, '+x', layer=layer, datatype=datatype)
    cell.add(line)

# Save the design to a GDS file
gdspy.write_gds('grid_design.gds', cells=[cell])