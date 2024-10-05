import numpy as np
import gdspy

# Create a new GDSII library
lib = gdspy.GdsLibrary()

# Create a cell in the library named 'HEXAGON'
cell = lib.new_cell('HEXAGON')

# Number of sides for the hexagon
num_sides = 6

# Edge length in micrometers (10 mm = 10,000 µm)
edge_length = 10000.0

# Calculate the radius of the circumscribed circle (distance from center to a vertex)
# For a regular hexagon, the radius is equal to the edge length
radius = edge_length

# Generate the angles for each vertex of the hexagon
angles = np.linspace(0, 2 * np.pi, num_sides, endpoint=False)

# Calculate the (x, y) coordinates for each vertex
x_coords = radius * np.cos(angles)
y_coords = radius * np.sin(angles)
vertices = list(zip(x_coords, y_coords))

# Create the hexagon as a polygon with the calculated vertices
hexagon = gdspy.Polygon(vertices)

# Add the hexagon to the cell
cell.add(hexagon)

# Save the library in a GDSII file named 'hexagon.gds'
lib.write_gds('hexagon.gds')