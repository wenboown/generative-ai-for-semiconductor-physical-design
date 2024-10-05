import gdspy

# Create a new GDSII library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('DONUT')

# Parameters
center = (0, 0)
outer_radius = 10.0  # Outer radius in mm
inner_radius = 5.0   # Inner radius in mm
tolerance = 0.01     # Max distance between the true curve and the polygon edge in mm

# Create the donut shape
donut = gdspy.Round(
    center,
    outer_radius,
    inner_radius=inner_radius,
    tolerance=tolerance
)

# Add the donut to the cell
cell.add(donut)

# Save the GDSII file
lib.write_gds('donut.gds')