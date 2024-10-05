import gdspy

# Define the dimensions
width = 10000  # 10 mm = 10000 µm

# Create a new library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell("SQUARE")

# Create the square
# The lower right corner is at (0, 0)
# So the other corners will be:
# Lower left: (-width, 0)
# Upper left: (-width, width)
# Upper right: (0, width)
square = gdspy.Rectangle((-width, 0), (0, width))

# Add the square to the cell
cell.add(square)

# Save the design to a GDS file
lib.write_gds("square_10mm.gds")

print("GDS file 'square_10mm.gds' has been created.")