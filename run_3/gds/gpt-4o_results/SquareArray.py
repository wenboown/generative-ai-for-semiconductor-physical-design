import gdspy

# Parameters
square_size = 5.0  # size of each square in mm
rows = 10  # number of rows
columns = 10  # number of columns
spacing = 20.0  # spacing between squares in mm
start_x = 0  # x coordinate of the lower left corner of the upper right square
start_y = 0  # y coordinate of the lower left corner of the upper right square

# Create a GDSII library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('SQUARE_ARRAY')

# Calculate the total size of the array
total_width = square_size + (columns - 1) * spacing
total_height = square_size + (rows - 1) * spacing

# Shift for the lower left corner of the upper right square to be at (0,0)
shift_x = -total_width
shift_y = -total_height

# Create the square array
for i in range(columns):
    for j in range(rows):
        lower_left_x = start_x + shift_x + i * spacing
        lower_left_y = start_y + shift_y + j * spacing
        square = gdspy.Rectangle((lower_left_x, lower_left_y),
                                 (lower_left_x + square_size, lower_left_y + square_size))
        cell.add(square)

# Save the layout to a GDSII file
lib.write_gds('square_array.gds')

print("GDSII file 'square_array.gds' has been generated.")