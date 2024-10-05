import gdspy
import math

# Create a new GDSII library and add a cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('HEPTAGON')

# Parameters
n = 7  # Number of sides for the heptagon
s = 10000  # Side length in micrometers (10 mm = 10,000 µm)
center = (0, 0)  # Center of the heptagon

# Calculate the radius of the circumcircle
# R = s / (2 * sin(π / n))
R = s / (2 * math.sin(math.pi / n))

# Generate the vertices of the heptagon
vertices = []
for i in range(n):
    angle = 2 * math.pi * i / n  # Angle for each vertex
    x = center[0] + R * math.cos(angle)
    y = center[1] + R * math.sin(angle)
    vertices.append((x, y))

# Create the heptagon polygon
heptagon = gdspy.Polygon(vertices)

# Add the heptagon to the cell
cell.add(heptagon)

# Save the GDSII file
lib.write_gds('heptagon.gds')