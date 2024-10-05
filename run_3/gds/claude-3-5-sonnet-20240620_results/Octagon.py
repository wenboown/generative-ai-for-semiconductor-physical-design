import gdspy
import numpy as np

# Calculate the radius of the circumscribed circle
side_length = 10  # 10 mm
radius = side_length / (2 * np.sin(np.pi / 8))

# Calculate vertex coordinates
angles = np.linspace(0, 2*np.pi, 9)[:-1]  # 8 equally spaced angles
vertices = [(radius * np.cos(angle), radius * np.sin(angle)) for angle in angles]

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