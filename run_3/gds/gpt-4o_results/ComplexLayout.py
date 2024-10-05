import gdspy

# Create the library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('LAYOUT')

# Function to draw a rectangle
def draw_rectangle(cell, x, y, width, height, layer):
    rect = gdspy.Rectangle((x, y), (x + width, y + height), layer=layer)
    cell.add(rect)

# Draw three rectangular active regions
active_width = 20.0
active_height = 5.0
spacing = 5.0
start_x = 0
start_y = 0
layer_active = 1
for i in range(3):
    draw_rectangle(cell, start_x + i * (active_width + spacing), start_y, active_width, active_height, layer_active)

# Create polysilicon gate pattern (grid-like structure)
poly_width = 0.5
poly_spacing = 2.5
layer_poly = 2

# Horizontal lines
for i in range(4):  # 3 lines inside + 1 at the bottom edge
    y = start_y + i * poly_spacing
    draw_rectangle(cell, start_x, y, 3 * (active_width + spacing) - spacing, poly_width, layer_poly)

# Vertical lines
for i in range(13):  # Enough to cover the width of 3 active regions plus spacing
    x = start_x + i * poly_spacing
    draw_rectangle(cell, x, start_y, poly_width, 3 * active_height, layer_poly)

# Adding contact holes at intersections (1 µm x 1 µm)
contact_size = 1.0
layer_contact = 3

# Loop through each intersection point between polysilicon and active regions
for i in range(13):
    for j in range(4):
        x_contact = start_x + i * poly_spacing - contact_size / 2 + poly_width / 2
        y_contact = start_y + j * poly_spacing - contact_size / 2 + poly_width / 2
        # Check if this contact overlaps with any active region
        if ((x_contact > start_x and x_contact < start_x + active_width) or
            (x_contact > start_x + active_width + spacing and x_contact < start_x + active_width * 2 + spacing) or
            (x_contact > start_x + (active_width + spacing) * 2 and x_contact < start_x + active_width * 3 + spacing * 2)):
            draw_rectangle(cell, x_contact, y_contact, contact_size, contact_size, layer_contact)

# Save the layout to a GDS file
lib.write_gds('layout_design.gds')

print("GDS layout design successfully created!")