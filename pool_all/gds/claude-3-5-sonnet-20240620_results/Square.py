import gdspy

# Define the dimensions
width = 10000  # 10 mm = 10000 μm

# Create a new library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell("SQUARE")

# Create the square with lower right corner at (0,0)
square = gdspy.Rectangle((0, 0), (-width, width))

# Add the square to the cell
cell.add(square)

# Save the design to a GDS file
lib.write_gds("square_10mm.gds")

print("GDS file 'square_10mm.gds' has been created.")