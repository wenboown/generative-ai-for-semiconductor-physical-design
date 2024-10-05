import gdspy

# Create a GDSII library
lib = gdspy.GdsLibrary()

# Create a cell to contain the geometry
cell = lib.new_cell('ARROW')

# Define parameters in mm, convert to um
scale = 1000  # scale factor from mm to um

total_length_mm = 10.0  # Total length of the arrow in mm
start_x_mm = 0.0        # Starting x-coordinate in mm
start_y_mm = 0.0        # Starting y-coordinate in mm
L_head_mm = 2.0         # Length of the arrow head in mm
L_body_mm = total_length_mm - L_head_mm  # Length of the arrow body in mm
w_head_mm = 3.0         # Width of the arrow head at the base in mm
w_body_mm = w_head_mm / 3.0  # Width of the arrow body (1/3 of the head width)

# Convert dimensions from mm to um
total_length = total_length_mm * scale
start_x = start_x_mm * scale
start_y = start_y_mm * scale
L_head = L_head_mm * scale
L_body = L_body_mm * scale
w_head = w_head_mm * scale
w_body = w_body_mm * scale

# Coordinates for the arrow body (rectangle)
body_coords = [
    (start_x, start_y - w_body / 2),
    (start_x, start_y + w_body / 2),
    (start_x + L_body, start_y + w_body / 2),
    (start_x + L_body, start_y - w_body / 2)
]

# Coordinates for the arrow head (triangle)
head_coords = [
    (start_x + L_body, start_y - w_head / 2),
    (start_x + L_body, start_y + w_head / 2),
    (start_x + total_length, start_y)
]

# Create polygons for the body and head
body = gdspy.Polygon(body_coords)
head = gdspy.Polygon(head_coords)

# Add the polygons to the cell
cell.add([body, head])

# Save the layout to a GDSII file
lib.write_gds('arrow.gds')