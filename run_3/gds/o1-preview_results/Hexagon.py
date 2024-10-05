import gdspy
import numpy as np

# Define the parameters for the hexagon
center_x, center_y = 0, 0  # Center coordinates (in micrometers)
side_length = 10000  # Side length of the hexagon in micrometers (10 mm = 10,000 μm)

# For a regular hexagon, the radius of the circumscribed circle is equal to the side length
radius = side_length

# Calculate the angles at which the vertices of the hexagon will be located
num_sides = 6
angles = np.linspace(0, 2 * np.pi, num_sides, endpoint=False)

# Compute the x and y coordinates of the vertices
x_coords = center_x + radius * np.cos(angles)
y_coords = center_y + radius * np.sin(angles)
points = np.column_stack((x_coords, y_coords))

# Create a new GDSII library
lib = gdspy.GdsLibrary()

# Create a new cell named 'HEXAGON'
cell = lib.new_cell('HEXAGON')

# Create the hexagon polygon using the calculated points
hexagon = gdspy.Polygon(points)

# Add the hexagon to the cell
cell.add(hexagon)

# Save the GDSII file
lib.write_gds('hexagon.gds')