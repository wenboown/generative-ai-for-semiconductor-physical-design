import gdspy
import numpy as np

# Define octagon parameters
edge_length = 10  # mm
center = (0, 0)

# Calculate the radius of the circumscribed circle
radius = edge_length / (2 * np.sin(np.pi / 8))

# Generate vertex coordinates
angles = np.linspace(0, 2*np.pi, 9)[:-1]  # 8 equally spaced angles
vertices = [(radius * np.cos(angle) + center[0], 
             radius * np.sin(angle) + center[1]) for angle in angles]

# Create a new library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('OCTAGON')

# Create the octagon polygon
octagon = gdspy.Polygon(vertices)

# Add the octagon to the cell
cell.add(octagon)

# Save the design to a GDS file
lib.write_gds('octagon.gds')

print("Octagon GDS file has been generated successfully.")