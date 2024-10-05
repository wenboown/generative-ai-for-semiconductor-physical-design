import gdspy
import math

# Create a GDSII library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('HEPTAGON')

# Heptagon parameters
n_sides = 7               # Number of sides
side_length = 10.0        # Side length in mm
center = (0.0, 0.0)       # Center of the heptagon

# Calculate the radius of the circumscribed circle
R = side_length / (2 * math.sin(math.pi / n_sides))

# Calculate the coordinates of the vertices
vertices = []
for i in range(n_sides):
    theta = (2 * math.pi / n_sides) * i  # Angle for the current vertex
    x = center[0] + R * math.cos(theta)
    y = center[1] + R * math.sin(theta)
    vertices.append((x, y))

# Create the polygon and add it to the cell
heptagon = gdspy.Polygon(vertices)
cell.add(heptagon)

# Write the GDSII file
lib.write_gds('heptagon.gds')

# Optional: View the layout using gdspy's internal viewer
# Uncomment the following line to display the heptagon