import gdspy

# Create a new library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('GRID')

# Define grid parameters
layer = 1
datatype = 4
grid_spacing = 5000  # 5 µm in nanometers
width = 200000  # 200 µm in nanometers
height = 400000  # 400 µm in nanometers
origin = (100, 800)  # Starting coordinates in nanometers

# Calculate number of lines
num_horizontal_lines = height // grid_spacing + 1
num_vertical_lines = width // grid_spacing + 1

# Create horizontal lines
for i in range(num_horizontal_lines):
    y = origin[1] + i * grid_spacing
    path = gdspy.Path(1, (origin[0], y))
    path.segment(width, '+x', layer=layer, datatype=datatype)
    cell.add(path)

# Create vertical lines
for i in range(num_vertical_lines):
    x = origin[0] + i * grid_spacing
    path = gdspy.Path(1, (x, origin[1]))
    path.segment(height, '+y', layer=layer, datatype=datatype)
    cell.add(path)

# Save the layout to a GDSII file
lib.write_gds('grid_layout.gds')

# Optional: View the layout