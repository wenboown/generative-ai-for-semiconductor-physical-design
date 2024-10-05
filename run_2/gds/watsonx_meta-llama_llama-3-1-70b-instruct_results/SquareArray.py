import gdspy

# Define the GDS library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('square_array')

# Define the square size and spacing
square_size = (5, 5)
spacing = (20, 20)

# Calculate the number of columns and rows
num_cols = 10
num_rows = 10

# Initialize the origin (lower left corner of the upper right square)
origin = (0, 0)

# Iterate over the columns and rows
for col in range(num_cols):
    for row in range(num_rows):
        # Calculate the position of the square
        pos = (origin[0] + col * (square_size[0] + spacing[0]), 
               origin[1] + row * (square_size[1] + spacing[1]))
        
        # Create a square with the calculated position and size
        square = gdspy.Rectangle(pos, (pos[0] + square_size[0], pos[1] + square_size[1]))
        
        # Add the square to the cell
        cell.add(square)

# Save the GDS file
lib.write_gds('square_array.gds')