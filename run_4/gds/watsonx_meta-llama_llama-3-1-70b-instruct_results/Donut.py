import gdspy

# Define the library and cell for the GDS layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell('donut')

# Define the outer and inner radii of the donut
outer_radius = 10
inner_radius = 5

# Create the outer circle
outer_circle = gdspy.Round(
    (0, 0),  # center coordinates
    outer_radius,  # radius
    num_points=360,  # improve smoothness by increasing the number of points
    distance=0.01  # maximum distance between points
)

# Create the inner circle
inner_circle = gdspy.Round(
    (0, 0),  # center coordinates
    inner_radius,  # radius
    num_points=360,  # improve smoothness by increasing the number of points
    distance=0.01  # maximum distance between points
)

# Subtract the inner circle from the outer circle to create the donut shape
donut = gdspy.fast_boolean(
    outer_circle, 
    inner_circle, 
    'not', 
    max_points=1000, 
    precision=0.001
)

# Add the donut shape to the cell
cell.add(donut)

# Save the design to a GDS file
lib.write_gds('donut.gds')