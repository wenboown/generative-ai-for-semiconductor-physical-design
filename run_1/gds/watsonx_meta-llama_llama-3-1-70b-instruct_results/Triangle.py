import gdspy

# Step 1: Parse the user's design specifications
edge_length = 10  # mm
center_x, center_y = 0, 0  # mm

# Step 2: Define the library and cell for the GDS layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell("triangle")

# Step 3: Create each geometric element (e.g., rectangles, polygons) with precise coordinates
# Define the vertices of the triangle
vertices = [
    (center_x - edge_length / 2, center_y + edge_length * 0.8660254037844386 / 2),
    (center_x + edge_length / 2, center_y + edge_length * 0.8660254037844386 / 2),
    (center_x, center_y - edge_length * 0.8660254037844386 / 2)
]

# Create a polygon for the triangle
poly = gdspy.Polygon(vertices, layer=1)

# Step 4: Add the polygon to the cell
cell.add(poly)

# Step 5: Save the design to a GDS file
lib.write_gds("triangle.gds")