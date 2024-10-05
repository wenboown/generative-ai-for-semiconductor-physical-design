import gdspy

# Parameters
square_size = 5.0  # Square size in mm
spacing = 20.0     # Spacing between squares in mm (edge-to-edge)
pitch = square_size + spacing  # Total distance from one square to the next (center-to-center)

num_columns = 10
num_rows = 10

# Create a GDSII library with units in mm
lib = gdspy.GdsLibrary(unit=1e-3, precision=1e-6)  # unit=1e-3 sets the unit to 1 mm
cell = lib.new_cell('SQUARE_ARRAY')

# Loop to create the square array
for col in range(num_columns):
    for row in range(num_rows):
        x = -col * pitch
        y = -row * pitch
        # Create a rectangle for each square
        square = gdspy.Rectangle(
            (x, y),
            (x + square_size, y + square_size)
        )
        # Add the square to the cell
        cell.add(square)

# Write the GDS file
lib.write_gds('square_array.gds')