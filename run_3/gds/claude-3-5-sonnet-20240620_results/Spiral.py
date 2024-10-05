import gdspy
import numpy as np

def generate_spiral_points(start_t, end_t, num_points):
    t = np.linspace(start_t, end_t, num_points)
    r = np.exp(-0.1 * t)
    x = r * np.cos(t)
    y = r * np.sin(t)
    return np.column_stack((x, y))

# Create a new library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('SPIRAL')

# Generate spiral points
spiral_points = generate_spiral_points(0, 6*np.pi, 1000)

# Scale the spiral (optional, adjust as needed)
scale_factor = 100  # Adjust this value to change the size of the spiral
spiral_points *= scale_factor

# Create a path for the spiral
path = gdspy.FlexPath(
    spiral_points,
    1,  # width of the line
    layer=0,
    datatype=0
)

# Add the path to the cell
cell.add(path)

# Save the design to a GDS file
lib.write_gds('parametric_spiral.gds')

print("GDS file 'parametric_spiral.gds' has been generated.")