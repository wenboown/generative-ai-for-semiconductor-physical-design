import gdspy
import math

# Create a new GDSII library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('OVAL_CELL')

# Define the ellipse parameters
center = (0, 0)  # Center at (0,0)
major_axis = 20000  # Major axis in micrometers (20 mm)
minor_axis = 13000  # Minor axis in micrometers (13 mm)
a = major_axis / 2  # Semi-major axis (10 mm)
b = minor_axis / 2  # Semi-minor axis (6.5 mm)

# Create the ellipse (oval) using gdspy.Round
ellipse = gdspy.Round(
    center=center,
    radius=(a, b),  # (radius_x, radius_y)
    inner_radius=0,  # Solid ellipse
    initial_angle=0,
    final_angle=2 * math.pi,  # Full ellipse
    number_of_points=199,  # Number of points for ellipse approximation
    max_points=199,  # Maximum points per polygon (GDSII limit)
    layer=0  # Layer 0
)

# Add the ellipse to the cell
cell.add(ellipse)

# Save the GDS file
lib.write_gds('ellipse.gds')