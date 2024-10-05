import gdspy

# Create a GDSII library
lib = gdspy.GdsLibrary()

# Create a cell for the design
cell = lib.new_cell('SQUARE_ARRAY')

# Define square size and pitch in micrometers (um)
square_size = 5000    # 5 mm = 5000 um
spacing = 20000       # 20 mm = 20000 um
pitch = square_size + spacing  # Total distance between square origins

# Generate the array of squares
for i in range(10):  # 10 columns
    x = -i * pitch
    for j in range(10):  # 10 rows
        y = -j * pitch
        # Create a square at the calculated position
        square = gdspy.Rectangle(
            (x, y),
            (x + square_size, y + square_size)
        )
        # Add the square to the cell
        cell.add(square)

# Save the layout to a GDS file
lib.write_gds('square_array.gds')