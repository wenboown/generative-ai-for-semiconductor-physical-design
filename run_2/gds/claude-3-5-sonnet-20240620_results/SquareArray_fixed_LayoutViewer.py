import gdspy

# Create a new library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('SQUARE_ARRAY')

# Define square size and spacing
square_size = 5  # 5 mm
spacing = 20  # 20 mm

# Calculate starting position
start_x = -180  # 0 - (9 * 20)
start_y = -180  # 0 - (9 * 20)

# Create the array of squares
for row in range(10):
    for col in range(10):
        # Calculate position for each square
        x = start_x + (col * spacing)
        y = start_y + (row * spacing)
        
        # Create a square
        square = gdspy.Rectangle((x, y), (x + square_size, y + square_size))
        
        # Add the square to the cell
        cell.add(square)

# Save the design to a GDS file
lib.write_gds('square_array.gds')

# Optional: View the layout