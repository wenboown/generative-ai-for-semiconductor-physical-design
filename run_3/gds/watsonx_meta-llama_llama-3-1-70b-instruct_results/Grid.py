import gdspy

# Parse the user's design specifications
grid_layer = 1
datatype = 4
grid_size = 5
total_width = 200
total_height = 400
x-coordinate = 100
y-coordinate = 800

# Define the library and cell for the GDS layout
lib = gdspy.GdsLibrary(prefix="GRID")
cell = lib.new_cell("GRID")

# Create each geometric element (e.g., rectangles, polygons) with precise coordinates
# Calculate number of cells in grid
num_cells_x = int(total_width / grid_size)
num_cells_y = int(total_height / grid_size)

# Loop through each cell and create a rectangle
for i in range(num_cells_x):
    for j in range(num_cells_y):
        x = x_coordinate + (i * grid_size)
        y = y_coordinate + (j * grid_size)
        rect = gdspy.Rectangle((x, y), (x + grid_size, y + grid_size), layer=grid_layer, datatype=datatype)
        cell.add(rect)

# Save the design to a GDS file
lib.write_gds("grid_layout.gds")