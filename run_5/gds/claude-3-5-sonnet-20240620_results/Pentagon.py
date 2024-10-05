import gdspy
import numpy as np

# Calculate the coordinates of the pentagon vertices
def calculate_pentagon_vertices(side_length, center=(0, 0)):
    radius = side_length / (2 * np.sin(np.pi / 5))
    angles = np.linspace(np.pi / 2, 5 * np.pi / 2, 6)[:-1]
    vertices = [(radius * np.cos(angle) + center[0], radius * np.sin(angle) + center[1]) for angle in angles]
    return vertices

# Set up the parameters
side_length = 10000  # 10 mm in nanometers
center = (0, 0)

# Calculate the vertices
pentagon_vertices = calculate_pentagon_vertices(side_length, center)

# Create a new library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('PENTAGON')

# Create the pentagon polygon
pentagon = gdspy.Polygon(pentagon_vertices, layer=0)

# Add the pentagon to the cell
cell.add(pentagon)

# Save the design to a GDS file
lib.write_gds('pentagon.gds')

print("Pentagon GDS file has been generated successfully.")