import gdspy
import numpy as np

def create_regular_pentagon(edge_length):
    # Number of sides
    n_sides = 5
    
    # Angle in radians between each point
    internal_angle = 2 * np.pi / n_sides
    
    # Radius of circumscribed circle
    radius = edge_length / (2 * np.sin(np.pi / n_sides))
    
    # Vertices of the pentagon
    vertices = [(radius * np.cos(i * internal_angle), 
                 radius * np.sin(i * internal_angle)) for i in range(n_sides)]
    
    return vertices

# Define parameters
edge_length = 10000  # in micrometers (10mm)
center = (0, 0)

# Create vertices for the pentagon
pentagon_vertices = create_regular_pentagon(edge_length)

# Create a GDSII library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('PENTAGON')

# Add the pentagon to the cell
polygon = gdspy.Polygon(pentagon_vertices, layer=1)
cell.add(polygon)

# Write the layout to a GDS file
lib.write_gds('regular_pentagon.gds')

print("Regular pentagon with each edge 10 mm has been generated.")