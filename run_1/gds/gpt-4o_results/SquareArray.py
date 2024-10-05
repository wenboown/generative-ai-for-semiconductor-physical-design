import gdspy

# Initialize the library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('SQUARE_ARRAY')

# Define parameters
square_size = 5.0  # Size of each square (5 mm by 5 mm)
spacing = 20.0     # Spacing between squares (20 mm)
cols = 10          # Number of columns
rows = 10          # Number of rows

# Loop to create squares in an array
for i in range(cols):
    for j in range(rows):
        # Calculate the position of the lower-left corner of each square
        x_offset = (cols - 1 - i) * spacing
        y_offset = (rows - 1 - j) * spacing
        
        # Create a square (rectangle) with given size and position
        square = gdspy.Rectangle(
            (x_offset, y_offset), 
            (x_offset + square_size, y_offset + square_size)
        )
        
        # Add the square to the cell
        cell.add(square)

# Save the layout to a GDSII file
lib.write_gds('square_array.gds')

print("GDSII file 'square_array.gds' has been created.")