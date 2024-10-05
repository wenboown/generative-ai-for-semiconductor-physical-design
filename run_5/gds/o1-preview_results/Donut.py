import gdspy

# Create a new GDSII library
lib = gdspy.GdsLibrary()

# Create a new cell in the library
cell = lib.new_cell('DONUT_SHAPE')

# Define the center coordinates of the donut
center = (0, 0)

# Define the outer and inner radii of the donut (in mm)
outer_radius = 10.0  # Outer radius of the donut
inner_radius = 5.0   # Inner radius of the donut

# Set the tolerance to achieve smoother curves
tolerance = 0.01  # Maximum distance between points (in mm)

# Create the donut shape (an annulus) with specified parameters
donut = gdspy.Round(
    center,
    outer_radius,
    inner_radius=inner_radius,
    tolerance=tolerance
)

# Add the donut shape to the cell
cell.add(donut)

# Save the library to a GDS file
lib.write_gds('donut_shape.gds')