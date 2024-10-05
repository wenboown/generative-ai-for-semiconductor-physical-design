import gdspy

# Define the square dimensions
width = 10000  # 10 mm in nanometers

# Calculate the coordinates for the square
# Lower right corner is at (0, 0)
x1, y1 = 0, 0
x2, y2 = -width, width

# Create a new library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell("SQUARE")

# Create the square using a rectangle
square = gdspy.Rectangle((x1, y1), (x2, y2))

# Add the square to the cell
cell.add(square)

# Save the design to a GDS file
lib.write_gds("square_10mm.gds")

print("GDS file 'square_10mm.gds' has been generated successfully.")