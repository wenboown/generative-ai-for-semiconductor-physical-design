import gdspy

# Create a new GDSII library with default unit (1e-6 meters = 1 micrometer)
lib = gdspy.GdsLibrary()

# Create a new cell in the library
cell = lib.new_cell('ROUNDED_SQUARE')

# Define the size of the square and the corner rounding radius
square_size = 10.0  # in mm
corner_radius = 1.0  # in mm

# Convert mm to micrometers (µm)
square_size_um = square_size * 1000.0
corner_radius_um = corner_radius * 1000.0

# Define the coordinates of the square with rounded corners
paths = [
    [corner_radius_um, 0.0],
    [square_size_um - corner_radius_um, 0.0],
    [square_size_um, corner_radius_um],
    [square_size_um, square_size_um - corner_radius_um],
    [square_size_um - corner_radius_um, square_size_um],
    [corner_radius_um, square_size_um],
    [0.0, square_size_um - corner_radius_um],
    [0.0, corner_radius_um],
]

# Create the rounded square using a polygon with bezier curves for the rounded corners
polygon = gdspy.FlexPath(
    paths,
    2 * corner_radius_um,
    corners='circular bend',
    bend_radius=corner_radius_um,
    gdsii_path=True
)

# Add the polygon to the cell
cell.add(polygon)

# Save the library to a GDS file
lib.write_gds('rounded_square.gds')

# Optionally, display the layout using gdspy's built-in viewer (for verification purposes)