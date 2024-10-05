import gdspy
import numpy as np

# Define parameters
side_length = 10.0  # Edge length of the octagon in mm
num_sides = 8       # Number of sides for an octagon
center = (0.0, 0.0) # Center of the octagon at (0, 0)

# Calculate the radius of the circumscribed circle
# r = side_length / (2 * sin(pi / num_sides))
radius = side_length / (2 * np.sin(np.pi / num_sides))

# Compute the vertices of the octagon
vertices = []
for i in range(num_sides):
    angle = np.pi / num_sides + i * (2 * np.pi / num_sides)  # Start angle offset for symmetry
    x = center[0] + radius * np.cos(angle)
    y = center[1] + radius * np.sin(angle)
    vertices.append((x, y))

# Create a GDSII library with units in millimeters
gdsii_unit = 1e-3  # 1 unit = 1 mm
precision = 1e-9   # Precision of 1 nanometer
lib = gdspy.GdsLibrary(unit=gdsii_unit, precision=precision)

# Create a cell to contain the layout
cell = lib.new_cell('OCTAGON_CELL')

# Create the octagon polygon
octagon = gdspy.Polygon(vertices, layer=1)

# Add the octagon to the cell
cell.add(octagon)

# Save the layout to a GDS file
lib.write_gds('octagon.gds')

# Optionally, display the layout (requires matplotlib)