import gdspy
import numpy as np

# Calculate the radius for a 10 mm edge length
edge_length = 10  # mm
radius = edge_length / (2 * np.sin(np.pi/8))

# Generate vertex coordinates
angles = np.arange(0, 2*np.pi, 2*np.pi/8)
vertices = radius * np.column_stack((np.cos(angles), np.sin(angles)))

# Create a new library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('OCTAGON')

# Create the octagon polygon
octagon = gdspy.Polygon(vertices, layer=0)

# Add the octagon to the cell
cell.add(octagon)

# Save the design to a GDS file
lib.write_gds('octagon.gds')

# Optional: View the layout