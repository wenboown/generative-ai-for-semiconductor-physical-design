import gdspy
import numpy as np

# Function to create a regular pentagon centered at (0, 0) with each edge length
def create_regular_pentagon(edge_length):
    # Number of sides
    n_sides = 5
    
    # Angle between each point in radians
    internal_angle = 2 * np.pi / n_sides
    
    # Calculate the radius of the circumscribed circle
    radius = edge_length / (2 * np.sin(np.pi / n_sides))
    
    # Calculate the vertices of the pentagon
    vertices = [(radius * np.cos(i * internal_angle), 
                 radius * np.sin(i * internal_angle)) for i in range(n_sides)]
    
    return vertices

# Create vertices for the pentagon
pentagon_vertices = create_regular_pentagon(edge_length=10)

# Create a GDSII library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('PENTAGON')

# Add the pentagon to the cell
polygon = gdspy.Polygon(pentagon_vertices, layer=1)
cell.add(polygon)

# Write the layout to a GDS file
gdspy.write_gds('regular_pentagon.gds', [cell])

print("Regular pentagon with each edge 10 mm has been generated.")