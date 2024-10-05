import gdspy

# Create a new GDSII library
lib = gdspy.GdsLibrary()

# Create a new cell in the library
cell = lib.new_cell('GRID_CELL')

# User specifications
layer = 1  # Layer number
datatype = 4  # Datatype
grid_spacing = 5e3  # 5 µm in nanometers
total_width = 200e3  # Total width of 200 µm in nanometers
total_height = 400e3  # Total height of 400 µm in nanometers
origin_x, origin_y = 100, 800  # Origin coordinates in nanometers

# Calculate the number of grid lines
num_vertical_lines = int(total_width / grid_spacing) + 1
num_horizontal_lines = int(total_height / grid_spacing) + 1

# Define a small thickness for the grid lines (e.g., 10 nm)
line_thickness = 10  # Line thickness in nanometers

# Generate vertical grid lines
for i in range(num_vertical_lines):
    x = origin_x + i * grid_spacing
    # Define the rectangle representing the vertical line
    rect = gdspy.Rectangle(
        (x - line_thickness / 2, origin_y),
        (x + line_thickness / 2, origin_y + total_height),
        layer=layer,
        datatype=datatype
    )
    cell.add(rect)

# Generate horizontal grid lines
for j in range(num_horizontal_lines):
    y = origin_y + j * grid_spacing
    # Define the rectangle representing the horizontal line
    rect = gdspy.Rectangle(
        (origin_x, y - line_thickness / 2),
        (origin_x + total_width, y + line_thickness / 2),
        layer=layer,
        datatype=datatype
    )
    cell.add(rect)

# Save the GDSII file
lib.write_gds('grid.gds')