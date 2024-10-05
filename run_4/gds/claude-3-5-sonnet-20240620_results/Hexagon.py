import gdspy
import numpy as np

# Create a new library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('HEXAGON')

# Define hexagon parameters
edge_length = 10000  # 10 mm in μm
center = (0, 0)

# Calculate vertex coordinates
angles = np.linspace(0, 2*np.pi, 7)[:-1]  # 6 equally spaced angles
vertices = [(edge_length * np.cos(angle) + center[0],
             edge_length * np.sin(angle) + center[1]) for angle in angles]

# Create the hexagon polygon
hexagon = gdspy.Polygon(vertices)

# Add the hexagon to the cell
cell.add(hexagon)

# Save the design to a GDS file
lib.write_gds('hexagon.gds')

print("Hexagon GDS file has been generated successfully.")