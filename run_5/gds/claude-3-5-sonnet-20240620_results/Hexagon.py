import gdspy
import numpy as np

# Set the unit of measurement (1 unit = 1 mm)
gdspy.library.use_current_library = False
lib = gdspy.GdsLibrary(unit=1e-3, precision=1e-9)

# Create a new cell
cell = lib.new_cell('HEXAGON')

# Hexagon parameters
edge_length = 10  # mm
radius = edge_length

# Calculate vertices
angles = np.linspace(0, 2*np.pi, 7)[:-1]  # 6 angles, excluding the last (duplicate) point
vertices = radius * np.array([np.cos(angles), np.sin(angles)]).T

# Create the hexagon polygon
hexagon = gdspy.Polygon(vertices)

# Add the hexagon to the cell
cell.add(hexagon)

# Save the design to a GDS file
lib.write_gds('hexagon.gds')

print("Hexagon GDS file has been generated successfully.")