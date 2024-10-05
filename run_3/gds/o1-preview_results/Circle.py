import gdspy

# Create a new GDSII library
lib = gdspy.GdsLibrary()

# Create a new cell in the library
cell = lib.new_cell('CIRCLE_CELL')

# Design parameters
radius_mm = 10            # Radius in millimeters
radius_um = radius_mm * 1000  # Convert radius to micrometers
center = (0, 0)               # Center coordinates
layer = 0                     # Layer number

# Create the circle geometry
circle = gdspy.Round(
    center,                   # Center of the circle
    radius_um,                # Radius of the circle
    number_of_points=256,     # Number of points to approximate the circle
    max_points=199,           # Maximum points per polygon (GDSII limit)
    layer=layer               # Layer specification
)

# Add the circle to the cell
cell.add(circle)

# Write the GDSII file
lib.write_gds('circle.gds')

print("GDSII file 'circle.gds' has been created successfully.")