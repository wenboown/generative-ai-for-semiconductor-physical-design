import gdspy

# Define the library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('square')

# Define the square's dimensions
size = 10  # mm
radius = 1  # mm

# Create the square with rounded corners
square = gdspy.Round(
    (0, 0),
    size,
    size,
    inner_radius=radius,
    layer=0,
    datatype=0
)

# Add the square to the cell
cell.add(square)

# Save the design to a GDS file
lib.write_gds('square.gds')

# Print a message to indicate success
print("GDS layout design created and saved successfully.")