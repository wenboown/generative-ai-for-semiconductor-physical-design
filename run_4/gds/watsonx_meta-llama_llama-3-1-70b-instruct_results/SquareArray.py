import gdspy

# Define the library and cell for the GDS layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell("square_array")

# Define the size of the square and the spacing between squares
square_size = 5  # mm
spacing = 20  # mm

# Define the number of columns and rows
num_cols = 10
num_rows = 10

# Calculate the position of the lower left corner of each square
for i in range(num_rows):
    for j in range(num_cols):
        x = j * (square_size + spacing)
        y = -i * (square_size + spacing)
        # Create a square at the calculated position
        square = gdspy.Rectangle((x, y), (x + square_size, y - square_size))
        # Add the square to the cell
        cell.add(square)

# Save the design to a GDS file
lib.write_gds('square_array.gds')