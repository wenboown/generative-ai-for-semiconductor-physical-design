import gdspy
import numpy as np

# Define the hexagon parameters
edge_length = 10000  # 10 mm in nanometers
center_x, center_y = 0, 0

# Calculate the radius of the circumscribed circle
radius = edge_length

# Calculate the coordinates of the hexagon vertices
angles = np.linspace(0, 2*np.pi, 7)[:-1]  # 6 equally spaced angles
x_coords = center_x + radius * np.cos(angles)
y_coords = center_y + radius * np.sin(angles)

# Combine x and y coordinates into a list of points
hexagon_points = list(zip(x_coords, y_coords))

# Create a new GDS library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell("Hexagon")

# Create the hexagon polygon
hexagon = gdspy.Polygon(hexagon_points, layer=0)

# Add the hexagon to the cell
cell.add(hexagon)

# Save the GDS file
lib.write_gds("hexagon.gds")

print("Hexagon GDS file has been generated successfully.")