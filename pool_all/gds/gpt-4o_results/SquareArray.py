import gdspy

# Create a new GDSII library
lib = gdspy.GdsLibrary()

# Create a cell for the design
cell = lib.new_cell('SQUARE_ARRAY')

# Define the dimensions and spacing of the squares
square_size = 5000  # 5 mm in micrometers
spacing = 20000  # 20 mm in micrometers

# Number of rows and columns
rows = 10
columns = 10

# Iterate over the number of rows and columns to create the array of squares
for row in range(rows):
    for col in range(columns):
        # Calculate the position of the lower left corner of each square
        x_position = -(columns - 1 - col) * spacing
        y_position = (rows - 1 - row) * spacing
        # Create the square as a rectangle
        square = gdspy.Rectangle((x_position, y_position),
                                 (x_position + square_size, y_position + square_size))
        # Add the square to the cell
        cell.add(square)

# Save the layout to a GDS file
lib.write_gds('square_array.gds')