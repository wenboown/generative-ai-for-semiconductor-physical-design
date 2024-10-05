import gdspy

# Create a library and a cell for the GDS layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell('donut')

# Define the outer and inner radius of the donut
outer_radius = 10  # in mm
inner_radius = 5  # in mm

# Set the maximum distance between points to make the circle smoother
max_distance = 0.01  # in mm

# Create the outer ring of the donut
outer_ring = gdspy.Round(
    (0, 0),  # center coordinates
    outer_radius,  # radius
    inner_radius,  # inner radius
    number_of_points=int(2 * 3.14 * outer_radius / max_distance),
    layer=1,  # layer number
    datatype=0  # datatype
)

# Add the outer ring to the cell
cell.add(outer_ring)

# Save the design to a GDS file
lib.write_gds('donut.gds', unit=1.0e-6, precision=1.0e-9)