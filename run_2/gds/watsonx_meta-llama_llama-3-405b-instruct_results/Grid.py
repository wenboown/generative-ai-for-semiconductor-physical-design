import gdspy

# Define the library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('grid')

# Define the grid parameters
grid_size = 5  # in microns
total_width = 200  # in microns
total_height = 400  # in microns
layer = 1
datatype = 4
origin = (100, 800)  # in nanometers

# Convert grid size, total width, and total height to nanometers
grid_size_nm = grid_size * 1000
total_width_nm = total_width * 1000
total_height_nm = total_height * 1000

# Calculate the number of grid lines in x and y directions
num_lines_x = int(total_width_nm / grid_size_nm)
num_lines_y = int(total_height_nm / grid_size_nm)

# Create the grid
for i in range(num_lines_x + 1):
    # Create a line along the x-axis
    x = origin[0] + i * grid_size_nm
    y_min = origin[1]
    y_max = origin[1] + total_height_nm
    cell.add(gdspy.Rectangle([x, y_min], [x, y_max], layer, datatype))
    
for j in range(num_lines_y + 1):
    # Create a line along the y-axis
    x_min = origin[0]
    x_max = origin[0] + total_width_nm
    y = origin[1] + j * grid_size_nm
    cell.add(gdspy.Rectangle([x_min, y], [x_max, y], layer, datatype))

# Save the design to a GDS file
lib.write_gds('grid.gds')