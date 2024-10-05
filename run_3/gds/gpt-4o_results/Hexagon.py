import gdspy
import math

def generate_hexagon(side_length, center=(0, 0)):
    # Compute the vertices of the regular hexagon
    angle_deg = 60
    angle_rad = math.pi / 180 * angle_deg
    vertices = []
    for i in range(6):
        x = center[0] + side_length * math.cos(i * angle_rad)
        y = center[1] + side_length * math.sin(i * angle_rad)
        vertices.append((x, y))
    
    return gdspy.Polygon(vertices)

# Create a GDSII library
gdsii_library = gdspy.GdsLibrary()

# Create a new cell
cell = gdsii_library.new_cell("HEXAGON")

# Define the hexagon side length as 10 mm
side_length = 10.0

# Generate the hexagon and add it to the cell
hexagon = generate_hexagon(side_length)
cell.add(hexagon)

# Save the layout to a GDS file
gdsii_library.write_gds("hexagon.gds")

print("Hexagon layout has been created and saved as 'hexagon.gds'")
sh
pip install gdspy