import gdspy
import numpy as np

# Create a new library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('HEXAGON')

# Calculate the coordinates of the hexagon vertices
radius = 10  # mm
angles = np.linspace(0, 2*np.pi, 7)[:-1]  # 6 equally spaced angles
x_coordinates = radius * np.cos(angles)
y_coordinates = radius * np.sin(angles)

# Create a list of coordinate pairs
vertices = list(zip(x_coordinates, y_coordinates))

# Create the hexagon polygon
hexagon = gdspy.Polygon(vertices, layer=0)

# Add the hexagon to the cell
cell.add(hexagon)

# Save the design to a GDS file
lib.write_gds('hexagon.gds')

print("Hexagon GDS file has been generated successfully.")