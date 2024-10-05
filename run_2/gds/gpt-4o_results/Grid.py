import gdspy

# Create a new GDSII library named 'GridLibrary'
lib = gdspy.GdsLibrary()

# Create a new cell where the grid will be drawn
cell = lib.new_cell('GRID_CELL')

# Define grid parameters (convert micrometers to nanometers)
grid_spacing = 5e3   # 5 µm in nanometers
grid_width = 200e3   # 200 µm in nanometers
grid_height = 400e3  # 400 µm in nanometers
start_x = 100        # Start X coordinate in nanometers
start_y = 800        # Start Y coordinate in nanometers

# Calculate the number of horizontal and vertical lines
num_vertical_lines = grid_width // grid_spacing + 1
num_horizontal_lines = grid_height // grid_spacing + 1

# Draw vertical lines of the grid
for i in range(int(num_vertical_lines)):
    x_position = start_x + i * grid_spacing
    line = gdspy.Rectangle((x_position, start_y), (x_position, start_y + grid_height), layer=1, datatype=4)
    cell.add(line)

# Draw horizontal lines of the grid
for j in range(int(num_horizontal_lines)):
    y_position = start_y + j * grid_spacing
    line = gdspy.Rectangle((start_x, y_position), (start_x + grid_width, y_position), layer=1, datatype=4)
    cell.add(line)

# Save the library to a GDSII file
lib.write_gds('grid_design.gds')

print("GDSII file 'grid_design.gds' created successfully.")