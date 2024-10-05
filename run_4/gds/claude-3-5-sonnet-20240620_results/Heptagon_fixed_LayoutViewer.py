import gdspy
import numpy as np

# Create a new library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('HEPTAGON')

# Define the edge length (in micrometers, as GDS uses um)
edge_length = 10000  # 10 mm = 10000 um

# Calculate the radius of the circumscribed circle
radius = edge_length / (2 * np.sin(np.pi / 7))

# Generate the coordinates of the heptagon vertices
angles = np.linspace(0, 2*np.pi, 8)[:-1]  # 7 evenly spaced angles
vertices = [(radius * np.cos(angle), radius * np.sin(angle)) for angle in angles]

# Create the heptagon polygon
heptagon = gdspy.Polygon(vertices, layer=0)

# Add the heptagon to the cell
cell.add(heptagon)

# Save the design to a GDS file
lib.write_gds('heptagon.gds')

# Optional: View the layout