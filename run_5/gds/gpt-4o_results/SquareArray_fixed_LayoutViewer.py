import gdspy

# Creating a new GDSII library
lib = gdspy.GdsLibrary()

# Adding a new cell to the library
cell = lib.new_cell('SQUARE_ARRAY')

# Size of each square
square_size = 5.0

# Distance between the edges of adjacent squares
spacing = 20.0

# Number of columns and rows
num_columns = 10
num_rows = 10

# Loop through each position in the array to create the squares
for i in range(num_columns):
    for j in range(num_rows):
        # Calculate the coordinates of the lower-left corner of each square
        x = -i * (square_size + spacing)
        y = j * (square_size + spacing)
        # Create the square
        square = gdspy.Rectangle((x, y), (x + square_size, y + square_size))
        # Add the square to the cell
        cell.add(square)

# Save the layout to a GDSII file
lib.write_gds('square_array.gds')

# Optionally, you can view the layout using gdspy internal viewer, if needed