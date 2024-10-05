import gdspy

# Define the GDS library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('triangle')

# Define the triangle vertices
x = 0
y = 0
edge_length = 10
triangle_vertices = [(x - edge_length/2, y - edge_length/(2*3**0.5)), 
                     (x + edge_length/2, y - edge_length/(2*3**0.5)), 
                     (x, y + edge_length/3**0.5)]

# Create the triangle as a polygon
triangle = gdspy.Polygon(triangle_vertices, layer=1)

# Add the triangle to the cell
cell.add(triangle)

# Save the design to a GDS file
lib.write_gds('triangle.gds')