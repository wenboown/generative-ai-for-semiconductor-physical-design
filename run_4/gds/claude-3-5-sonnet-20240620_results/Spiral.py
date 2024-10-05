import gdspy
import numpy as np

# Create a new library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('SPIRAL')

# Define the parametric equations for the spiral
def spiral_x(t):
    return np.exp(-0.1 * t) * np.cos(t)

def spiral_y(t):
    return np.exp(-0.1 * t) * np.sin(t)

# Generate points along the spiral
t = np.linspace(0, 6 * np.pi, 1000)
x = spiral_x(t)
y = spiral_y(t)

# Scale the spiral to a reasonable size (e.g., 100 units wide)
scale_factor = 50 / np.max(np.abs(x))
x *= scale_factor
y *= scale_factor

# Create a polygon path for the spiral
points = np.column_stack((x, y))
spiral = gdspy.FlexPath(points, 1, layer=0)

# Add the spiral to the cell
cell.add(spiral)

# Save the design to a GDS file
lib.write_gds('parametric_spiral.gds')

print("GDS file 'parametric_spiral.gds' has been generated.")