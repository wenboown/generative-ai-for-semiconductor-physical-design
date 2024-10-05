import gdspy

# Create a new library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('SQUARE_ARRAY')

# Define parameters (convert mm to μm)
square_size = 5000  # 5 mm
spacing = 20000  # 20 mm
rows = 10
cols = 10

# Calculate the starting position for the upper-right square to be at (0,0)
start_x = -(cols - 1) * spacing
start_y = -(rows - 1) * spacing

# Create the array of squares
for i in range(rows):
    for j in range(cols):
        # Calculate position for each square
        x = start_x + j * spacing
        y = start_y + i * spacing
        
        # Create a square at the calculated position
        square = gdspy.Rectangle((x, y), (x + square_size, y + square_size))
        
        # Add the square to the cell
        cell.add(square)

# Save the layout to a GDS file
lib.write_gds('square_array.gds')

print("GDS file 'square_array.gds' has been created.")