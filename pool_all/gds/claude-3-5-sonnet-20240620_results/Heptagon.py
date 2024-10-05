import gdspy
import numpy as np

# Create a new library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('HEPTAGON')

# Heptagon parameters
num_sides = 7
edge_length = 10000  # 10 mm in nanometers
center = (0, 0)

# Calculate the radius of the circumscribed circle
radius = edge_length / (2 * np.sin(np.pi / num_sides))

# Generate the coordinates of the heptagon vertices
angles = np.linspace(0, 2*np.pi, num_sides, endpoint=False)
vertices = [(radius * np.cos(angle) + center[0], radius * np.sin(angle) + center[1]) for angle in angles]

# Create the heptagon polygon
heptagon = gdspy.Polygon(vertices)

# Add the heptagon to the cell
cell.add(heptagon)

# Save the design to a GDS file
lib.write_gds('heptagon.gds')

print("Heptagon GDS file has been generated successfully.")