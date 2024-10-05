import gdspy

# Define units (GDSII uses micrometers)
mm_to_um = 1000.0  # 1 mm = 1000 micrometers

# Design parameters in micrometers
L_total = 10 * mm_to_um         # Total length: 10 mm
W_head = 3 * mm_to_um           # Width of arrowhead: 3 mm
W_shaft = W_head / 3            # Width of arrow shaft: 1/3 of W_head
L_head = W_head                 # Length of arrowhead: equal to W_head
L_shaft = L_total - L_head      # Length of arrow shaft

# Coordinates for arrow shaft (rectangle)
shaft_x0 = 0
shaft_y0 = -W_shaft / 2
shaft_x1 = L_shaft
shaft_y1 = W_shaft / 2

# Coordinates for arrowhead (triangle)
tip_point = (L_total, 0)
base_upper = (L_shaft, W_head / 2)
base_lower = (L_shaft, -W_head / 2)

# Create a new GDSII library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('ARROW')

# Create arrow shaft as a rectangle
shaft = gdspy.Rectangle((shaft_x0, shaft_y0), (shaft_x1, shaft_y1))

# Create arrowhead as a polygon (triangle)
arrowhead = gdspy.Polygon([tip_point, base_upper, base_lower])

# Add the shaft and arrowhead to the cell
cell.add([shaft, arrowhead])

# Save the library in a GDSII file
lib.write_gds('arrow.gds')

# Optional: View the layout using the internal viewer (commented out)