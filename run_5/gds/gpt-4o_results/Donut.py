import gdspy

# Define library
lib = gdspy.GdsLibrary()

# Create a cell (top level structure)
cell = lib.new_cell('DONUT_CELL')

# Define parameters
outer_radius = 10.0  # Outer radius in mm
inner_radius = 5.0   # Inner radius in mm
max_points_distance = 0.01  # Maximum distance between points in mm

# Create outer circle (donut outer boundary)
outer_circle = gdspy.Round(
    (0, 0),  # Center coordinates
    outer_radius,  # Outer radius
    tolerance=max_points_distance  # Maximum distance between points on the circle
)

# Create inner circle (donut inner boundary)
inner_circle = gdspy.Round(
    (0, 0),  # Center coordinates
    inner_radius,  # Inner radius
    tolerance=max_points_distance  # Maximum distance between points on the circle
)

# Subtract inner circle from outer circle
donut = gdspy.boolean(outer_circle, inner_circle, 'not')

# Add donut to the cell
cell.add(donut)

# Save the layout to a GDS file
lib.write_gds('donut_shape.gds')

print("Donut shape GDS file has been created successfully.")