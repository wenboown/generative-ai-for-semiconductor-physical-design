import gdspy

# Create a new GDSII library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('ARROW')

# Dimensions in micrometers
length_shaft = 8000  # Shaft length in um (8 mm)
length_head = 2000   # Arrowhead length in um (2 mm)
W_head = 3000        # Width of the arrowhead base in um (3 mm)
W_body = 1000        # Width of the shaft in um (1 mm)

# Shaft coordinates
shaft = gdspy.Rectangle((0, -W_body / 2), (length_shaft, W_body / 2))

# Arrowhead coordinates
arrowhead_points = [
    (length_shaft, W_head / 2),
    (length_shaft, -W_head / 2),
    (length_shaft + length_head, 0)
]
arrowhead = gdspy.Polygon(arrowhead_points)

# Add shapes to cell
cell.add(shaft)
cell.add(arrowhead)

# Write the GDSII file
lib.write_gds('arrow.gds')