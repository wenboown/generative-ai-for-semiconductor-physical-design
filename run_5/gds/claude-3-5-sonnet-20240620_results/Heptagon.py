import gdspy
import numpy as np

# Define the library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('HEPTAGON')

# Heptagon parameters
num_sides = 7
edge_length = 10e3  # 10 mm converted to nanometers (standard unit in GDS)

# Calculate the radius of the circumscribed circle
radius = edge_length / (2 * np.sin(np.pi / num_sides))

# Generate the coordinates of the heptagon vertices
angles = np.linspace(0, 2*np.pi, num_sides, endpoint=False)
vertices = np.column_stack((radius * np.cos(angles), radius * np.sin(angles)))

# Create the heptagon polygon
heptagon = gdspy.Polygon(vertices)

# Add the heptagon to the cell
cell.add(heptagon)

# Save the design to a GDS file
lib.write_gds('heptagon.gds')

print("Heptagon GDS file has been generated successfully.")