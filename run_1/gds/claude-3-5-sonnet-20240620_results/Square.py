import gdspy

# Create a new library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('Square')

# Define square dimensions (in µm)
width = 10000  # 10 mm = 10,000 µm

# Calculate coordinates for the square
# Lower right corner at (0, 0)
x1, y1 = 0, 0
x2, y2 = -width, width

# Create the square
square = gdspy.Rectangle((x1, y1), (x2, y2))

# Add the square to the cell
cell.add(square)

# Save the design to a GDS file
lib.write_gds('square_10mm.gds')

print("GDS file 'square_10mm.gds' has been generated.")