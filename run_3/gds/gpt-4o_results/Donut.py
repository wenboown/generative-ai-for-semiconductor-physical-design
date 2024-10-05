import gdspy

# Create a new GDSII library
lib = gdspy.GdsLibrary()

# Define a cell where the layout will be created
cell = lib.new_cell("DONUT_SHAPE")

# Define parameters for the donut shape
outer_radius = 10.0  # mm
inner_radius = 5.0   # mm
max_points_distance = 0.01  # mm

# Create the outer circle
outer_circle = gdspy.Round(
    center=(0, 0),
    radius=outer_radius,
    number_of_points=max(3, int(2 * 3.14159 * outer_radius / max_points_distance))
)

# Create the inner circle (to be subtracted)
inner_circle = gdspy.Round(
    center=(0, 0),
    radius=inner_radius,
    number_of_points=max(3, int(2 * 3.14159 * inner_radius / max_points_distance))
)

# Create the donut shape by subtracting the inner circle from the outer circle
donut = gdspy.boolean(outer_circle, inner_circle, 'not')

# Add the donut shape to the cell
cell.add(donut)

# Save the layout to a GDS file
lib.write_gds('donut_shape.gds')

print("GDS file 'donut_shape.gds' has been created.")