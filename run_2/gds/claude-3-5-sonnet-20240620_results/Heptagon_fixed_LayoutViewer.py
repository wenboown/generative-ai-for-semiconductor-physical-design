import gdspy
import numpy as np

# Create a new library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('HEPTAGON')

# Calculate the radius of the circumscribed circle
edge_length = 10000  # 10 mm in nanometers
radius = edge_length / (2 * np.sin(np.pi / 7))

# Calculate the coordinates of the heptagon vertices
angles = np.linspace(0, 2*np.pi, 8)[:-1]  # 7 equally spaced angles
vertices = radius * np.column_stack((np.cos(angles), np.sin(angles)))

# Create the heptagon polygon
heptagon = gdspy.Polygon(vertices, layer=0)

# Add the heptagon to the cell
cell.add(heptagon)

# Save the design to a GDS file
lib.write_gds('heptagon.gds')

# Display all cells using the built-in viewer