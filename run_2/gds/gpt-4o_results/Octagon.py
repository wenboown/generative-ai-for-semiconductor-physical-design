import gdspy
import math

# Function to calculate the vertices of a regular octagon centered at (0, 0)
def calculate_octagon_vertices(edge_length):
    # The angle between each vertex (in radians)
    angle = math.pi / 4  # 360 degrees / 8 sides = 45 degrees = pi/4 radians
    radius = edge_length / (2 * math.sin(math.pi / 8))
    
    vertices = []
    for i in range(8):
        theta = angle * i
        x = radius * math.cos(theta)
        y = radius * math.sin(theta)
        vertices.append((x, y))
    
    return vertices

# Define the edge length of the octagon
edge_length = 10

# Calculate the vertices
vertices = calculate_octagon_vertices(edge_length)

# Create a new GDSII library
lib = gdspy.GdsLibrary()

# Create a cell to contain the polygon
cell = lib.new_cell('OCTAGON')

# Create the octagon polygon
octagon = gdspy.Polygon(vertices)

# Add the polygon to the cell
cell.add(octagon)

# Save the layout to a GDS file
lib.write_gds('octagon.gds')

# Display a summary of the library
print(lib)