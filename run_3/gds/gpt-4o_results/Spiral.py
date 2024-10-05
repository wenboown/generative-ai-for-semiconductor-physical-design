import gdspy
import numpy as np

# Define the parametric equation for the spiral r(t) = e^(-0.1*t)
def spiral_points(t_values):
    points = []
    for t in t_values:
        r = np.exp(-0.1 * t)
        x = r * np.cos(t)
        y = r * np.sin(t)
        points.append((x, y))
    return points

# Generate t values ranging from 0 to 6*pi
t_values = np.linspace(0, 6 * np.pi, num=1000)  # Increasing the number of points for smooth curve

# Get the points of the spiral
points = spiral_points(t_values)

# Define the GDSII library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('SPIRAL')

# Define the path with a width of 1 unit
path = gdspy.Path(1, points[0])

# Create the spiral path by adding segments
for point in points[1:]:
    path.segment(abs(point[0] - path.x) + abs(point[1] - path.y), direction=None, final_point=point)

# Add the path to the cell
cell.add(path)

# Save the layout to a GDS file
lib.write_gds('parametric_spiral.gds')