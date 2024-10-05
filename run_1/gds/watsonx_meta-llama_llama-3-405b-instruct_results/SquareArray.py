import gdspy

# Define the library and cell
lib = gdspy.GdsLibrary(name='Square_Array')
cell = lib.new_cell('Square_Array')

# Define the square dimensions
square_size = 5

# Define the spacing and number of columns and rows
spacing = 20
num_columns = 10
num_rows = 10

# Define the upper right square's lower left corner coordinates
x_start = 0
y_start = 0

# Calculate the coordinates for each square
for i in range(num_rows):
    for j in range(num_columns):
        x = x_start - j * (square_size + spacing)
        y = y_start - i * (square_size + spacing)
        square = gdspy.Rectangle((x, y), (x + square_size, y + square_size))
        cell.add(square)

# Save the design to a GDS file
lib.write_gds('square_array.gds')