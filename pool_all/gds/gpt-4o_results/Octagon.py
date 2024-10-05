import gdspy
import numpy as np

# Define octagon parameters
edge_length = 10  # Edge length in mm
num_sides = 8  # Number of sides
center_x, center_y = 0, 0  # Center at (0, 0)

# Calculate the radius of the circumcircle
radius = edge_length / (2 * np.sin(np.pi / num_sides))

# Calculate vertex coordinates
angles = np.linspace(0, 2 * np.pi, num_sides, endpoint=False)
vertices = [(center_x + radius * np.cos(angle), center_y + radius * np.sin(angle)) for angle in angles]

# Create a GDSII library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('OCTAGON')

# Create the octagon polygon
octagon = gdspy.Polygon(vertices)

# Add the octagon to the cell
cell.add(octagon)

# Save the design to a GDS file
lib.write_gds('octagon.gds')

print("Octagon GDS file 'octagon.gds' has been created successfully.")