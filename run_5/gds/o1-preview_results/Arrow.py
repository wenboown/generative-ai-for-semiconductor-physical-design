import gdspy

# Create a new GDSII library to contain the design.
lib = gdspy.GdsLibrary()

# Create a new cell ('ARROW') to hold the arrow geometry.
cell = lib.new_cell('ARROW')

# Define dimensions in micrometers (1 mm = 1000 um).
Lb = 7000    # Length of the arrow body in um (7 mm)
Lh = 3000    # Length of the arrowhead in um (3 mm)
L = Lb + Lh  # Total length of the arrow in um (10 mm)
Wb = 1000    # Width of the arrow body in um (1 mm)
Wh = 3000    # Width of the arrowhead at the base in um (3 mm)

# Define the body of the arrow as a rectangle.
# The body starts at (0, -Wb/2) and ends at (Lb, Wb/2).
body = gdspy.Rectangle((0, -Wb / 2), (Lb, Wb / 2))

# Define the arrowhead as a polygon (triangle).
# The arrowhead base aligns with the end of the body at x = Lb.
arrowhead = gdspy.Polygon([
    (Lb, -Wh / 2),   # Left base point of the arrowhead.
    (Lb, Wh / 2),    # Right base point of the arrowhead.
    (L, 0)           # Tip of the arrowhead.
])

# Add the body and arrowhead to the cell.
cell.add([body, arrowhead])

# Save the library in a GDSII file called 'arrow.gds'.
lib.write_gds('arrow.gds')