import gdspy

# Define the library and cell for the GDS layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell('square_array')

# Define the size of the square and the spacing
square_size = 5  # mm
spacing = 20  # mm

# Define the number of columns and rows
columns = 10
rows = 10

# Calculate the coordinates of the first square
x0 = -(columns - 1) * spacing
y0 = -(rows - 1) * spacing

# Create each square in the array
for i in range(rows):
    for j in range(columns):
        x = x0 + j * spacing
        y = y0 + i * spacing
        square = gdspy.Rectangle((x, y), (x + square_size, y + square_size))
        cell.add(square)

# Save the design to a GDS file
lib.write_gds('square_array.gds')