import gdspy

# Create a new GDSII library
lib = gdspy.GdsLibrary()

# Create a new cell for our design
cell = lib.new_cell('Layout')

# Define dimensions and spacing
active_width = 20.0
active_height = 5.0
spacing = 5.0
poly_width = 0.5
contact_size = 1.0

# Draw three rectangular active regions
for i in range(3):
    x_offset = i * (active_width + spacing)
    active_region = gdspy.Rectangle(
        (x_offset, 0), 
        (x_offset + active_width, active_height)
    )
    cell.add(active_region)

# Create complex polysilicon gate pattern (grid-like structure)
num_lines = 10  # Number of lines across the pattern
pattern_spacing = 2.5  # Spacing between grid lines

# Vertical lines
for i in range(num_lines):
    x = i * pattern_spacing
    poly_line_v = gdspy.Rectangle(
        (x, -pattern_spacing), 
        (x + poly_width, active_height + 10)  # Cover active region and enough height for intersections
    )
    cell.add(poly_line_v)

# Horizontal lines
for j in range(num_lines):
    y = j * pattern_spacing
    poly_line_h = gdspy.Rectangle(
        (-pattern_spacing, y), 
        (3 * (active_width + spacing), y + poly_width)
    )
    cell.add(poly_line_h)

# Add contact holes at intersections of polysilicon grid and active regions
for i in range(num_lines):
    for j in range(num_lines):
        x_contact = i * pattern_spacing
        y_contact = j * pattern_spacing

        # Determine if contact point is within any active region bounds
        for k in range(3):
            x_offset = k * (active_width + spacing)
            if (x_offset <= x_contact <= (x_offset + active_width)) and (0 <= y_contact <= active_height):
                contact_hole = gdspy.Rectangle(
                    (x_contact - contact_size / 2, y_contact - contact_size / 2),
                    (x_contact + contact_size / 2, y_contact + contact_size / 2)
                )
                cell.add(contact_hole)

# Output the design to a GDSII file
lib.write_gds('layout_design.gds')