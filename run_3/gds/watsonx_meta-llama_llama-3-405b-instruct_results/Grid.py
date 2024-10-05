import gdspy

# User design specifications
grid_size = 5  # 5 um grid size
total_width = 200  # total width in um
total_height = 400  # total height in um
placement_x = 100  # x-coordinate in nm
placement_y = 800  # y-coordinate in nm
layer = 1  # layer number
datatype = 4  # datatype number

# Convert coordinates to nanometers
total_width_nm = total_width * 1000
total_height_nm = total_height * 1000
grid_size_nm = grid_size * 1000

# Define the library and cell for the GDS layout
gdsii = gdspy.GdsLibrary()
top_cell = gdsii.new_cell('grid')

# Create the grid elements
grid_elements = []
x_coords = [placement_x + i for i in range(0, total_width_nm, grid_size_nm)]
y_coords = [placement_y + i for i in range(0, total_height_nm, grid_size_nm)]

for x in x_coords:
    for y in y_coords:
        grid_element = gdspy.Rectangle((x, y), (x + grid_size_nm, y + grid_size_nm), layer=layer, datatype=datatype)
        grid_elements.append(grid_element)

# Add the grid elements to the top cell
top_cell.add(grid_elements)

# Save the design to a GDS file
gdsii.write_gds('grid.gds')