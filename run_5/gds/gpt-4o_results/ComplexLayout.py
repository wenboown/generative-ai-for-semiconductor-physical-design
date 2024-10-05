import gdspy

# Create a new GDSII library, with 0.001um precision.
lib = gdspy.GdsLibrary(precision=1e-3)

# Create a new cell for our design.
cell = lib.new_cell('CELL')

# Define dimensions and spacing.
active_width = 20.0
active_height = 5.0
spacing = 5.0

# Draw three rectangular active regions with 5µm spacing between them.
x_offset = 0
for i in range(3):
    active_region = gdspy.Rectangle(
        (x_offset, 0),
        (x_offset + active_width, active_height)
    )
    cell.add(active_region)
    x_offset += active_width + spacing

# Define the polysilicon gate pattern dimensions.
poly_width = 0.5
num_vertical_lines = 10
num_horizontal_lines = 10
pattern_width = 2.5

# Create the polysilicon gate pattern in a grid-like structure.
# Vertical lines.
for i in range(num_vertical_lines):
    x = i * pattern_width
    poly_line_v = gdspy.Rectangle(
        (x, -pattern_width),
        (x + poly_width, 3 * (active_height + spacing))
    )
    cell.add(poly_line_v)

# Horizontal lines.
for j in range(num_horizontal_lines):
    y = j * pattern_width
    poly_line_h = gdspy.Rectangle(
        (-poly_width, y),
        (num_vertical_lines * pattern_width, y + poly_width)
    )
    cell.add(poly_line_h)

# Add contact holes at intersections of polysilicon gate pattern and active regions.
contact_size = 1.0
x_base = -pattern_width + poly_width / 2.0
y_base = poly_width / 2.0

for i in range(num_vertical_lines):
    x = x_base + i * pattern_width
    for j in (range(num_horizontal_lines)):
        y = y_base + j * pattern_width
        for k in range(3):
            if 0 <= y - k * (active_height + spacing) <= active_height:
                contact_hole = gdspy.Rectangle(
                    (x - contact_size / 2.0, y - contact_size / 2.0),
                    (x + contact_size / 2.0, y + contact_size / 2.0)
                )
                cell.add(contact_hole)

# Output the design to a GDSII file.
lib.write_gds('layout_design.gds')