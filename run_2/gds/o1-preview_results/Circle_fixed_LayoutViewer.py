import gdspy

# Create a new GDSII library
lib = gdspy.GdsLibrary()

# Define the cell where the circle will be placed
cell = lib.new_cell('CIRCLE_CELL')

# Design parameters
radius_mm = 10  # Radius in millimeters
radius_um = radius_mm * 1000  # Convert radius to micrometers (1 mm = 1000 µm)
center_coordinates = (0, 0)  # Center at (0, 0)
number_of_points = 128  # Number of points to approximate the circle
layer_number = 0  # Layer 0

# Create the circle
circle = gdspy.Round(
    center=center_coordinates,
    radius=radius_um,
    number_of_points=number_of_points,
    layer=layer_number
)

# Add the circle to the cell
cell.add(circle)

# Save the GDSII file
lib.write_gds('circle.gds')

# Optional: View the layout using gdspy's built-in viewer (uncomment the next line to use)