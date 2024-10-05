import gdspy

# Create a new GDSII library
lib = gdspy.GdsLibrary()

# Create a cell
cell = lib.new_cell('CELL')

# Define layers
ACTIVE_LAYER = 1
POLY_LAYER = 2
CONTACT_LAYER = 3

# Active regions
# Dimensions: 20 µm x 5 µm
# Positioned horizontally with 5 µm spacing between them
active_regions = []
# First rectangle
active1 = gdspy.Rectangle((0, 0), (20, 5), layer=ACTIVE_LAYER)
active_regions.append(active1)
# Second rectangle
active2 = gdspy.Rectangle((25, 0), (45, 5), layer=ACTIVE_LAYER)
active_regions.append(active2)
# Third rectangle
active3 = gdspy.Rectangle((50, 0), (70, 5), layer=ACTIVE_LAYER)
active_regions.append(active3)

# Add active regions to cell
for active in active_regions:
    cell.add(active)

# Polysilicon gate pattern
# Grid-like structure of vertical and horizontal lines
# Line width: 0.5 µm
poly_lines = []

# Grid parameters
x_min, x_max = 0, 70   # x range
y_min, y_max = -5, 15  # y range to cover area beyond active regions

line_width = 0.5

# Vertical lines every 2 µm
x_positions = [x for x in range(int(x_min), int(x_max)+1, 2)]
for x in x_positions:
    x0 = x - line_width / 2
    x1 = x + line_width / 2
    poly_line = gdspy.Rectangle((x0, y_min), (x1, y_max), layer=POLY_LAYER)
    cell.add(poly_line)

# Horizontal lines every 2 µm
y_positions = [y for y in range(int(y_min), int(y_max)+1, 2)]
for y in y_positions:
    y0 = y - line_width / 2
    y1 = y + line_width / 2
    poly_line = gdspy.Rectangle((x_min, y0), (x_max, y1), layer=POLY_LAYER)
    cell.add(poly_line)

# Contact holes
# 1 µm x 1 µm squares at intersections of polysilicon grid and active regions
contact_size = 1.0

for x in x_positions:
    for y in y_positions:
        # Check if intersection point is within any active region
        point_in_active = False
        for active in active_regions:
            (ax0, ay0), (ax1, ay1) = active.get_bounding_box()
            if ax0 <= x <= ax1 and ay0 <= y <= ay1:
                point_in_active = True
                break
        if point_in_active:
            # Place a contact hole centered at (x, y)
            x0 = x - contact_size / 2
            x1 = x + contact_size / 2
            y0 = y - contact_size / 2
            y1 = y + contact_size / 2
            contact = gdspy.Rectangle((x0, y0), (x1, y1), layer=CONTACT_LAYER)
            cell.add(contact)

# Save the GDSII file
lib.write_gds('layout_design.gds')