import gdspy

# Create a new library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('SQUARE_ARRAY')

# Define the square size and spacing
square_size = 5000  # 5 mm in nanometers
spacing = 20000  # 20 mm in nanometers

# Create the array of squares
for i in range(10):
    for j in range(10):
        # Calculate the position of each square
        x = -i * spacing + 2500  # Start from 2.5 mm (half of square size)
        y = -j * spacing + 2500  # Start from 2.5 mm (half of square size)
        
        # Create a square at the calculated position
        square = gdspy.Rectangle((x - square_size/2, y - square_size/2),
                                 (x + square_size/2, y + square_size/2))
        
        # Add the square to the cell
        cell.add(square)

# Save the layout to a GDS file
lib.write_gds('square_array.gds')

# Optionally, view the layout