import gdspy

# Define the library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell("layout")

# Step 1: Draw three rectangular active regions
active_width = 20  # width in micrometers
active_height = 5  # height in micrometers
spacing = 5  # spacing between regions in micrometers

# Define the active region shapes
for i in range(3):
    x_offset = i * (active_width + spacing)
    active_region = gdspy.Rectangle((x_offset, 0), (x_offset + active_width, active_height))
    cell.add(active_region)

# Step 2: Create complex polysilicon gate pattern (grid-like structure)
poly_width = 0.5  # width of polysilicon lines in micrometers
grid_spacing = 2  # spacing between grid lines in micrometers

# Define vertical lines of the grid
for i in range(5):
    x_pos = i * grid_spacing
    poly_line = gdspy.Rectangle((x_pos, -active_height), (x_pos + poly_width, 2 * active_height + active_height))
    cell.add(poly_line)

# Define horizontal lines of the grid
for i in range(5):
    y_pos = -active_height + i * grid_spacing
    poly_line = gdspy.Rectangle((0, y_pos), (3 * (active_width + spacing), y_pos + poly_width))
    cell.add(poly_line)

# Step 3: Add contact holes at intersections
contact_size = 1  # size of contact hole in micrometers

# Define the contact holes at the intersections
for i in range(5):
    x_pos = i * grid_spacing
    for j in range(5):
        y_pos = -active_height + j * grid_spacing
        if 0 <= y_pos <= active_height:
            for k in range(3):
                x_offset = k * (active_width + spacing)
                contact_hole = gdspy.Rectangle((x_pos + x_offset - contact_size / 2, y_pos - contact_size / 2), (x_pos + x_offset + contact_size / 2, y_pos + contact_size / 2))
                cell.add(contact_hole)

# Save the design to a GDS file
lib.write_gds('layout_design.gds')

# To inspect the created layout visually in Python (optional)