import gdspy

# Create a new GDSII library
lib = gdspy.GdsLibrary()

# Create a new cell in the library
cell = lib.new_cell('SQUARE_ARRAY')

# Define the size of each square (5 mm x 5 mm) in microns
square_size = 5000  # 5000 microns = 5 mm

# Define the spacing between squares (center-to-center distance)
spacing = 20000  # 20000 microns = 20 mm

# Number of rows and columns
num_rows = 10
num_cols = 10

# Generate the array of squares
for row in range(num_rows):
    for col in range(num_cols):
        # Calculate the position of the lower left corner of each square
        x0 = -col * spacing
        y0 = -row * spacing
        # Create a square (rectangle) at the calculated position
        square = gdspy.Rectangle(
            (x0, y0),
            (x0 + square_size, y0 + square_size)
        )
        # Add the square to the cell
        cell.add(square)

# Save the library to a GDSII file
lib.write_gds('square_array.gds')