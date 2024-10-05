import gdspy

# Define the GDS library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('square_array')

# Define the square dimensions
square_size = 5  # mm

# Define the spacing between squares
spacing = 20  # mm

# Define the number of rows and columns
num_rows = 10
num_cols = 10

# Calculate the total size of the array
total_size_x = num_cols * (square_size + spacing)
total_size_y = num_rows * (square_size + spacing)

# Create a list to store the squares
squares = []

# Generate the squares
for i in range(num_rows):
    for j in range(num_cols):
        # Calculate the lower left corner of the square
        x = j * (square_size + spacing)
        y = -i * (square_size + spacing)
        
        # Create the square
        rect = gdspy.Rectangle((x, y), (x + square_size, y + square_size))
        
        # Add the square to the list
        squares.append(rect)

# Add the squares to the cell
cell.add(*squares)

# Save the cell to a GDS file
lib.write_gds('square_array.gds')