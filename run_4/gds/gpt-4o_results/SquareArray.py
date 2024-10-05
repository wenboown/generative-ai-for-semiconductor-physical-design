import gdspy

# Create a new GDSII library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('ARRAY')

# Square dimensions
square_size = 5.0  # in mm
spacing = 20.0  # in mm
columns = 10
rows = 10

# Coordinates for the lower left corner of the upper right square
reference_x = 0.0
reference_y = 0.0

# Calculate the starting point for the entire array
start_x = reference_x - (columns - 1) * spacing
start_y = reference_y + (rows - 1) * spacing

# Create the array of squares
for row in range(rows):
    for col in range(columns):
        x_offset = start_x + col * spacing
        y_offset = start_y - row * spacing
        square = gdspy.Rectangle(
            (x_offset, y_offset),
            (x_offset + square_size, y_offset - square_size)
        )
        cell.add(square)

# Write the GDSII file to disk
lib.write_gds('square_array.gds')

print("GDS file 'square_array.gds' has been created.")