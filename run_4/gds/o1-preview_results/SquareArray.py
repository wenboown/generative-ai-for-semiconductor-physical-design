import gdspy

# Define units (5 mm = 5000 μm, since GDSII commonly uses micrometers)
square_size = 5000       # 5 mm in μm
spacing = 20000          # 20 mm in μm
pitch = square_size + spacing  # Total distance between squares' origins
num_columns = 10
num_rows = 10

# Create a new library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('SQUARE_ARRAY')

# Generate the array of squares
for i in range(num_columns):
    x0 = 0 - i * pitch
    for j in range(num_rows):
        y0 = 0 - j * pitch
        rectangle = gdspy.Rectangle(
            (x0, y0),
            (x0 + square_size, y0 + square_size)
        )
        cell.add(rectangle)

# Save the GDS file
lib.write_gds('square_array.gds')