import gdspy

# Define the library and cell for the GDS layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell('square_array')

# Define the size of the square and the spacing between them
square_size = 5  # in mm
spacing = 20  # in mm
num_rows = 10
num_cols = 10

# Calculate the total size of the array
total_size = (num_rows - 1) * spacing + square_size

# Create each square in the array
for i in range(num_rows):
    for j in range(num_cols):
        # Calculate the position of the square
        x = -total_size + j * spacing
        y = total_size - i * spacing - square_size
        
        # Create the square
        square = gdspy.Rectangle((x, y), (x + square_size, y + square_size))
        cell.add(square)

# Save the design to a GDS file
lib.write_gds('square_array.gds')