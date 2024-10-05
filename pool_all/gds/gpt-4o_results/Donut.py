import gdspy

# Define the library and cell for the GDS layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell('DONUT_SHAPE')

# Define the parameters
outer_radius = 10.0  # mm
inner_radius = 5.0   # mm
max_distance = 0.01  # mm

# Create the outer and inner circles with calculated smoothness
outer_circle = gdspy.Round(
    (0, 0), 
    outer_radius, 
    tolerance=max_distance
)

inner_circle = gdspy.Round(
    (0, 0), 
    inner_radius, 
    tolerance=max_distance
)

# Create the donut shape by subtracting the inner circle from the outer circle
donut = gdspy.boolean(outer_circle, inner_circle, 'not')

# Add the donut shape to the cell
cell.add(donut)

# Save the design to a GDS file
lib.write_gds('donut_shape.gds')

print("Donut shape GDS file has been created successfully.")