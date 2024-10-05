import gdspy

# Create a new GDSII library
lib = gdspy.GdsLibrary()

# Create a cell
cell = lib.new_cell('ARROW')

# Define dimensions in micrometers
L = 10000  # Total length of the arrow in um (10 mm)
H_length = L / 4  # Arrowhead length (2.5 mm)
S_length = L - H_length  # Shaft length (7.5 mm)

W_head = 3000  # Width of the arrowhead in um (3 mm)
W_body = W_head / 3  # Width of the shaft (1 mm)

# Shaft coordinates
shaft = gdspy.Rectangle((0, -W_body / 2), (S_length, W_body / 2))

# Arrowhead coordinates
arrowhead = gdspy.Polygon([
    (S_length, -W_head / 2),
    (L, 0),
    (S_length, W_head / 2)
])

# Add shapes to the cell
cell.add(shaft)
cell.add(arrowhead)

# Save the GDSII file
lib.write_gds('arrow.gds')