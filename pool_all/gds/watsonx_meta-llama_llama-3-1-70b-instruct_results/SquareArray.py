import gdspy

# Define the library and cell for the GDS layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell('square_array')

# Define the size of the square and the spacing between them
square_size = 5  # mm
spacing = 20  # mm
num_cols = 10
num_rows = 10

# Create the square array
for i in range(num_rows):
    for j in range(num_cols):
        x = - (num_cols - 1) * spacing + j * spacing
        y = (num_rows - 1) * spacing - i * spacing
        square = gdspy.Rectangle((x, y), (x + square_size, y + square_size))
        cell.add(square)

# Save the design to a GDS file
lib.write_gds('square_array.gds')