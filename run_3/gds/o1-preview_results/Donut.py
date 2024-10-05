import gdspy

# Create a new GDSII library
lib = gdspy.GdsLibrary()

# Define units (1 unit = 1 mm) and precision
unit = 1.0e-3  # 1 mm units
precision = 1.0e-9  # Precision of 1 nm

# Create a new cell for the donut shape
cell = lib.new_cell('DONUT')

# Center coordinates of the donut
center = (0, 0)

# Define inner and outer radii in mm
inner_radius = 5.0  # Inner radius of 5 mm
outer_radius = 10.0  # Outer radius of 10 mm

# Maximum allowed distance between points along the circle in mm
max_distance = 0.01  # 0.01 mm

# Calculate the circumference of the outer and inner circles
import math
outer_circumference = 2 * math.pi * outer_radius
inner_circumference = 2 * math.pi * inner_radius

# Calculate the required number of points for the outer and inner circles
num_points_outer = int(math.ceil(outer_circumference / max_distance))
num_points_inner = int(math.ceil(inner_circumference / max_distance))

# Use the maximum number of points to ensure both circles are smooth
num_points = max(num_points_outer, num_points_inner)

# Create the donut shape with specified parameters
donut = gdspy.Round(
    center=center,
    radius=outer_radius,
    inner_radius=inner_radius,
    initial_angle=0,
    final_angle=2 * math.pi,
    number_of_points=num_points,
    max_points=0,
    tolerance=None,
    layer=0,
    datatype=0,
)

# Add the donut shape to the cell
cell.add(donut)

# Save the library to a GDS file with specified units and precision
lib.write_gds('donut.gds', unit=unit, precision=precision)