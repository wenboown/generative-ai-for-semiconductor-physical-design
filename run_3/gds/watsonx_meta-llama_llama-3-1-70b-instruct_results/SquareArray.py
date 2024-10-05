import gdspy

# Define the library and cell for the GDS layout
lib = gdspy.Library()
cell = lib.new_cell('square_array')

# Define the size of the square and spacing
square_size = 5  # mm
spacing = 20  # mm

# Calculate the total size of the array
array_size_x = 10 * (square_size + spacing)
array_size_y = 10 * (square_size + spacing)

# Create the square array
for i in range(10):
    for j in range(10):
        # Calculate the position of the square
        x = i * (square_size + spacing)
        y = j * (square_size + spacing)
        
        # Create the square
        sq = gdspy.Rectangle((x, y), (x + square_size, y + square_size))
        
        # Add the square to the cell
        cell.add(sq)

# Save the design to a GDS file
lib.write_gds('square_array.gds')