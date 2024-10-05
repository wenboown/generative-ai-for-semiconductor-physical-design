import gdspy

# Create a new GDSII library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('DONUT')

# Parameters for the donut
outer_radius = 10.0  # mm
inner_radius = 5.0   # mm
tolerance = 0.01     # mm  # Maximum distance between points

# Create the donut shape using two circles
donut = gdspy.Round(
    (0, 0),
    outer_radius,
    inner_radius=inner_radius,
    tolerance=tolerance
)

# Add the donut to the cell
cell.add(donut)

# Save the GDSII file
lib.write_gds('donut.gds')