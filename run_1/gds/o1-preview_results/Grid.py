import gdspy

# Create a new GDSII library
lib = gdspy.GdsLibrary()

# Create a new cell in the library
cell = lib.new_cell('GRID_CELL')

# Design specifications
x0 = 0.1  # Starting x-coordinate in micrometers (100 nanometers)
y0 = 0.8  # Starting y-coordinate in micrometers (800 nanometers)
total_width = 200.0  # Total width of the grid in micrometers
total_height = 400.0  # Total height of the grid in micrometers
grid_spacing = 5.0  # Grid spacing in micrometers
line_width = 0.1  # Line width in micrometers

# Layer and datatype specifications
layer = 1
datatype = 4

# Calculate the number of vertical and horizontal grid lines
num_vertical_lines = int(total_width / grid_spacing) + 1
num_horizontal_lines = int(total_height / grid_spacing) + 1

# Generate vertical grid lines
for i in range(num_vertical_lines):
    x = x0 + i * grid_spacing
    x_left = x - line_width / 2
    x_right = x + line_width / 2
    y_bottom = y0
    y_top = y0 + total_height
    rectangle = gdspy.Rectangle(
        (x_left, y_bottom),
        (x_right, y_top),
        layer=layer,
        datatype=datatype
    )
    cell.add(rectangle)

# Generate horizontal grid lines
for j in range(num_horizontal_lines):
    y = y0 + j * grid_spacing
    y_bottom = y - line_width / 2
    y_top = y + line_width / 2
    x_left = x0
    x_right = x0 + total_width
    rectangle = gdspy.Rectangle(
        (x_left, y_bottom),
        (x_right, y_top),
        layer=layer,
        datatype=datatype
    )
    cell.add(rectangle)

# Write the GDSII file
lib.write_gds('grid_layout.gds')