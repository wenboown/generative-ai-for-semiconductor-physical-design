import gdspy

# Define the library and cell for the GDS layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell('square_array')

# Define the size of the square and the spacing between them
square_size = 5  # mm
spacing = 20  # mm
num_cols = 10
num_rows = 10

# Calculate the coordinates for the lower left corner of each square
for i in range(num_rows):
    for j in range(num_cols):
        x = - (num_cols - 1) * spacing + j * spacing
        y = (num_rows - 1) * spacing - i * spacing
        # Create a square with precise coordinates
        square = gdspy.Rectangle((x, y), (x + square_size, y + square_size), layer=0, datatype=0)
        # Add the square to the cell
        cell.add(square)

# Save the design to a GDS file
lib.write_gds('square_array.gds')