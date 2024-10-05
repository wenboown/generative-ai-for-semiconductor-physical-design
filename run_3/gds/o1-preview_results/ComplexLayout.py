import gdspy

# Create a new GDSII library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('LAYOUT')

# Define units (default is micrometers in gdspy)
# Layer numbers for different layers
ACTIVE_LAYER = 1
POLY_LAYER = 2
CONTACT_LAYER = 3

# 1. Draw three rectangular active regions (20 µm x 5 µm) with 5 µm spacing between them
active_regions = []
for i in range(3):
    # Calculate the x-coordinate for each active region
    x_start = i * (20 + 5)  # 20 µm width + 5 µm spacing
    x_end = x_start + 20
    # Create the rectangle for the active region
    active = gdspy.Rectangle((x_start, 0), (x_end, 5), layer=ACTIVE_LAYER)
    active_regions.append(active)
    cell.add(active)

# 2. Create a complex polysilicon gate pattern (grid-like structure)
# Vertical polysilicon lines (width 0.5 µm)
vertical_lines = []
for x in range(0, 71, 5):  # From 0 µm to 70 µm with 5 µm intervals
    x_center = x
    x_left = x_center - 0.25  # Half of 0.5 µm width
    x_right = x_center + 0.25
    vertical_line = gdspy.Rectangle((x_left, -5), (x_right, 10), layer=POLY_LAYER)
    vertical_lines.append(vertical_line)
    cell.add(vertical_line)

# Horizontal polysilicon lines (width 0.5 µm)
horizontal_lines = []
for y in [0, 2, 4]:  # At y = 0 µm, 2 µm, and 4 µm
    y_center = y
    y_bottom = y_center - 0.25  # Half of 0.5 µm width
    y_top = y_center + 0.25
    horizontal_line = gdspy.Rectangle((-5, y_bottom), (75, y_top), layer=POLY_LAYER)
    horizontal_lines.append(horizontal_line)
    cell.add(horizontal_line)

# Combine vertical and horizontal lines to form the grid
poly_lines = vertical_lines + horizontal_lines

# 3. Add contact holes (1 µm x 1 µm) at intersections of polysilicon and active regions
contact_size = 1.0  # 1 µm x 1 µm contact hole
contact_half = contact_size / 2

# Function to create contact holes at intersection points
def create_contact_holes(active_region, poly_line):
    # Check for intersection between active region and polysilicon line
    intersection = gdspy.boolean(active_region, poly_line, 'and')
    if intersection:
        # Get the bounding boxes of the intersection areas
        for poly in intersection.polygons:
            xmin, ymin = poly.min(axis=0)
            xmax, ymax = poly.max(axis=0)
            # Calculate the center of the intersection area
            x_center = (xmin + xmax) / 2
            y_center = (ymin + ymax) / 2
            # Define the contact hole rectangle around the center point
            contact_hole = gdspy.Rectangle(
                (x_center - contact_half, y_center - contact_half),
                (x_center + contact_half, y_center + contact_half),
                layer=CONTACT_LAYER
            )
            cell.add(contact_hole)

# Create contact holes at all intersections
for active in active_regions:
    for poly_line in poly_lines:
        create_contact_holes(active, poly_line)

# Save the layout to a GDSII file
lib.write_gds('layout.gds')