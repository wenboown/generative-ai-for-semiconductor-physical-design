import gdspy
import numpy as np

# Constants
EDGE_LENGTH = 10  # Length of each edge of the octagon in mm
CENTER = (0, 0)  # Center of the octagon
NUM_SIDES = 8  # Number of sides for the octagon

# Calculate the radius of the circumcircle of the octagon
radius = EDGE_LENGTH / (2 * np.sin(np.pi / NUM_SIDES))

# Calculate the vertices of the octagon
theta = np.linspace(0, 2 * np.pi, NUM_SIDES, endpoint=False)
vertices = [(CENTER[0] + radius * np.cos(t), CENTER[1] + radius * np.sin(t)) for t in theta]

# Create a new GDS library and cell
gdsii_lib = gdspy.GdsLibrary()
cell = gdsii_lib.new_cell('OCTAGON')

# Create the octagon polygon and add it to the cell
octagon = gdspy.Polygon(vertices)
cell.add(octagon)

# Save the layout to a GDS file
gdsii_lib.write_gds('octagon.gds')

print("Octagon GDS file generated successfully!")