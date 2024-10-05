import gdspy

# Define the library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('GRID_LAYOUT')

# Define the grid specifications
grid_spacing = 5  # in micrometers, both horizontally and vertically
grid_width = 200  # in micrometers
grid_height = 400  # in micrometers
datatype = 4
layer = 1

# Define the starting coordinate (100, 800) nanometers converted to micrometers
origin = (0.1, 0.8)

# Create the grid lines and add them to the cell

# Horizontal lines
for y in range(0, grid_height + 1, grid_spacing):
    line = [(origin[0], origin[1] + y), (origin[0] + grid_width, origin[1] + y)]
    cell.add(gdspy.FlexPath(line, width=0.001, layer=layer, datatype=datatype))

# Vertical lines
for x in range(0, grid_width + 1, grid_spacing):
    line = [(origin[0] + x, origin[1]), (origin[0] + x, origin[1] + grid_height)]
    cell.add(gdspy.FlexPath(line, width=0.001, layer=layer, datatype=datatype))

# Output the GDSII file
lib.write_gds('grid_layout.gds')