import gdspy

# Create a new GDSII library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('SQUARE_ARRAY')

# Dimensions in microns (1 mm = 1000 microns)
square_size = 5000   # 5 mm * 1000
spacing = 20000      # 20 mm * 1000
num_columns = 10
num_rows = 10

for i in range(num_columns):
    x = -i * spacing
    for j in range(num_rows):
        y = -j * spacing
        # Define the rectangle coordinates
        rect = gdspy.Rectangle(
            (x, y),
            (x + square_size, y + square_size)
        )
        # Add the rectangle to the cell
        cell.add(rect)

# Write the GDS file
lib.write_gds('square_array.gds')