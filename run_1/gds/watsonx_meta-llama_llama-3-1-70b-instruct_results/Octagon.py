import gdspy

# Parse the user's design specifications
edge_length = 10  # mm
center_x, center_y = 0, 0  # mm

# Define the library and cell for the GDS layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell('Octagon')

# Create an octagon shape
octagon = gdspy.Polygon(
    [
        (center_x + edge_length * 0.707106781, center_y + edge_length * 0.707106781),
        (center_x + edge_length, center_y),
        (center_x + edge_length * 0.707106781, center_y - edge_length * 0.707106781),
        (center_x, center_y - edge_length),
        (center_x - edge_length * 0.707106781, center_y - edge_length * 0.707106781),
        (center_x - edge_length, center_y),
        (center_x - edge_length * 0.707106781, center_y + edge_length * 0.707106781),
        (center_x, center_y + edge_length),
    ],
    layer=1,
    datatype=0,
)

# Add the octagon shape to the cell
cell.add(octagon)

# Save the design to a GDS file
lib.write_gds('octagon.gds')