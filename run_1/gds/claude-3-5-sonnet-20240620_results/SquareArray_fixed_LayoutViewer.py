import gdspy

# Create a new library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('SQUARE_ARRAY')

# Define square size and spacing
square_size = 5000  # 5 mm in um
spacing = 20000  # 20 mm in um

# Calculate the total size of the array
array_size = (10 - 1) * spacing  # 9 spaces between 10 squares

# Create the square shape
square = gdspy.Rectangle((-square_size/2, -square_size/2), (square_size/2, square_size/2))

# Create the array of squares
for i in range(10):
    for j in range(10):
        # Calculate position for each square
        x = -i * spacing
        y = -j * spacing
        
        # Create a copy of the square at the calculated position
        square_copy = gdspy.copy(square, x, y)
        
        # Add the square to the cell
        cell.add(square_copy)

# Save the design to a GDS file
lib.write_gds('square_array.gds')

# Optional: View the layout