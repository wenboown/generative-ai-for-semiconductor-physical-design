import gdspy

# Define the cell and library for the GDS layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell("square_array")

# Define the size of the square and the spacing between squares
square_size = 5  # in mm
spacing = 20  # in mm

# Calculate the total size of the array
array_size_x = (square_size + spacing) * 10 - spacing
array_size_y = (square_size + spacing) * 10 - spacing

# Calculate the coordinates of the lower left corner of the upper right square
lower_left_corner_x = -array_size_x
lower_left_corner_y = -array_size_y

# Create a loop to generate the square array
for i in range(10):
    for j in range(10):
        # Calculate the coordinates of the current square
        x = lower_left_corner_x + i * (square_size + spacing)
        y = lower_left_corner_y + j * (square_size + spacing)

        # Create a rectangle for the current square
        square = gdspy.Rectangle(x, y, x + square_size, y + square_size)

        # Add the square to the cell
        cell.add(square)

# Save the design to a GDS file
lib.write_gds("square_array.gds", cells=[cell])