import gdspy
import math

# Define the library and cell for the GDS layout
lib = gdspy.Library()
cell = lib.new_cell("Heptagon")

# Calculate the coordinates for the heptagon
n_sides = 7
radius = 10 / (2 * math.sin(math.pi / n_sides))
coords = [(radius * math.cos(2 * math.pi * i / n_sides), 
           radius * math.sin(2 * math.pi * i / n_sides)) for i in range(n_sides)]

# Create the heptagon polygon
heptagon = gdspy.Polygon(coords, layer=1)

# Add the heptagon to the cell
cell.add(heptagon)

# Save the design to a GDS file
lib.write_gds("heptagon.gds")