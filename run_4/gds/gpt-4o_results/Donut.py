import gdspy

# Create a library and a cell to hold the geometry
lib = gdspy.GdsLibrary()
cell = lib.new_cell('DONUT')

# Define the donut parameters
outer_radius = 10.0  # in mm
inner_radius = 5.0   # in mm
max_points_distance = 0.01  # in mm

# Calculate the number of points needed to achieve the smoothness
import math

def calculate_points(radius, max_distance):
    return max(3, int(2 * math.pi * radius / max_distance))

# Create the donut shape using gdspy.Round
inner_points = calculate_points(inner_radius, max_points_distance)
outer_points = calculate_points(outer_radius, max_points_distance)

donut = gdspy.Round(
    (0, 0), 
    outer_radius, 
    inner_radius=inner_radius, 
    number_of_points=max(inner_points, outer_points)
)

# Add the shape to the cell
cell.add(donut)

# Save the GDS layout to a file
lib.write_gds('donut.gds')

print("Donut shape GDS file created successfully.")