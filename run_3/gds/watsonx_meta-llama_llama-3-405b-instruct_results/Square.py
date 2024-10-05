import gdspy

# Define the library and cell for the GDS layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell('square')

# Define the square dimensions (10 mm x 10 mm)
width = 10e-3  # Convert mm to meters (10 mm = 0.01 m)
lower_right_corner = (0, 0)

# Calculate the upper left corner coordinates
upper_left_corner = (lower_right_corner[0] - width, lower_right_corner[1] + width)

# Create the square as a rectangle with precise coordinates
square = gdspy.Rectangle(
    lower_right_corner,  # (x1, y1) coordinates
    upper_left_corner,   # (x2, y2) coordinates
    layer=0,            # Layer number (arbitrary value for example purposes)
    datatype=0          # Datatype number (arbitrary value for example purposes)
)

# Add the square to the cell
cell.add(square)

# Save the design to a GDS file
lib.write_gds('square.gds')